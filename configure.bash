#!/bin/bash

# ------------------
# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`

cd $SCRIPTPATH

cp actor-framework-snocs/libcaf_core_SNocscript.py actor-framework/libcaf_core/SNocscript.py 
cp actor-framework-snocs/libcaf_core_ucl.yaml actor-framework/libcaf_core/ucl.yaml

cp actor-framework-snocs/libcaf_io_SNocscript.py actor-framework/libcaf_io/SNocscript.py
cp actor-framework-snocs/libcaf_io_ucl.yaml actor-framework/libcaf_io/ucl.yaml


./ucl snocs compiler=gpp_cpp11 "$1"

cd -