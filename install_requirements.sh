#!/bin/bash

function main {
    mkdir -p libs 2>/dev/null

    pip install -t libs -r requirements.txt; result=$?
    if [[ ${result} -ne 0 ]]; then
        echo "Error"
        exit 1
    fi

    touch ./libs/__init__.py
}

main
