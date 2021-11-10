#!/bin/bash

function start() {
    if [ -z "$1" ]
    then
        echo "You need to define a tag for you deplyoment: ./icekube_dev.sh start tag_name"
        exit 1
    fi

    kubectl config use-context icekube
    kubectl config set-context --current --namespace=ltu-default

    SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    cd $SCRIPT_DIR

    helm install \
    --debug \
    ml-dev-utils-$1 ./ -f ./values_icekube.yaml

    helm list
}

function stop() {
    if [ -z "$1" ]
    then
        echo "You need to define a tag for you deplyoment: ./icekube_dev.sh stop tag_name"
        exit 1
    fi

    kubectl config use-context icekube
    kubectl config set-context --current --namespace=ltu-default

    helm uninstall \
    ml-dev-utils-$1
    
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
            start $2 ;;
        stop)
            stop $2 ;;
        build)
            build ;;
        *)
            echo $"Usage: $0 {start|stop|build}"
            exit 1
esac
