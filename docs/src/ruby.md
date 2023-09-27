# Ruby

## Gem

### Gem commands

```
gem list bundler
gem install bundler -v 1.17.3 --source 'https://gems.ruby-china.com/'

# Not work?
bundle _1.17.3_ install

gem uninstall bundler -v 2.2.15
```

## Bundler

Invoke bundle commands outside of a project:

```
BUNDLE_GEMFILE=PATH_TO_GEMFILE bundle exec rails new --api foo
```

### Bundler fails to install mysql2 on Mac OSX

Error:

```
ld: library not found for -lssl
```

To solve the above error, install `mysql2` using below options with `gem install`:

```
-- --with-ldflags=-L/usr/local/opt/openssl/lib --with-cppflags=-I/usr/local/opt/openssl/include
```

Ref: https://stackoverflow.com/questions/43523389/cannot-install-mysql2-gem-for-rails-project

Error:

```
./result.h:24:3: error: unknown type name 'my_bool'
  my_bool *is_null;
```

```
brew install mysql-client@5.7
```

Then run `gem install` with below options, you may need to update the path
below.

```
-- --with-mysql-config=/usr/local/Cellar/mysql-client@5.7/5.7.32/bin/mysql_config
```

### Bundler fails to install rmagick on Mac OSX

Error:

```
checking for outdated ImageMagick version (<= 6.7.7)... no
checking for __GNUC__... yes
checking for Ruby version >= 2.3.0... yes
checking for magick/MagickCore.h... no


ERROR: Can't install RMagick 4.0.0. Can't find magick/MagickCore.h.
```

To solve the above error, first make sure you have `imagemagick@6` installed, if
not, install it by `brew install imagemagick@6`. Then run `bundle install`
again.

Error:

```
checking for clang... yes
checking for Magick-config... no
checking for pkg-config... yes
checking for outdated ImageMagick version (<= 6.4.9)... no
checking for presence of MagickWand API (ImageMagick version >= 6.9.0)... no
checking for Ruby version >= 1.8.5... yes
checking for stdint.h... yes
checking for sys/types.h... yes
checking for wand/MagickWand.h... no

Can't install RMagick 2.16.0. Can't find MagickWand.h.
```

```
export PKG_CONFIG_PATH="/usr/local/opt/imagemagick@6/lib/pkgconfig"
```

```
-- --with-ldflags=-L/usr/local/opt/imagemagick@6/lib --with-cppflags=-I/usr/local/opt/imagemagick@6/include
```

### Bundler fails to install ffi on Mac OSX

Error:

```
Call.c:355:5: error: implicit declaration of function 'rb_thread_call_without_gvl' is invalid in C99
[-Werror,-Wimplicit-function-declaration]
```

To solve the above error, install `ffi` using below options with `gem install`:

```
-- --with-cflags="-Wno-error=implicit-function-declaration"
```

## Run specified tests for minitest

```
rake test TEST=test/test_foo.rb TESTOPTS="--name=test_foo_method -v"
ruby -Ilib -Itest test/test_foo.rb --name=test_foo_method
```

Ref: https://guides.rubyonrails.org/testing.html#the-rails-test-runner

## RSpec

Configuration options are loaded from `~/.rspec`, `.rspec`, `.rspec-local`,
command line switches, and the `SPEC_OPTS` environment variable (listed in
lowest to highest precedence; for example, an option in `~/.rspec` can be
overridden by an option in `.rspec-local`).

```
SPEC_OPTS='--fail-fast' bundle exec rspec
SPEC_OPTS='--no-fail-fast' bundle exec rspec
```

Ref: https://relishapp.com/rspec/rspec-core/v/3-7/docs/configuration/read-command-line-configuration-options-from-files

## Pass in compiler options when installing a gem

For example, on Mac 10.15.6, installing puma 4.3.5 fails with:

```
puma_http11.c:203:22: error: implicitly declaring library function 'isspace' with type 'int (int)' [-Werror,-Wimplicit-function-declaration]
```

We can resolve this issue by:

```
gem install puma:4.3.5 -- --with-cflags="-Wno-error=implicit-function-declaration"
```

Ref: https://github.com/puma/puma/issues/2304


## Push a gem to rubygems.org

* Using bundler

First check the file `~/.gem/credentials` exists and an API key is specified in
that file as below shown.

```
---
:rubygems_api_key: YOUR_API_KEY
```

Then run rake task to push.

```
bundle exec rake release
```

## mina

Remove assets cache.

```
command %{#{fetch(:rake)} assets:clobber}
```

## Text string encoding

```
utf8_str = "测试"
puts utf8_str.encoding
packed_str = utf8_str.bytes.pack("C*")
puts utf8_str.unicode_str(prefix: '\u', separator: '')
puts utf8_str.bytes_str(prefix: '\x', separator: '')

gbk_str = utf8_str.encode('gbk')
puts gbk_str.encoding
packed_str = gbk_str.bytes.pack("C*")
puts gbk_str.bytes_str(prefix: '\x', separator: '')

# Result is ASCII-8BIT
puts packed_str.encoding

packed_str.force_encoding('gbk')
packed_str.encode('utf-8')

unicode_str = "\u6d4b\u8bd5"
String.new("\xb2\xe2\xca\xd4", encoding: 'gbk').encode('utf-8')
```
