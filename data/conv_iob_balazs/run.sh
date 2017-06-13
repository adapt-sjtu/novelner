#!/bin/bash
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

scriptname='conv_iob_balazs.py'

realpath="`realpath $0`"
abspath="`dirname $realpath`"

# Colors: http://stackoverflow.com/a/5947802
LBLUE='\033[1;34m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "${LBLUE}"
echo "Runing $abspath/$scriptname $@ :"
printf "${NC}"
$abspath/$scriptname $@ 2>&1
if [ $? -eq 0 ]; then printf "${GREEN}Done!${NC}"; echo; fi
