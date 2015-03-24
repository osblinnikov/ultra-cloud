<%import parsing
from helpers import getFullName_
p = reload(parsing)
p.parsing(a)%>
  %for v in a.read_data["actors"]:
  AddDependency(args,'${getFullName_(v["name"])}',join(args['PROJECTS_ROOT_PATH'],'src/${v["name"]}'))
  %endfor
  %for v in a.read_data["depends"]:
  AddDependency(args,'${getFullName_(v)}',join(args['PROJECTS_ROOT_PATH'],'src/${v}'))
  %endfor