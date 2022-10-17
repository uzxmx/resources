android-lib:
	gomobile bind -target android -ldflags='-s -w' -o ./android/app/libs/hello.aar ./hello

android-app:
	cd ./android && ./gradlew build
