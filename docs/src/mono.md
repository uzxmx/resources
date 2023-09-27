# Mono

## Build mono on Mac OSX

```
git clone --depth=1 https://github.com/mono/mono.git
cd mono
# Get dependencies beforehand.
# TODO we also need to get dependencies for `external/linker` submodule.
git submodule update --init --depth=1 --progress
./autogen.sh --prefix=$PREFIX --disable-nls
make
make install
```

## mscorlib.dll

CIL image

## API

```
MonoDomain *
mono_init (const char *domain_name);

MonoDomain *
mono_init_from_assembly (const char *domain_name, const char *filename);

MonoDomain *
mono_init_version (const char *domain_name, const char *version);

MonoAssembly *
mono_assembly_load_corlib (const MonoRuntimeInfo *runtime, MonoImageOpenStatus *status);

MonoClass *
mono_class_load_from_name (MonoImage *image, const char* name_space, const char *name);
```
