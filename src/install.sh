#!/bin/bash

# install golang 1.20.1
wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz

#install scov
go install gitlab.com/stone.code/scov@latest

# download go sources
mkdir -p ~/go/src/go
git clone --depth 1 --branch go1.20.1 https://github.com/golang/go.git ~/go/src/go
rm ~/go/src/go/src/html/template/*_test.go
rm ~/go/src/go/src/text/template/*_test.go

# install tribble
mkdir -p /tribble
cd tribble
git clone https://github.com/havrikov/tribble.git .
./gradlew build
mv tribble-tool/build/libs/tribble-1.0.0.jar tribble.jar
cd

