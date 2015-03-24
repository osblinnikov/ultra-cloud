<%
import sys
sys.path.insert(0, a.parserPath)

import parsing
p = reload(parsing)
p.parsing(a)

%>
// tests/${a.className}Test.cpp

#include "../${p.getHeaderPath(a)}.hpp"

int main(int argc, char* argv[]){

  return 0;
}