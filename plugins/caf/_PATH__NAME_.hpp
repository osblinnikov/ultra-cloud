<%
import sys
sys.path.insert(0, a.parserPath)

import parsing
p = reload(parsing)
p.parsing(a)

%>

// ${a.read_data["name"]}.hpp

#ifndef ${a.fullNameU_}_H
#define ${a.fullNameU_}_H

#include <string>

${a.namespaceStart}

#undef ${a.fullNameU_}_EXPORT_API
#if defined WIN32 && !defined __MINGW32__ && !defined(CYGWIN) && !defined(${(a.fullNameU_+"_static").upper()})
  #ifdef ${a.fullNameU_}_EXPORT
    #define ${a.fullNameU_}_EXPORT_API __declspec(dllexport)
  #else
    #define ${a.fullNameU_}_EXPORT_API __declspec(dllimport)
  #endif
#else
  #define ${a.fullNameU_}_EXPORT_API 
//extern
#endif


/**
 * This class is only being used as style guide example.
 */

class ${a.fullNameU_}_EXPORT_API ${a.className}{
 public:
  /**
   * Brief description. More description. Note that CAF uses the
   * "JavaDoc-style" autobrief option, i.e., everything up until the
   * first dot is the brief description.
   */  
  ${a.className}();
  
  /**
   * Destructs `${a.className}`. Please use Markdown in comments.
   */  
  ~${a.className}();

};

${a.namespaceEnd}

#endif // ${a.fullNameU_}_H