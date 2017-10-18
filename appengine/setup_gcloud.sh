#!/usr/bin/env bash

function setVariables {
    clientSecretsFile="client-secret.json"
    GOOGLESDK_VERSION="175.0.0"
    GOOGLESDK_NAME="google-cloud-sdk"
    GOOGLESDKD_URL="https://dl.google.com/dl/cloudsdk/channels/rapid/downloads"
    GOOGLEAPPENGINE_VERSION="1.9.61"
    GOOGLEAPPENGINE_NAME="google_appengine"
    GOOGLEAPPENGINE_URL="https://storage.googleapis.com/appengine-sdks/featured"
    DIRECTORYLIBRARY_NAME="sdk"
}

function printVariables {
    echo "clientSecretsFile="${clientSecretsFile}
    echo "GOOGLESDK_VERSION="${GOOGLESDK_VERSION}
    echo "GOOGLESDK_NAME="${GOOGLESDK_NAME}
    echo "GOOGLESDKD_URL="${GOOGLESDKD_URL}
    echo "GOOGLEAPPENGINE_VERSION="${GOOGLEAPPENGINE_VERSION}
    echo "GOOGLEAPPENGINE_NAME="${GOOGLEAPPENGINE_NAME}
    echo "GOOGLEAPPENGINE_URL="${GOOGLEAPPENGINE_URL}
    echo "DIRECTORYLIBRARY_NAME="${DIRECTORYLIBRARY_NAME}
}

function createDirectoryLibrary {
    mkdir -p ${HOME}/${DIRECTORYLIBRARY_NAME}
}

function downloadSDK {
    createDirectoryLibrary
    local downloadPath=${HOME}/${DIRECTORYLIBRARY_NAME}/${GOOGLESDK_NAME}-${GOOGLESDK_VERSION}.tar.gz
    local urlToDownload=${GOOGLESDKD_URL}/${GOOGLESDK_NAME}-${GOOGLESDK_VERSION}-linux-x86_64.tar.gz

    echo "downloadPath="${downloadPath}
    echo "urlToDownload="${urlToDownload}

    curl -o ${downloadPath} ${urlToDownload}
}

function downloadAppengine {
    createDirectoryLibrary
    local downloadPath=${HOME}/${DIRECTORYLIBRARY_NAME}/${GOOGLEAPPENGINE_NAME}_${GOOGLEAPPENGINE_VERSION}.zip
    local urlToDownload=${GOOGLEAPPENGINE_URL}/${GOOGLEAPPENGINE_NAME}_${GOOGLEAPPENGINE_VERSION}.zip

    echo "downloadPath="${downloadPath}
    echo "urlToDownload="${urlToDownload}

    curl -o ${downloadPath} ${urlToDownload}
}

function installAppengine {
    local directory=${HOME}/${DIRECTORYLIBRARY_NAME}

    echo "Now in "${directory}

    cd ${directory} && unzip -q ${GOOGLEAPPENGINE_NAME}_${GOOGLEAPPENGINE_VERSION}.zip
}

function installSDK {
    local directory=${HOME}/${DIRECTORYLIBRARY_NAME}

    echo "Now in "${directory}

    cd ${directory} && tar xf ${GOOGLESDK_NAME}-${GOOGLESDK_VERSION}-linux-x86_64.tar.gz && ./${GOOGLESDK_NAME}-${GOOGLESDK_VERSION}/install.sh
}

function goToCircleHome {
    echo "Going to circle home="${CIRCLE_PROJECT_REPONAME}

    cd ${HOME}/${CIRCLE_PROJECT_REPONAME}
}

function setupEnvironment {
    echo "SetupEnvironment"

    echo ${CLIENT_SECRET} | base64 --decode > ${HOME}/${clientSecretsFile}
    gcloud auth activate-service-account --key-file ${HOME}/${clientSecretsFile}
    gcloud config set project ${HOST_APPENGINE}
}

function main {
    setVariables
    printVariables
    
    downloadSDK
    installSDK
    downloadAppengine
    installAppengine

    goToCircleHome
}

main