<%
import sys
sys.path.insert(0, a.parserPath)

import parsing
p = reload(parsing)
p.parsing(a)

%>/*[[[cog
import cogging as c
c.tpl(cog,templateFile,c.a(prefix=configFile))
]]]*/
/*[[[end]]]*/

void ${a.fullName_}_onCreate(${a.fullName_} *that){
  
  return;
}

void ${a.fullName_}_onDestroy(${a.fullName_} *that){
  
  return;
}


void ${a.fullName_}_onKernels(${a.fullName_} *that){
  
  return;
}