#!/bin/bash

if [[ -z $PKGS_DIR ]]
then
    export PKGS_DIR="$HOME/pkgs"
fi

orig_dir="$PWD"
cd "$PKGS_DIR"

for pkg in $(ls -1) ; do

    if [[ -d "$pkg" ]]
    then
        if [[ -f "$pkg/.pkg.sh" ]]; then
            cd $pkg
            . ".pkg.sh" 
            cd -
        fi
    fi
done

cd $orig_dir
