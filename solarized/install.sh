#!/bin/bash

source  ~/pkgs/pkgs_utils.sh

# for KDE stuff
repo='git://github.com/hayalci/kde-colors-solarized.git'
clone_update  $repo
sdir=$(repo_name $repo) 

cd $sdir 
sh ./install.sh
cd -

cp xresources ~/.Xresources
xrdb -merge ~/.Xresources

# insdir="$HOME/.kde4/share/apps/konsole"

# # For just konsole
# repo='git://github.com/phiggins/konsole-colors-solarized.git'
# clone_update  $repo

# mkdir -p $insdir

# sdir=$(repo_name $repo) 

# for theme in $PWD/$sdir/*.colorscheme ; do
#     ln -nsfv "$theme" $insdir/
# done

# ls -l $insdir

