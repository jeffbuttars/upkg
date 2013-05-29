#!/bin/bash

if [[ -z $PKGS_DIR ]]; then
    PKGS_DIR="$HOME/pkgs"
fi
.  "$PKGS_DIR/pkgs_utils.sh"

repo='https://github.com/rkitover/vimpager.git'
clone_update  $repo
sdir=$(repo_name $repo) 
cd $sdir
make
sudo make install
cd -
