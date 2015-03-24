<%
import sys
sys.path.insert(0, a.parserPath)

import parsing
p = reload(parsing)
p.parsing(a)

%>
// src/${a.className}.cpp

#include "../${p.getHeaderPath(a)}.hpp"

${a.namespaceStart}

${a.className}::${a.className}(){

}

${a.className}::~${a.className}(){
  
}

${a.namespaceEnd}
