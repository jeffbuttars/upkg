#!/bin/bash

. /home/jeff/pkgs/go/.pkgs.sh
gd='https://go.googlecode.com/files/go1.1.linux-amd64.tar.gz'

curl "$gd" > /tmp/godown.tar.gz
cd $GOPATH;
tar xvf /tmp/godown.tar.gz
