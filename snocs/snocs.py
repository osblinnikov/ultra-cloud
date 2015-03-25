#! /usr/bin/env python
import os.path
import sys
import os
import imp
from builder import PROJECTS_ROOT_PATH
from builder import printHelp

def main(argv):
    SNocscript = None
    firstRealArgI = 1
    #in case we don't have any arguments
    if len(argv) <= firstRealArgI:
        #try to find the SNocscript right here
        if os.path.exists(os.path.join(os.getcwd(),"SNocscript.py")):
            firstRealArgI = firstRealArgI - 1
            SNocscript = os.path.join(os.getcwd(),"SNocscript.py")
        else:
            print "No SNocscript files found"
            printHelp()
            exit()
    else:
        #try to find the SNocscript in the specified relative to current path
        if os.path.exists(os.path.join(os.getcwd(),argv[firstRealArgI],"SNocscript.py")):
            SNocscript = os.path.join(os.getcwd(),argv[firstRealArgI],"SNocscript.py")
        #try to find the SNocscript in the specified absolute path
        elif os.path.exists(os.path.join(argv[firstRealArgI],"SNocscript.py")):
            SNocscript = os.path.join(argv[firstRealArgI],"SNocscript.py")            
        #try to find the SNocscript in the specified path from projects src root
        elif os.path.exists(os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI],"SNocscript.py")):
            SNocscript = os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI],"SNocscript.py")
        #try to find the SNocscript right here
        elif os.path.exists(os.path.join(os.getcwd(),"SNocscript.py")):
            firstRealArgI = firstRealArgI - 1
            SNocscript = os.path.join(os.getcwd(),"SNocscript.py")
        else:
            print "No "+os.path.join(os.getcwd(),"SNocscript.py")
            print "No "+os.path.join(argv[firstRealArgI],"SNocscript.py")
            print "No "+os.path.join(os.getcwd(),argv[firstRealArgI],"SNocscript.py")
            print "No "+os.path.join(PROJECTS_ROOT_PATH,'src',argv[firstRealArgI],"SNocscript.py")
            print "NO SNocscript files found"
            printHelp()
            exit()
        
    OTHER_ARGUMENTS = ""
    ONLY_PROJECT_CLEANING_STAGE = 0
    CLEANING_STAGE = 0
    if len(argv) > firstRealArgI + 1:
        for i in range(firstRealArgI+1, len(argv)):
            if argv[i] == '-h':
                printHelp()
                exit()
            if argv[i] == '-r':
                os.system("python "+SNocscript+" "+os.path.join(PROJECTS_ROOT_PATH,'src'))
                #imp.load_source('SNocscript',os.path.dirname(SNocscript))
                exit()
            if argv[i] == '-c':
                print "ONLY CURRENT PROJECT WILL BE CLEARED"
                ONLY_PROJECT_CLEANING_STAGE = 1
                CLEANING_STAGE = 1
            if argv[i] == '-call':
                print "ALL DEPENDENCIES WILL BE CLEARED"
                OTHER_ARGUMENTS+=" -c"
                CLEANING_STAGE = 1
            else:
                #FOR ALL EXCEPT -call
                OTHER_ARGUMENTS+=" "+argv[i]
        #end for arguments
        
    if ONLY_PROJECT_CLEANING_STAGE == 1:
        OTHER_ARGUMENTS+=" cleaning_one=1"
    if CLEANING_STAGE == 1:
        OTHER_ARGUMENTS+=" cleaning_all=1"
    os.system("scons -f "+os.path.abspath(os.path.dirname(__file__))+"/SNocstruct snocscript="+SNocscript+OTHER_ARGUMENTS)


if __name__ == '__main__':
    main(sys.argv)