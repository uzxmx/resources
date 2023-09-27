# Arthas

```
ognl '@java.lang.System@out.println("hello world")'

# Not work
ognl '@com.example.service.ArthasService@getApplicationContext()'

# Get classLoaderClass
sc -d com.example.service.ArthasService

ognl --classLoaderClass org.springframework.boot.devtools.restart.classloader.RestartClassLoader '#context=@com.example.service.ArthasService@getApplicationContext(), #context.getBean("companyService")'

ognl --classLoaderClass org.springframework.boot.devtools.restart.classloader.RestartClassLoader '#context=@com.example.service.ArthasService@getApplicationContext(), #repository=#context.getBean("staffWalletConsumptionRepository"), #repository.findById(1)'

ognl --classLoaderClass org.springframework.boot.devtools.restart.classloader.RestartClassLoader '#context=@com.example.service.ArthasService@getApplicationContext(), #repository=#context.getBean("channelRepository"), #repository.findAll()'

ognl --classLoaderClass org.springframework.boot.loader.LaunchedURLClassLoader '#context=@com.example.service.ArthasService@getApplicationContext(), #repository=#context.getBean("channelRepository"), #repository.findAll()'

ognl --classLoaderClass org.springframework.boot.loader.LaunchedURLClassLoader '#context=@com.example.service.ArthasService@getApplicationContext(), #repository=#context.getBean("staffWalletConsumptionRepository"), #repository.findById(1)'

ognl --classLoaderClass org.springframework.boot.loader.LaunchedURLClassLoader '#context=@com.example.service.ArthasService@getApplicationContext(), #service=#context.getBean("foo"), #service.testMethod("bar")'
```
