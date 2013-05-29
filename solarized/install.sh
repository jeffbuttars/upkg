#!/bin/bash

if [[ -z $PKGS_DIR ]]; then
    PKGS_DIR="~/pkgs"
fi
.  "$PKGS_DIR/pkgs_utils.sh"

# for KDE stuff
repo='git://github.com/hayalci/kde-colors-solarized.git'
clone_update  $repo
sdir=$(repo_name $repo) 

cd $sdir 
sh ./install.sh
cd -

