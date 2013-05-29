#!/bin/zsh

if [[ -z $PKGS_DIR ]]
then
    export PKGS_DIR="$HOME/pkgs"
fi

cd "$PKGS_DIR"

for pkg in $(ls -1) ; do

    if [[ -d "$pkg" ]]
    then
        # echo $pkg
        # echo "$pkg/.pkg.zsh"

        if [[ -f "$pkg/.pkg.zsh" ]]; then
            cd $pkg
            # echo "$pkg/.pkg.zsh" 
            source ".pkg.zsh" 
            cd -
        elif [[ -f "$pkg/.pkg.sh" ]]; then
            cd $pkg
            # echo "$pkg/.pkg.sh" 
            source ".pkg.sh" 
            cd -
        fi
    fi
done

cd -
