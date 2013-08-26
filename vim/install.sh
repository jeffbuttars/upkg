#!/bin/bash

if [[ -z $PKGS_DIR ]]; then
    PKGS_DIR="$HOME/pkgs"
fi
.  "$PKGS_DIR/pkgs_utils.sh"

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

repo='git@github.com:jeffbuttars/Viming-With-Buttars.git'
clone_update  $repo vim

repo2='git@jeffbuttars.com:users/jeff/vimingwithbuttars'
cd vim
rurl_exists=0
for url in $(git remote -v | awk '{print $2}')
do
    if [ "$url" = "$repo2" ]
    then
        echo "repo2 exists, not adding it."
        rurl_exists=1
        break
    fi
done

if [ "$rurl_exists" = "0" ]; then
    echo "Adding repo url: $repo2"
    git remote set-url --add origin $repo2
    git pull origin master
    git remote -v
fi

mv -f ~/.vimrc ~/.vimrc.bak
echo "set runtimepath=$THIS_DIR/vim,\$VIMRUNTIME" > ~/.vimrc
echo "source $THIS_DIR/vim/.vimrc" >> ~/.vimrc
vim +'BundleInstall!' +':q'

# Build YouCompleteMe
if [[ -d "~/.vim/bundle/YouCompleteMe" ]]; then
    cd "~/.vim/bundle/YouCompleteMe"
    ./install.sh --clang-completer
fi

cd -
