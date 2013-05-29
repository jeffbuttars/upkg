#!/bin/bash

# exit 0

. .pkg.sh
gd='https://go.googlecode.com/files/go1.1.linux-amd64.tar.gz'
tball='godown.tar.gz'

if [[ -f "$tball" ]]; then
    echo "Using exising go tarball"
else
    curl "$gd" > $tball
fi

# cd $GOPATH;
tar xvf $tball
