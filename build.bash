#!/bin/bash

# ------------------
# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`

cd $SCRIPTPATH


#cp actor-framework-snocs/libcaf_core_ucl.yaml actor-framework/libcaf_core/ucl.yaml
#cp actor-framework-snocs/libcaf_io_ucl.yaml actor-framework/libcaf_io/ucl.yaml
#cp actor-framework-snocs/libcaf_opencl_ucl.yaml actor-framework/libcaf_opencl/ucl.yaml
#cp actor-framework-snocs/libcaf_riac_ucl.yaml actor-framework/libcaf_riac/ucl.yaml
#cp actor-framework-snocs/nexus_ucl.yaml actor-framework/nexus/ucl.yaml
#cp actor-framework-snocs/cash_ucl.yaml actor-framework/cash/ucl.yaml

cp actor-framework-snocs/libcaf_core_SNocscript.py actor-framework/libcaf_core/SNocscript.py 
cp actor-framework-snocs/libcaf_io_SNocscript.py actor-framework/libcaf_io/SNocscript.py
cp actor-framework-snocs/libcaf_opencl_SNocscript.py actor-framework/libcaf_opencl/SNocscript.py
cp actor-framework-snocs/libcaf_riac_SNocscript.py actor-framework/libcaf_riac/SNocscript.py
cp actor-framework-snocs/nexus_SNocscript.py actor-framework/nexus/SNocscript.py
cp actor-framework-snocs/cash_SNocscript.py actor-framework/cash/SNocscript.py
cp actor-framework-snocs/unit_testing_SNocscript.py actor-framework/unit_testing/SNocscript.py

./ucl snocs ${*:1} compiler=gpp_cpp11

cd -