#!/usr/bin/env bash

function fixError {
    cp ${GOOGLEAPPENGINE_PATH}/lib/fancy_urllib/fancy_urllib/__init__.py ${GOOGLEAPPENGINE_PATH}/lib/fancy_urllib/__init__.py
}

function main {
    fixError
}

main