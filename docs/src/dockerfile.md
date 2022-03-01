# Dockerfile

## CMD

```
# This won't work
CMD ["sh", "-c", "ant", "-Djmeter.home=$JMETER_HOME/"]

# This works
CMD ["sh", "-c", "ant -Djmeter.home=$JMETER_HOME/"]
```

https://stackoverflow.com/questions/40454470/how-can-i-use-a-variable-inside-a-dockerfile-cmd

Also see https://hub.docker.com/r/curlimages/curl

## COPY

```
COPY hom* /mydir/
```

Ref: https://docs.docker.com/engine/reference/builder/#copy
