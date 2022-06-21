# Docker

<!-- vim-markdown-toc GFM -->

* [Common services](#common-services)
* [Bind mounts](#bind-mounts)
* [Commands](#commands)
  * [Run a container](#run-a-container)
  * [Show node labels](#show-node-labels)
  * [Build a docker image with http proxy](#build-a-docker-image-with-http-proxy)
  * [Swarm mode](#swarm-mode)
    * [Commands](#commands-1)
    * [Rolling update a service](#rolling-update-a-service)
* [Troubleshooting](#troubleshooting)
    * [`ctrl-p` behaving unexpectedly under Docker](#ctrl-p-behaving-unexpectedly-under-docker)
    * [`docker exec -it some-container bash` results in `stty -a` with 0 cols and 0 rows](#docker-exec--it-some-container-bash-results-in-stty--a-with-0-cols-and-0-rows)
* [Mirror sites](#mirror-sites)
    * [For images from docker.io](#for-images-from-dockerio)
    * [For images from gcr.io](#for-images-from-gcrio)
    * [For images from k8s.gcr.io](#for-images-from-k8sgcrio)
    * [For images from quay.io](#for-images-from-quayio)
* [Access host port from container](#access-host-port-from-container)
* [Dockerfile](#dockerfile)
  * [CMD](#cmd)
  * [COPY](#copy)

<!-- vim-markdown-toc -->

## Common services

```
# Run MySQL server.
docker run --name mysql-server -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7.32

# Run redis server.
docker run --name redis-server -p 6379:6379 -d redis:5.0.12

# Run openssl command.
docker run --rm uzxmx/openssl openssl version
```

## Bind mounts

If you want to mount a file or directory on the host machine into a docker
container, you can use bind mounts.

There are two kinds of flags: `-v` / `--volume` and `--mount`.
The main difference is when using `--mount`, an error
will be thrown if the source file doesn't exist, whereas when using
`-v` / `--volume`, the source file will be created as a directory if it doesn't exist.

```
# Source file should be an absolute path.
docker run --rm -e FOO=true -e BAR=false -v "$(pwd)/docker/docker-entrypoint.sh:/docker-entrypoint.sh" -p 8080:80 <image>

docker run --rm -e FOO=true -e BAR=false --mount type=bind,source="$(pwd)/foo/docker-entrypoint.sh",target=/docker-entrypoint.sh -p 8080:80 <image>
```

Ref: https://docs.docker.com/storage/bind-mounts/

## Commands

### Run a container

```
# Start a container and publish container port 8080 to host port 3000.
docker run -p 3000:8080 <image-name>

# We can also start an interactive shell and execute command, so we can use
# `docker exec -it <container-id> bash` to update codes and restart process.
docker run -p 3000:8080 -it <image-name> bash

docker run -it --rm busybox:1.32.0 sh

# Connect to host network. This only works on Linux. For docker on Mac, the
# daemon actually runs in a VM, so the host is the VM host. For workaround, use
# `host.docker.internal` DNS name to reach the Mac host.
# For more info, please visit https://docs.docker.com/docker-for-mac/networking/
docker run --rm --network host busybox:1.32.0 nc -zv localhost 80
docker run --rm --network host busybox:1.32.0 nc -zv host.docker.internal 80
```

### Show node labels

```
docker node ls -q | xargs docker node inspect \
  -f '{{ .ID }} [{{ .Description.Hostname }}]: {{ .Spec.Labels }}'

docker node ls -q | xargs docker node inspect \
  -f '{{ .ID }} [{{ .Description.Hostname }}]: {{ range $k, $v := .Spec.Labels }}{{ $k }}={{ $v }} {{end}}'
```

### Build a docker image with http proxy

```
docker build . -f docker/Dockerfile --build-arg http_proxy=http://192.168.1.5:8123
```

### Swarm mode

#### Commands

```
# Initialize a swarm cluster if there isn't one.
docker swarm init

# Create a network.
docker network create --driver=overlay --attachable public

# Deploy a stack.
docker stack deploy --compose-file docker-compose.yml <stack-name>

# List all services of a stack.
docker stack services <stack-name>

# Show details of a service.
docker service inspect <service-name>
docker service inspect <service-name> -f "{{ .ID }}"
docker service inspect <service-name> -f "{{ join .Spec.TaskTemplate.ContainerSpec.Env \"\n\" }}"
docker service inspect <service-name> -f "{{ range .Spec.TaskTemplate.ContainerSpec.Env }}{{ print . \"\n\" }}{{ end }}"
```

#### Rolling update a service

```
docker service update -d <service-name> --force
docker service update -d --image <image> <service-name> --force
```

## Troubleshooting

#### `ctrl-p` behaving unexpectedly under Docker

The command sequence to detach from a docker container is `ctrl-p` `ctrl-q`,
which is why `ctrl-p` doesn't work as expected. When you hit `ctrl-p`, docker is
waiting on `ctrl-q`, so nothing happens.

You can use the new --detach-keys argument to docker run to override this
sequence to be something other than `ctrl-p`:

```
docker run -ti --detach-keys="ctrl-@" ubuntu:14.04 bash
```

If you want, you can add this to your `~/.docker/config.json` file to persist
this change:

```
{
  ...
  "detachKeys": "ctrl-@",
  ...
}
```

Ref: https://stackoverflow.com/questions/41820108/ctrl-p-and-ctrl-n-behaving-unexpectedly-under-docker

#### `docker exec -it some-container bash` results in `stty -a` with 0 cols and 0 rows

Upgrade docker-ce to 18.09.

## Mirror sites

#### For images from docker.io

* docker.mirrors.ustc.edu.cn
* hub-mirror.c.163.com
* `<ali-allocated-prefix>.mirror.aliyuncs.com`

```
# Example: docker pull mysql:5.0.0
#
# Using a mirror like:
docker pull docker.mirrors.ustc.edu.cn/library/mysql:5.0.0
docker pull dockerhub.azk8s.cn/library/mysql:5.0.0
docker pull hub-mirror.c.163.com/library/mysql:5.0.0

# Example: docker pull foo/bar:v1.0.0
#
# Using a mirror like:
docker pull docker.mirrors.ustc.edu.cn/foo/bar:v1.0.0
docker pull dockerhub.azk8s.cn/foo/bar:v1.0.0
```

#### For images from gcr.io

```
# Example: docker pull gcr.io/foo/bar:v1.0.0
#
# Using a mirror like:
docker pull gcr.mirrors.ustc.edu.cn/foo/bar:v1.0.0
docker pull gcr.azk8s.cn/foo/bar:v1.0.0
```

#### For images from k8s.gcr.io

```
# Example: docker pull k8s.gcr.io/foo:v1.0.0
#
# Using a mirror like:
docker pull gcr.mirrors.ustc.edu.cn/google-containers/foo:v1.0.0
docker pull gcr.azk8s.cn/google-containers/foo:v1.0.0
```

#### For images from quay.io

```
# Example: docker pull quay.io/coreos/etcd:v1.0.0
#
# Using a mirror like:
docker pull quay.mirrors.ustc.edu.cn/coreos/etcd:v1.0.0
docker pull quay.azk8s.cn/coreos/etcd:v1.0.0
```

## Access host port from container

Method 1:

For non-swarm mode, you can use host network mode.

Method 2:

You can access the host port from container by using the host IP.

## Dockerfile

### CMD

```
# This won't work
CMD ["sh", "-c", "ant", "-Djmeter.home=$JMETER_HOME/"]

# This works
CMD ["sh", "-c", "ant -Djmeter.home=$JMETER_HOME/"]
```

https://stackoverflow.com/questions/40454470/how-can-i-use-a-variable-inside-a-dockerfile-cmd

Also see https://hub.docker.com/r/curlimages/curl

### COPY

```
COPY hom* /mydir/
```

Ref: https://docs.docker.com/engine/reference/builder/#copy
