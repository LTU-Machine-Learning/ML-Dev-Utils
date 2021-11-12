#!/bin/bash

function start() {
    kubectl config use-context docker-desktop

    SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    cd $SCRIPT_DIR

    helm install \
    --debug \
    --set localVolumePath=$ML_DEV_UTILS_VOLUME_PATH \
    ml-dev-utils ./ -f ./values_local.yaml

    helm list
}

function stop() {
    kubectl config use-context docker-desktop

    helm uninstall \
    ml-dev-utils
    
    helm list
}

function build() {
    SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    cd $SCRIPT_DIR/../.devcontainer

    docker build --force-rm --tag ltuml/ml-dev:ml-dev-utils --file Dockerfile .
    docker push ltuml/ml-dev:ml-dev-utils
}

case "$1" in
        start)
            start ;;
        stop)
            stop ;;
        build)
            build ;;
        *)
            echo $"Usage: $0 {start|stop|build}"
            exit 1
esac
