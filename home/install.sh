#!/bin/bash

if [[ -z $PKGS_DIR ]]; then
    PKGS_DIR="$HOME/pkgs"
fi
.  "$PKGS_DIR/pkgs_utils.sh"

repo='git@jeffbuttars.com:users/jeff/jhome'
clone_update  $repo

# For each file in this repo, hard link it
# into the home dir. Backing up any existing, non linked files.

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BACKUPDIR="$THIS_DIR/.home_backup"

# Ignore the install file from the file list

mkdir -p $BACKUPDIR

# for each file, if it's a hard link to our install here, leave it alone.
# If not, back it up and overrite it with a link.

cd $(repo_name $repo)

# flist=$(find . -type f -not -name "install.sh" ! -wholename '*.git/*' ! -name '.git' ! -wholename "*$BACKUPDIR/*" ! -name "$BACKUPDIR")
flist=$(find . -type f ! -wholename '*.git/*' ! -name '.git')

echo "$flist" | while read fname; do

    echo "Processing '$fname'"
    if [[ "$fname" -ef "$HOME/$fname" ]]; then
        echo "$fname <- linked to -> $HOME/$fname"
        continue
    else
        echo "$fname <- NOT linked to -> $HOME/$fname"

        if [[ -f "$HOME/$fname" ]]; then
            echo "Backing up $HOME/$fname"
            dname=$(dirname "$fname")
            mkdir -p "$BACKUPDIR/$dname"
            fmode=$(stat -c "%a" "$HOME/$fname")
            install -v --backup=existing -C --mode="$fmode" "$HOME/$fname" "$BACKUPDIR/$dname"
        else
            echo "$HOME/$fname doesn't exist, not backing up."
            continue
        fi

        mkdir -p "$HOME/$dname"
        ln -vf "$fname" "$HOME/$fname"
    fi    
done

cd -
