# OpenSSL

## PKCS: Public Key Cryptography Standards

### PKCS#1

The first of a family of standards for PKCS. OpenSSL by default generates RSA
private keys with this syntax.

### PKCS#8

A standard syntax for storing private key information. Java by default adopts
this syntax for RSA private keys.

```
# Convert RSA private key from default format to PKCS#8.
openssl pkcs8 -topk8 -inform PEM -in private_key.pem -out private_key_pkcs8.pem -nocrypt
```

### PKCS#12

A container file format commonly used to store private keys with accompanying
public key certificates, protected with a password-based symmetric key.
The file usually comes with `.p12` or `.pfx` extension.

Ref: https://en.wikipedia.org/wiki/PKCS

## Ruby throws error: SSL_connect returned=1 errno=0 state=error: certificate verify failed (unable to get local issuer certificate) (OpenSSL::SSL::SSLError)

This error might be caused by the target host using a `chain.pem`, not a `fullchain.pem`.

```
ruby -ropenssl -e 'puts OpenSSL::X509::DEFAULT_CERT_FILE'
ruby -ropenssl -e 'puts OpenSSL::SSL::VERIFY_PEER'
```

One workaround for ruby is adding below codes:

```
require 'openssl'
OpenSSL::SSL::VERIFY_PEER = OpenSSL::SSL::VERIFY_NONE
```

## How to generate self signed certificate with custom root CA

### Create root CA

#### Create root key

Attention: this is the key used to sign the certificate requests, anyone holding this can sign certificates on your behalf. So keep it in a safe place!

```
# If you want to encrypt the key, you can add -des3 option or other encryption option.
# By default the numbits is 2048, you can change it to other value, e.g. 4096.
# For more info, please see `openssl genrsa -h`.
openssl genrsa -out rootCA.key
```

#### Create root certificate

```
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt
```

### Create a certificate

#### Create certificate key

```
openssl genrsa -out mydomain.com.key
```

#### Create the certificate signing request

```
# Interactive way
openssl req -new -key mydomain.com.key -out mydomain.com.csr

# One liner way for automation
openssl req -new -sha256 -key mydomain.com.key -subj "/C=US/ST=CA/O=MyOrg, Inc./CN=mydomain.com" -out mydomain.com.csr
```

If you need to pass additional config you can use the -config parameter, here for example I want to add alternative names to my certificate.

```
openssl req -new -sha256 \
    -key mydomain.com.key \
    -subj "/C=US/ST=CA/O=MyOrg, Inc./CN=mydomain.com" \
    -reqexts SAN \
    -config <(cat /etc/ssl/openssl.cnf \
        <(printf "\n[SAN]\nsubjectAltName=DNS:mydomain.com,DNS:www.mydomain.com")) \
    -out mydomain.com.csr
```

#### Verify the csr's content

```
openssl req -in mydomain.com.csr -noout -text
```

#### Generate the certificate using the csr and key along with the CA root key

```
openssl x509 -req -in mydomain.com.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out mydomain.com.crt -days 500 -sha256
```

#### Verify the certificate's content

```
openssl x509 -in mydomain.com.crt -text -noout
```

## ECC (Elliptic Curve Cryptography)

#### List curves

```
# Print list of all currently implemented EC parameter names.
# For example: secp256k1, secp224r1, etc.
openssl ecparam -list_curves
```

#### Generate EC private key

```
openssl ecparam -name secp256k1 -genkey -noout -out ec_privkey.pem

# Show the EC private key.
openssl ec -in ec_privkey.pem -text -noout
```

#### Generate EC private key from BIGNUM

Suppose you want to create a EC private key from a BIGNUM whose hexadecimal is `68FC5456FEA519EEA03CCBC5E4961961246641A3A58F8894CDD4C3003DB14F07` by using `secp256k1`.

```
# Generate EC private key with DER format.
openssl asn1parse -genconf <(echo -e "asn1=SEQUENCE:seq_sect\n[seq_sect]\nfield1=INT:1\nfield2=FORMAT:HEX,OCT:68FC5456FEA519EEA03CCBC5E4961961246641A3A58F8894CDD4C3003DB14F07\nfield3=EXP:0,OID:secp256k1") -out ec_privkey.der

# Show the EC private key with DER format.
openssl ec -in ec_privkey.der -inform der -text -noout

# Convert DER to PEM.
openssl ec -in ec_privkey.der -inform der -out ec_privkey.pem

# Show the EC private key with PEM format.
openssl ec -in ec_privkey.pem -text -noout
```

#### Generate EC public key from BIGNUM

```
# Generate EC public key with DER format.
openssl asn1parse -genconf <(echo -e "asn1=SEQUENCE:pubkey\n[pubkey]\nseq=SEQUENCE:info\nbn=FORMAT:HEX,BITSTRING:04d8ec05ca4018312a650f4147052b7e82337a9f07b5f4e041917a09a28cb0bfa4733012f45d5b10c81b89bd34d8906be9e13604703536d9f91aca82449b0f30ad\n[info]\nid=OID:id-ecPublicKey\ncurve=OID:secp256k1") -out ec_pubkey.der

# Show the EC public key with DER format.
openssl ec -in ec_pubkey.der -inform der -pubin -text -noout

# Convert DER to PEM.
openssl ec -in ec_pubkey.der -inform der -pubin -out ec_pubkey.pem

# Show the EC public key with PEM format.
openssl ec -in ec_pubkey.pem -pubin -text -noout
```

#### Other commands

```
# Show EC private key in DER format.
openssl ec -in ec_privkey.der -inform der -text

# Show EC public key.
openssl ec -in pubkey.der -pubin -inform der

# Generate EC public key in PEM format from private key.
openssl ec -in privkey.der -inform der -pubout -out pubkey.pem

# Generate EC public key in DER format from private key.
openssl ec -in privkey.der -inform der -pubout -out pubkey.der -outform der
```

## ECDH

Compute the exchanged key:

```
# For PEM format.
openssl pkeyutl -derive -inkey ec_privkey.pem -peerkey peer_pubkey.pem | hexdump -e '16/1 "%02x"'

# Use MD5 as KDF.
openssl pkeyutl -derive -inkey ec_privkey.pem -peerkey peer_pubkey.pem | openssl md5

# For DER format.
openssl pkeyutl -derive -inkey <(openssl ec -in ec_privkey.der -inform der 2>/dev/null) -peerkey <(openssl ec -in peer_pubkey.der -inform der -pubin 2>/dev/null) | hexdump -e '16/1 "%02x"'
```

### KDF

https://man.openbsd.org/ECDH_compute_key.3

## Build OpenSSL 3.0.0

```
curl -L -O https://www.openssl.org/source/openssl-3.0.0.tar.gz
tar zxvf openssl-3.0.0.tar.gz
mkdir openssl-build
cd openssl-3.0.0
./Configure --prefix="$(pwd)/../openssl-build"
make
make install
```

For more information, please see `INSTALL.md` in the root source directory.

## asn1parse

`asn1parse` is the command to display internal structure of a DER document,
which is a binary format for data structures described by ASN.1.

For more information, please visit https://wiki.openssl.org/index.php/DER.

#### Show ASN1

```
# Show ASN1 for a PEM file.
openssl asn1parse -in key.pem

# Dump BIT STRING.
openssl asn1parse -in key.pem -dump

# Show ASN1 for a DER file.
openssl asn1parse -in key.der -inform der
```

#### Generate ASN1

```
openssl asn1parse -genstr "UTF8:Hello World"

# Ref: https://www.openssl.org/docs/man3.0/man3/ASN1_generate_nconf.html
openssl asn1parse -genconf <(echo -e "asn1=SEQUENCE:seq_sect\n[seq_sect]\nfield1=INT:1\nfield2=FORMAT:HEX,OCT:68FC5456FEA519EEA03CCBC5E4961961246641A3A58F8894CDD4C3003DB14F07\nfield3=EXP:0,OID:secp256k1")
```

### EC

https://wiki.openssl.org/index.php/Command_Line_Elliptic_Curve_Operations
https://wiki.openssl.org/index.php/Libcrypto_API
https://wiki.openssl.org/index.php/Elliptic_Curve_Diffie_Hellman
https://jameshfisher.com/2017/04/14/openssl-ecc/
https://wiki.openssl.org/index.php/EVP_Key_Derivation
https://stackoverflow.com/questions/15686821/generate-ec-keypair-from-openssl-command-line
https://www.scottbrady91.com/openssl/creating-elliptical-curve-keys-using-openssl
https://security.stackexchange.com/questions/131297/openssl-generate-ecdh-public-key

### KDF

```
# export HEX_KEY=3215d2a6cc353c74e3ba108a4b8a900c3f21ff82cc95c13ccc346d5be7eb2f86
# export DIGEST=sha256
# export DIGEST=md5
# docker run --rm uzxmx/openssl openssl kdf -keylen 32 -kdfopt digest:$DIGEST -kdfopt hexkey:$HEX_KEY -kdfopt hexsalt:67e6096a85ae67bb72f36e3c3af54fa5 -kdfopt hexinfo:7f520e518c68059babd9831f19cde05b HKDF
# 
# docker run --rm uzxmx/openssl openssl kdf -keylen 56 -kdfopt digest:$DIGEST -kdfopt hexkey:$HEX_KEY -kdfopt mode:EXPAND_ONLY -kdfopt hexinfo:68616e647368616b65206b657920657870616e73696f6ec9b71584264b11ece10b4fd2885d3fc5f44c9fa6d13096e4d308cf414ae09944 HKDF
```

### AES crypto

```
# AES-128-CBC, decrypt without pad
xxd -r -p msg.txt | openssl enc -d -aes128 -K '404b553b23385a596c48416669232652' -iv 404b553b23385a596c48416669232652 -nopad

# Decrypt with pad
xxd -r -p cipher.txt | openssl enc -d -aes128 -K '8d58a133ee724f57a3a9bb4f6b57a806' -iv 8d58a133ee724f57a3a9bb4f6b57a806

# Encrypt with pad
xxd -r -p plaintext.txt | openssl enc -aes128 -K 'dd21177677eb9fbbcc2afe9549b68abc' -iv dd21177677eb9fbbcc2afe9549b68abc
```

### Start a TLS server

```
# https://stackoverflow.com/questions/21319841/signing-certificate-with-another-certificate-signed-by-ca
# openssl s_server -key key.pem -cert cert.pem -accept 4443 -www
# openssl s_client -connect localhost:4443
# openssl - verify
```

### DES crypto

```
# Decrypt
openssl enc -d -des -K <hexadecimal> -iv <hexadecimal>
```
