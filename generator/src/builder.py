# realpath() with make your script run, even if you syamlink it :)
#
# cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
# if cmd_folder not in sys.path:
# sys.path.insert(0, cmd_folder)
#
# use this if you want to include modules from a subforder
import inspect
import re
import subprocess
import sys
from config import PROJECTS_ROOT_PATH
from attrs import attrs
from helpers import *
import json, os

sysPathBcp = list(sys.path+[os.path.dirname(__file__)])

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from helpers import *
from cogapp import cogapp
import mako.template
import mako.lookup

join = os.path.join

def tpl(strfile, args):
    mylookup = mako.lookup.TemplateLookup(directories=[
        os.path.abspath(os.getcwd())
    ])
    tplFromFile = mako.template.Template(filename=strfile, lookup=mylookup, imports=['from attrs import attrs'])
    return tplFromFile.render(a=args)


def getArgs(firstRealArgI, argv):
    all_args = []
    compiling_arg = ['-U', '-c']  #-U means unix style line endings

    if len(argv) > firstRealArgI + 1:
        for i in range(firstRealArgI + 1, len(argv)):
            if argv[i] == '-c':
                compiling_arg = ['-x']
            # elif argv[i] == '-g':
            #     if i + 1 == len(argv) or argv[i + 1].startswith("-"):
            #         raise Exception("expected language type after -lang option")
            #     else:
            #         Types.append(argv[i + 1])
            #         i = i + 1
            elif i == 1: # argv[i - 1] == '-g' or
                continue
            else:
                all_args.append(argv[i])
    all_args += compiling_arg
    return all_args


def getFilteredSubFolders(folder, filters):
    res = []
    d = []
    for root, dirs, files in os.walk(folder):
        print dirs
        d = dirs
        break

    for i in d:
        if len(filters) == 0 or i in filters:
            res.append(i)
    return res

def getPath(pathSrc):
    # path = pathSrc.split('.')
    # if len(path) < 3:
    #     raise Exception("path: \""+pathSrc+"\" is not a full package name")
    # arr = [PROJECTS_ROOT_PATH, path[1] + "." + path[0]]
    # to_delete = [0, 1]
    # for offset, index in enumerate(to_delete):
    #     index -= offset
    #     del path[index]
    # return '/'.join(arr + path)
    return os.path.join(PROJECTS_ROOT_PATH, pathSrc)


def generateMissedFiles(topology_dir, generator_dir, classPath, extra_args):
    classPathList = splitClassPath(classPath)
    className = getClassName(classPath)
    fullName_ = getFullName_(classPath)
    json_file_to_read = join(topology_dir, "ucl.yaml")

    for root, dirs, files in os.walk(generator_dir):
        for fileName in files:
            fileP = os.path.join(root,fileName)
            if (len(fileName)>4 and fileName[-4:] == '.tpl') or not os.path.exists(fileP+".tpl"):
                continue

            relativeFilePath =  fileP[(len(generator_dir)+1):]\
                .replace("_NAME_", className) \
                .replace("_FULLNAME_", fullName_) \
                .replace("_FULLNAMEDIR_", os.path.join(*[fullName_, ""])) \
                .replace("_PATH_", os.path.join(*(classPathList+[""])))
            
            absDstFilePath = os.path.join(topology_dir, relativeFilePath) #os.path.split(generator_dir)[1], 

            if not os.path.exists(absDstFilePath):
                checkDir(absDstFilePath)

                #cleaning paths before copying template
                sys.path = list(sysPathBcp)

                f = open(absDstFilePath,'w')#output file
                f.write(tpl(
                    fileP,#input template
                    attrs(
                        prefix=json_file_to_read,#required for parser of json file
                        parserPath=generator_dir
                    )#args
                ))
                f.close()

            #cleaning paths before cogging template
            sys.path = list(sysPathBcp)
            args = extra_args+[
                '-I',
                os.path.abspath(os.path.dirname(__file__)),
                '-I',
                generator_dir,
                '-r',#replace in file
                "-D","configFile="+json_file_to_read, #specify config as global variable
                "-D","templateFile="+fileP+'.tpl', #specify config as global variable
                absDstFilePath
            ]
            # print args
            cogapp.Cog().main(["cogging"]+args)


def runGenerator(firstRealArgI, argv, topology_dir):
    FiltersOrig = []
    extra_args = getArgs(firstRealArgI, argv)
    read_data = readyaml(join(topology_dir,"ucl.yaml"))
    print read_data
    gens = read_data["gen"]
    for g in range(0, len(gens)):
        print(getPath(gens[g]))
        # Types = getFilteredSubFolders(getPath(gens[g]), FiltersOrig)
        # print Types
        # # if len(Types) == 0:
        #     # print ("No one generator was found")
        #     # return
        # for i in range(0, len(Types)):
        generateMissedFiles(
            topology_dir,
            getPath(gens[g]),
            read_data["name"],
            extra_args
        )


def checkDir(directory):
    fPath, fName = os.path.split(directory)
    if not os.path.exists(fPath):
        os.makedirs(fPath)
    return fPath
