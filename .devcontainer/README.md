# Development inside a Docker container with Visual Studio Code

This is the setup for the development with VSC and Docker. The complete environment is shared and setup by Docker containers. You are developing inside the containers.

## Prerequisites

- Github account
- Docker
- Kubernetes
- Helm
- VSC

All following commands are assuming that they are run from the .devcontainer folder.

## Create Docker image

```bash
# dev 
docker build --force-rm --tag ltuml/ml-dev:ml-dev-utils --file Dockerfile .
docker push ltuml/ml-dev:ml-dev-utils
```
