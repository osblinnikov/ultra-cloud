<%import parsing
p = reload(parsing)
p.parsing(a)%>
#include "../include/${a.className}.h"

void ${a.fullName_}_onKernels(struct ${a.fullName_} *that);
void ${a.fullName_}_onCreate(${a.fullName_} *that);
void ${a.fullName_}_onDestroy(${a.fullName_} *that);
void ${a.fullName_}_initialize(${a.fullName_} *that){
  ${a.fullName_}_onCreate(that);
}

void ${a.fullName_}_deinitialize(struct ${a.fullName_} *that){
  ${a.fullName_}_onDestroy(that);
}