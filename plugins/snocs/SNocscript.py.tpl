<%import parsing
import helpers
p = reload(parsing)
p.parsing(a)%>
  %for v in a.read_data["actors"]+a.read_data["depends"]:
  AddDependency(args,'${p.fullName_}',join(args['PROJECTS_ROOT_PATH'],'src/${v["name"]}'))
  %endfor