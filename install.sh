#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for pkg in $(ls -1) ; do
    if [[ -d "$pkg" ]]; then
        if [[ -f "$pkg/install.sh" ]]; then
            echo "Running install on $pkg"
            cd $pkg
            make install
            cd -
        fi
    fi
done
