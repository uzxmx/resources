# java-library-gradle

This project demonstrates how to make a java library and publish it to the local
maven repository by gradle.

For a demo which uses this library, please see
[java-application-gradle](../java-application-gradle/README.md).

### Publish to local maven repository

```
./gradlew publishToMavenLocal
```

After running the above command, the library should be published to
`~/.m2/repository/com/example/my-library`.

For more info about publishing, please see [the doc](https://docs.gradle.org/current/userguide/publishing_maven.html).
