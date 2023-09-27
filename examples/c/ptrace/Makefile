all: main

main: main.c
	@clang -g -o $@ $^

lldb: main
	@lldb --one-line "break set -f main.c -l 14" \
		--one-line "run" \
		main
