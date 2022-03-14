all: Hello.exe
	@mono $^

Utility.dll: Utility.cs
	@mcs -target:library -out:$@ $^

Hello.exe: Hello.cs Utility.dll
	@mcs -r:Utility.dll $<
