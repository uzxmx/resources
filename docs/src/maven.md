## Commands

```
# https://github.com/LearnLib/learnlib/wiki/Setting-Up-a-New-Maven-Project-(Command-Line)
# https://www.vogella.com/tutorials/ApacheMaven/article.html
mvn archetype:generate

# https://stackoverflow.com/questions/1089285/maven-run-project
mvn exec:java -Dexec.mainClass=foo.App
mvn test
mvn -Dtest=com.example.Test test
mvn -Dtest=com.example.Test#foo test

mvn install -DskipTests
# Use `maven.test.skip` property to skip compiling the tests
mvn install -Dmaven.test.skip=true

# Run spring boot project.
mvn spring-boot:run
```

## Show help

```
mvn help:help -Ddetail=true
mvn help:describe
mvn help:describe -Dcmd=spring-boot:run -Ddetail
mvn help:describe -Dplugin=org.jacoco:jacoco-maven-plugin -Ddetail
```

## Redirect output to file when using surefire to test

```
# Output will be saved in PROJECT_ROOT/target/surefire-reports/xxx-output.txt
mvn test -Dmaven.test.redirectTestOutputToFile=true
```

## Pass system properties to maven test

Specify properties in command line as below:

```
# http://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html#argLine
mvn test -DargLine="-DpropertyName=propertyValue"
```

We can also add system properties in `maven-surefire-plugin` configuration
section of `pom.xml`. Find examples
[here](https://maven.apache.org/surefire/maven-surefire-plugin/examples/system-properties.html).

If we want to pass environment variables to maven test, we can declare the
environment variables in the same way as most linux commands.

## Get dependency tree

```
mvn dependency:tree
```

Ref: https://stackoverflow.com/questions/3342908/how-to-get-a-dependency-tree-for-an-artifact

## Download sources for jar

```
mvn dependency:sources

# You can get group id and artifact id from `mvn dependency:tree`.
# TODO this doesn't work for `org.eclipse.jdt.core`.
mvn dependency:sources -DincludeGroupIds=p2.eclipse-plugin -DincludeArtifactIds=org.eclipse.jdt.core
```

Ref:
https://stackoverflow.com/questions/27971430/how-to-download-sources-for-an-specific-jar-dependency-of-a-maven-project
https://www.baeldung.com/maven-download-sources-javadoc
