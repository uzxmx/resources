all: main

main: main.cpp
	@clang++ -std=c++11 -g -o $@ $^

lldb: main
	@lldb --one-line "break set -n printBuffer" \
		--one-line "break set -n Buffer::Print" \
		--one-line "run" \
		main
