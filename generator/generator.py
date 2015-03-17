#! /usr/bin/env python
import sys
import os

from src.config  import PROJECTS_ROOT_PATH
from src.builder import runGenerator


def printHelp():
    print "**********************"
    print "Ultra-Cloud Generator is a little wrapper on Cogapp (http://nedbatchelder.com/code/cog) which enables you to generate full implementations of the embedded and distributed topologies of actors"
    print "Usage: ucl gen [TopologyFilePath] [options]"
    print "Examples:"
    print "  ucl gen .."
    print "  ucl gen icanchangethisdomain/SomeProjectName"
    print "TopologyFilePath can be absolute, relative to current path, or "
    print "relative to projects root path e.g.:"
    print "  ucl gen github.com\\osblinnikov\\generator\\example"
    print ""
    print "Available options:"
    print "  -c        # execute cleaning only for chosen Topology"
    print ""
    print "Other options can be Cog specific."
    print "  If you want to change default path to the Projects directory please see the"
    print "  config.py file and PROJECTS_ROOT_PATH variable"


def Generator(argv):
    TopologyDirs = []
    firstRealArgI = 1
    #try to find the TopologyDirs right here
    if len(argv) > firstRealArgI:
        pPr = None
        #try to find the TopologyDirs in the specified absolute path
        if os.path.exists(os.path.join(argv[firstRealArgI],"ucl.yaml")):
            TopologyDirs.append(os.path.join(argv[firstRealArgI]))
        #try to find the TopologyDirs in the specified relative to current path
        elif os.path.exists(os.path.join(os.getcwd(),argv[firstRealArgI],"ucl.yaml")):
            TopologyDirs.append(os.path.join(os.getcwd(),argv[firstRealArgI]))
        #try to find the TopologyDirs in the specified path from projects src root
        elif os.path.exists(os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI],"ucl.yaml")):
            TopologyDirs.append(os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI]))
        elif argv[firstRealArgI] == "." or os.path.exists(os.path.join(os.getcwd(),argv[firstRealArgI])):
            pPr = os.path.join(os.getcwd(),argv[firstRealArgI])
        elif os.path.exists(os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI])):
            pPr = os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI])
        elif os.path.exists(argv[firstRealArgI]):
            pPr = argv[firstRealArgI]
        if pPr != None:
            for root, dirs, files in os.walk(pPr):
                if os.path.exists(os.path.join(pPr,root,"ucl.yaml")):
                    TopologyDirs.append(os.path.join(pPr,root))

    if len(TopologyDirs) == 0 and os.path.exists(os.path.join(os.getcwd(),"ucl.yaml")):
        firstRealArgI = 0
        TopologyDirs.append(os.getcwd())
    elif len(TopologyDirs) == 0:
        print "**********************"
        print "No "+os.path.join(os.getcwd(),"ucl.yaml")
        if len(argv) > firstRealArgI:
            print "No "+os.path.join(argv[firstRealArgI],"ucl.yaml")
            print "No "+os.path.join(os.getcwd(),argv[firstRealArgI],"ucl.yaml")
            print "No "+os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI],"ucl.yaml")
        print "NO ucl.yaml files found"
        printHelp()
        exit()

    for d in TopologyDirs:
        try:
            runGenerator(firstRealArgI, argv, d)
        except:
            print "-------------"
            print "Exception in: "+d
            print "Unexpected error:", sys.exc_info()[0]
            raise

if __name__ == "__main__":
    Generator(sys.argv)
