

#ifndef com_github_osblinnikov_ultra_cloud_generator_ExampleType_H
#define com_github_osblinnikov_ultra_cloud_generator_ExampleType_H

/*[[[cog
import cogging as c
c.tpl(cog,templateFile,c.a(prefix=configFile))
]]]*/


#undef com_github_osblinnikov_ultra_cloud_generator_ExampleType_EXPORT_API
#if defined WIN32 && !defined __MINGW32__ && !defined(CYGWIN) && !defined(COM_GITHUB_OSBLINNIKOV_ULTRA_CLOUD_GENERATOR_EXAMPLETYPE_STATIC)
  #ifdef com_github_osblinnikov_ultra_cloud_generator_ExampleType_EXPORT
    #define com_github_osblinnikov_ultra_cloud_generator_ExampleType_EXPORT_API __declspec(dllexport)
  #else
    #define com_github_osblinnikov_ultra_cloud_generator_ExampleType_EXPORT_API __declspec(dllimport)
  #endif
#else
  #define com_github_osblinnikov_ultra_cloud_generator_ExampleType_EXPORT_API extern
#endif

struct com_github_osblinnikov_ultra_cloud_generator_ExampleType;

com_github_osblinnikov_ultra_cloud_generator_ExampleType_EXPORT_API
void com_github_osblinnikov_ultra_cloud_generator_ExampleType_initialize(struct com_github_osblinnikov_ultra_cloud_generator_ExampleType *that);

com_github_osblinnikov_ultra_cloud_generator_ExampleType_EXPORT_API
void com_github_osblinnikov_ultra_cloud_generator_ExampleType_deinitialize(struct com_github_osblinnikov_ultra_cloud_generator_ExampleType *that);

/*declaration of macros, can be overriden*/
#undef com_github_osblinnikov_ultra_cloud_generator_ExampleType_onCreateMacro
#define com_github_osblinnikov_ultra_cloud_generator_ExampleType_onCreateMacro(_NAME_) /**/



typedef struct com_github_osblinnikov_ultra_cloud_generator_ExampleType{
  
  
  /*void (*run)(void *that);*/
/*[[[end]]] (checksum: f85ace07fc2b5f65e98041c4ac70d3da)*/

}com_github_osblinnikov_ultra_cloud_generator_ExampleType;

#undef com_github_osblinnikov_ultra_cloud_generator_ExampleType_onCreateMacro
#define com_github_osblinnikov_ultra_cloud_generator_ExampleType_onCreateMacro(_NAME_) /**/

#endif /* com_github_osblinnikov_ultra_cloud_generator_ExampleType_H */