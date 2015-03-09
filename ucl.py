#! /usr/bin/env python
import sys
import os

from generator.generator import Generator

def printHelp():
    print "**********************"
    print "Ultra-Cloud utility"
    print "which enables you to generate, compile and distribute actors in the cluster"
    print "Usage: ucl [options]"
    print "options:"
    print "  gen"
    print "**********************"

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        printHelp()
        exit()
    if sys.argv[1] == 'gen':
        Generator(sys.argv[1:])
