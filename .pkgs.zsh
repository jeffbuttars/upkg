#!/bin/zsh

if [[ -z $PKGS_DIR ]]
then
    export PKGS_DIR="$HOME/pkgs"
fi

cd "$PKGS_DIR"

for pkg in $(ls -1) ; do

    # echo $(file $pkg)
    if [[ -d "$pkg" ]]
    then
        # echo "pkg?: $pkg"

        if [[ -f "$pkg/.pkg.zsh" ]]; then
            cd $pkg
            # echo "sourcing $pkg/.pkg.zsh" 
            source ".pkg.zsh" 
            cd -
        elif [[ -f "$pkg/.pkg.sh" ]]; then
            cd $pkg
            # echo "sourcing $pkg/.pkg.sh" 
            source ".pkg.sh" 
            cd -
        fi
    fi
done

cd -
