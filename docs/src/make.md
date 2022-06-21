# Make

### Variable expansion

```
# This is wrong, it means `$f`oo.
$foo

Below the two forms are equivalent.
$(foo)
${foo}
```

### Automatic variables

`$@`: The file name of the target of the rule

`$<`: The name of the first prerequisite.

`$^`: The names of all the prerequisites, with spaces between them.

Ref: https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html

### List all targets

```
make -qp | awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ {split($1,A,/ /);for(i in A)print A[i]}' | sort -u
```

Ref:
* https://stackoverflow.com/questions/4219255/how-do-you-get-the-list-of-targets-in-a-makefile
* https://stackoverflow.com/questions/3063507/list-goals-targets-in-gnu-make-that-contain-variables-in-their-definition

### Check variables

#### Using prerequisite

```
foo: check-variables
	@$(docker_push)

check-variables:
ifeq ($(FOO),)
	$(error FOO is required)
endif
```

Ref: https://stackoverflow.com/questions/4728810/how-to-ensure-makefile-variable-is-set-as-a-prerequisite

#### Using shell

```
define bar
if test "$(FOO)" = "" ; then echo "FOO is required"; exit 1; fi
echo "$(FOO)"
endef

foo:
	@$(bar)
```

### Current working directory

```
make -C /path

$(PWD)
$(shell pwd)
```

Ref: https://stackoverflow.com/questions/18136918/how-to-get-current-relative-directory-of-your-makefile

### Functions

```
DOCKER_BUILD_ARGS := $(addprefix --build-arg ,$(shell cat "$(PWD)/build_args.txt"))
```
