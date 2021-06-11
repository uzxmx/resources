## Commands

```
# Exclude ./kubespray directory, note the differences with --exclude='kubespray' and --exclude='kubespray/'
rsync -avuz -e 'ssh -p 1234 -o "SetEnv=AssetName=host Interactive=no"' --exclude='/kubespray/' . user@host:/tmp/foo

rsync -avuz -e 'ssh -p 1234 -o "SetEnv=AssetName=host Interactive=no"' --exclude='/.git/' --exclude='/kubespray/' --exclude='/.local/' --exclude='*.swp' --exclude='*.swo' . user@host:/tmp/foo

# Resume transfering a partial file.
rsync -P user@host:path_to_a_large_file .
```
