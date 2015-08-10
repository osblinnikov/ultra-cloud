#! /usr/bin/env python
import sys
import os
from os.path import dirname

sys.path.append(os.path.join(dirname(__file__),'github.com','osblinnikov'))

from gernet.gernet import Gernet
from snocs.snocs import Snocs

def printHelp():
    print " **********************"
    print "  Ultra-Cloud utility"
    print "  Generate, compile and distribute actors in the cluster"
    print "  Usage: ucl [options]"
    print "  options:"
    print "    gernet"
    print "    snocs"
    print " **********************"

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        printHelp()
        exit()
    if sys.argv[1] == 'gernet':
        Gernet(sys.argv[1:])
    elif sys.argv[1] == 'snocs':
        Snocs(sys.argv[1:])
    else:
        print "Please, specify correct option, see help: `ucl`"
