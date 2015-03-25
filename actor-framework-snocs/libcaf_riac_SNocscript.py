
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
    '''[[[cog
    import cogging as c
    c.tpl(cog,templateFile,c.a(prefix=configFile))
    ]]]'''

    AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_core',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_core'))
    AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_io',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_io'))
    '''[[[end]]] (checksum: 53cb8fce97f2bb235c8a56d1d0a30797)'''
    # AddPthreads(env, args)
    # AddNetwork(args)

c = {}
c['PROG_NAME'] = 'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_riac'
#c['sourceFiles'] = ['libcaf_io.c']
#c['testFiles'] = ['libcaf_ioTest.c']
#c['runFiles'] = ['main.c']
#c['defines'] = []
c['inclDeps'] = add_dependencies
#c['inclDepsDynamic'] = add_dependencies
#c['inclDepsDynamic_tests'] = add_dependencies
#c['inclDepsDynamic_run'] = add_dependencies
#c['inclDepsStatic'] = add_dependencies
#c['inclDepsStatic_tests'] = add_dependencies
#c['inclDepsStatic_run'] = add_dependencies
DefaultLibraryConfig(c, env, args)