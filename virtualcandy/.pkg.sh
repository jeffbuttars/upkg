#!/bin/bash

# THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [[ -z $PKGS_DIR ]]
then
    export PKGS_DIR="$HOME/pkgs"
fi

cd $PKGS_DIR/virtualcandy/virtualcandy
. virtualcandy.sh
cd -
