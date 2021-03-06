#!/usr/bin/env bash

function main {
    mkdir -p ./libs

    pip install -t libs -r requirements.txt; result=$?
    if [[ ${result} -ne 0 ]]; then
        echo "Error"
        exit 1
    fi

    touch ./libs/__init__.py
    pwd
    ls -l ${HOME}
    ls -l ${HOME}/${CIRCLE_PROJECT_REPONAME}/libs
    ls -l ${HOME}/${CIRCLE_PROJECT_REPONAME}
    ls -l ${HOME}/virtualenvs
}

main
