#!/bin/zsh

if [[ -z $PKGS_DIR ]]
    export PKGS_DIR="$HOME/pkgs"
then
    
fi
cd "$PKGS_DIR"

for pkg in $(ls -1) ; do

    if [[ -d "$pkg" ]]
    then
        # echo $pkg
        # echo "$pkg/.pkg.zsh"

        if [[ -f "$HOME/pkgs/$pkg/.pkg.zsh" ]]; then
            # echo "$HOME/pkgs/$pkg/.pkg.zsh" 
            source "$HOME/pkgs/$pkg/.pkg.zsh" 
        elif [[ -f "$HOME/pkgs/$pkg/.pkg.sh" ]]; then
            # echo "$HOME/pkgs/$pkg/.pkg.sh" 
            source "$HOME/pkgs/$pkg/.pkg.sh" 
        fi
    fi
done

cd -
