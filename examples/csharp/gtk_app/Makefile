all: Hello.exe
	@mono $^

Hello.exe: Hello.cs
	@mcs $< -pkg:gtk-sharp-2.0
