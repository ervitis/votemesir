#!/usr/bin/env bash

function fixError {
    sudo cp /opt/google-cloud-sdk/platform/google_appengine/lib/fancy_urllib/fancy_urllib/__init__.py /opt/google-cloud-sdk/platform/google_appengine/lib/fancy_urllib/__init__.py
}

function main {
    fixError
}

main