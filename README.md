## Overview

Entire project reference is [here](https://testdriven.io/blog/fastapi-docker-traefik/), and here is the [GitHub](https://github.com/testdrivenio/fastapi-docker-traefik/blob/master/docker-compose.yml) repo.

Here we are trying to cover Docker basic in a use case of setting up something, from pulling, run, exec and many others.

### Pull

Ref: [Docker Pull](https://docs.docker.com/engine/reference/commandline/pull/#options)

Generic usage would be:

`$ docker pull [image:tag]`

By default it will connect to the [Dockerhub](https://hub.docker.com/) registry. if we are gonna pull from, specific repo or registry, say `registry.doggonebead.xyz:5000` for image named `db:latest`, then it shall be:

`$ docker pull registry.doggonebad.xyz:5000/db:latest`, however we might need to perform [docker login](https://docs.docker.com/engine/reference/commandline/login/) first.

### Run 

Ref: [Docker Run](https://docs.docker.com/engine/reference/commandline/run/)

Run an image in a new container.

Typical usage:

`$ docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`

If you have a image from `alpine:latest` then to run it simply by:

`$ docker run -d -t --name alpinehome alpine:latest`

Here are each flags/options mean:

* `-d` or `--detach`: Run container in background and print container ID
* `-t` or `--tty`: Run container with connected stdout, hence if you want an `echo` command to be shown, this is needed.
* `--name`: To rename the container into something you prefer.

### Exec

Ref: [Docker Exec](https://docs.docker.com/engine/reference/commandline/exec/)

To run a command inside already running container.

Typical usage:

`$ docker exec [OPTIONS] CONTAINER [COMMAND] [ARG...]`

From [Run](Run) above, we can just run a command `sh` which means, to run shell inside the *alpinehome* container:

`$ docker exec -it alpinehome sh`.

```
yanua in ~ λ docker exec -it alpinehome sh
/ # whoami
root
/ # ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ #
```
Very neat!

### Stop

Ref: [Docker Stop](https://docs.docker.com/engine/reference/commandline/stop/)

Stop one or more running containers

Typical usage:

`$ docker stop [OPTIONS] CONTAINER [CONTAINER..]`

The main process inside the CONTAINER will receive `SIGTERM`,a nd after a grace period, `SIGKILL`. The first signal can be changed with the `STOPSIGNAL` instruction in the container's Dockerfile, or the `--stop-signal` option to `docker run`.

### Volume

Ref: [Docker Volumes](https://docs.docker.com/storage/volumes/)

*Volumes* are preferred mechanism for persistent data storage used by all containers to dump files.

## Dockerfile

### Workdir

`WORKDIR` by default is always created, but if explicitly specified by users, will be used subsequently.

For this example **Dockerfile**:

``` dockerfile
# Python base image
FROM python:3.9.4-slim

# set the work directory
WORKDIR /app

# copy pip-dependencies to WORKDIr
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
```

`WORKDIR` is specified into `/app` directory inside the container. Hence, all dockerfile operations following this command, will use the `WORKDIR` as relative path :).

