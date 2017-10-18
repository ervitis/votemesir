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

function createDirectoryLibrary {
    mkdir -p ${HOME}/${DIRECTORYLIBRARY_NAME}
}

function downloadSDK {
    createDirectoryLibrary
    curl -o ${HOME}/${DIRECTORYLIBRARY_NAME}/${GOOGLESDK_NAME}_${GOOGLESDK_VERSION}.tar.gz ${GOOGLESDKD_URL}/${GOOGLESDK_NAME}-${GOOGLESDK_VERSION}-linux-x86_64.tar.gz
}

function downloadAppengine {
    createDirectoryLibrary
    curl -o ${HOME}/${DIRECTORYLIBRARY_NAME}/${GOOGLEAPPENGINE_NAME}_${GOOGLEAPPENGINE_VERSION}.zip ${GOOGLEAPPENGINE_URL}/${GOOGLEAPPENGINE_NAME}_${GOOGLEAPPENGINE_VERSION}.zip
}

function installAppengine {
    cd ${HOME}/${DIRECTORYLIBRARY_NAME} && unzip -q ${GOOGLEAPPENGINE_NAME}_${GOOGLEAPPENGINE_VERSION}.zip
}

function installSDK {
    cd ${HOME}/${DIRECTORYLIBRARY_NAME} && tar xf ${GOOGLESDK_NAME}-${GOOGLESDK_VERSION}-linux-x86_64.tar.gz && ./${GOOGLESDK_NAME}-${GOOGLESDK_VERSION}/install.sh
}

function goToCircleHome {
    cd ${HOME}/${CIRCLE_PROJECT_REPONAME}
}

function setupEnvironment {
    echo ${CLIENT_SECRET} | base64 --decode > ${HOME}/${clientSecretsFile}
    gcloud auth activate-service-account --key-file ${HOME}/${clientSecretsFile}
    gcloud config set project ${HOST_APPENGINE}
}

function main {
    setVariables
    downloadSDK
    installSDK
    downloadAppengine
    installAppengine

    goToCircleHome
}

main
