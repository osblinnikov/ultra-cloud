import yaml
import re
import os
from config import PROJECTS_ROOT_PATH

def readyaml(filename):
    file_to_read = os.path.join(filename)
    read_data = None
    try:
        with open (file_to_read, "r") as infile:
            pat=re.compile(r'/\*.*?\*/',re.DOTALL|re.M)
            read_data = yaml.load(re.sub(pat, '', infile.read()))
            infile.close()
    except:
        # print json_file_to_read+" invalid"
        try:
            infile.close()
        except:
            return read_data
    return read_data

def filterTypes_java(t):
    serializableType = False
    isObject = True
    isArray = False
    if len(t)>2 and t[-2:] == '[]':
        isArray = True
        t = t[:-2]
    if t in ["string","String"]:
        t = "String"
        serializableType = True
    if t in ["byte"]:
        t = "byte" if isArray else "byte"
        isObject = False
        serializableType = True
    if t in ["char"]:
        t = "char" if isArray else "char"
        isObject = False
        serializableType = True
    if t in ["int"]:
        t = "int" if isArray else "int"
        isObject = False
        serializableType = True
    if t in ["unsigned","long"]:
        t = "long" if isArray else "long"
        isObject = False
        serializableType = True
    if t in ["boolean"]:
        t = "boolean" if isArray else "boolean"
        isObject = False
        serializableType = True
    if t in ["double"]:
        t = "double" if isArray else "double"
        isObject = False
        serializableType = True
    if t in ["float"]:
        t = "float" if isArray else "float"
        isObject = False
        serializableType = True
    if t in ["Object"]:
        t = "Object"
    if isArray:
        t += "[]"
        isObject = True
    return t, isObject, isArray, serializableType

def filterTypes_c(t):
    serializableType = False
    isObject = True
    isArray = False
    if len(t)>2 and t[-2:] == '[]':
        isArray = True
        t = t[:-2]
    if t in ["string","char*"]:
        t = "char*"
        serializableType = True
    if t in ["char"]:
        t = "char"
        isObject = False
        serializableType = True
    if t in ["int"]:
        t = "int32_t"
        isObject = False
        serializableType = True
    if t in ["unsigned"]:
        t = "uint32_t"
        isObject = False
        serializableType = True
    if t  in ["long"]:
        t = "int64_t"
        isObject = False
        serializableType = True
    if t in ["boolean"]:
        t = "BOOL" if isArray else "BOOL"
        isObject = False
        serializableType = True
    if t in ["double"]:
        t = "double"
        isObject = False
        serializableType = True
    if t in ["float"]:
        t = "float"
        isObject = False
        serializableType = True
    if t in ["Object"]:
        t = "void*"
    if isArray:
        t = "arrayObject"
        isObject = True
    return t, isObject, isArray, serializableType


def getClassName(path):
    fullNameList = path.split('.')
    return fullNameList[-1]

def getCompany(path):
    fullNameList = path.split('.')
    return fullNameList[1]

def getCompanyDomain(path):
    fullNameList = path.split('.')
    return fullNameList[1]+'.'+fullNameList[0]

def getDomainName(path):
    fullNameList = path.split('.')
    del fullNameList[-1]
    return '.'.join(fullNameList)

def getDomainPath(path):
    fullNameList = path.split('.')
    to_delete = [0,1]
    for offset, index in enumerate(to_delete):
        index -= offset
        del fullNameList[index]
    return getCompanyDomain(path)+'/'+('/'.join(fullNameList))

def getFullName_(path):
    return '_'.join(path.split('.'))

def getRootPath(path):
    countstepsup = len(path.split('.')) -2
    if countstepsup < 0:
        countstepsup = 0
    countstepsup += 2

    rd = []
    for v in range(0, countstepsup):
        rd.append("..")
    rd = os.path.join(*rd)
    return rd
