#!/bin/bash

pkgs=$(ls -1 "$HOME/pkgs/")

for pkg in "$pkgs" ; do
    if [[ -f "$HOME/pkgs/$pkg/.pkg.sh" ]]; then
        . "$HOME/pkgs/$pkg/.pkg.sh" 
    fi
done
