# Console application

## Create new application

```
dotnet new console -o <app-name>
cd <app-name>
dotnet add package System.CommandLine --prerelease
```

For more information about `System.CommandLine`, please visit [here](https://github.com/dotnet/command-line-api).

## Run the application

```
dotnet run -- -h
dotnet run -- list -h
dotnet run -- list -s foo --int 5 --file README.md
```

## Build the application

```
dotnet build -o build
```
