all: main

main: main.cpp
	@g++ -g -o $@ $^

lldb: main
	@lldb --one-line "break set -n printBuffer" \
		--one-line "break set -n Buffer::Print" \
		--one-line "run" \
		main
