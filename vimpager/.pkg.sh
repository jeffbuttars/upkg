#!/bin/bash

export VIMPAGER_RC=~/.vimpagerrc
if [[ -f  /usr/local/bin/vimpager ]]; then
	export PAGER=/usr/local/bin/vimpager
fi

