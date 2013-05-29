#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export GOROOT="$THIS_DIR/go"
export PATH="$PATH:$GOROOT/bin"
