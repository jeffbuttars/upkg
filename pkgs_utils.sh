#!/bin/bash

repo_name()
{
    
    if [[ -z $1 ]]; then
        echo "repo_name no repo url given."
        echo "> repo_name <url_of_repo>"
        exit 1
    fi

    # Get the repo name/dirname
    rname=$(basename "$1")
    rname=${rname%.*}
    
    echo "$rname"
} #repo_name

clone()
{
    if [[ -z $1 ]]; then
        echo "clone no repo given."
        echo "> clone <url_of_repo>"
        exit 1
    fi

   # assume git for the moment 
   git clone $1
} #clone

clone_update()
{
    if [[ -z $1 ]]; then
        echo "clone_update no repo given."
        echo "> clone_update <name_of_repo>"
        exit 1
    fi

    rname=$(repo_name $1)
    if [[ ! -d "$rname" ]]; then
        git clone $1
    fi

    if [[ ! -d "$rname/.git" ]]; then
        echo "Expected directory $rname exists, but is not a git repo!!!"
        echo "Bailing out."
        exit 1
    fi

    cd "$rname";
    git fetch 
    git merge $(git rev-parse --abbrev-ref --symbolic-full-name @{u})
    cd -
} #clone_update
