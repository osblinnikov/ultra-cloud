
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
    '''[[[cog
    import cogging as c
    c.tpl(cog,templateFile,c.a(prefix=configFile))
    ]]]'''
    AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_riac',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_riac'))
    AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_io',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_io'))
    AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_core',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_core'))
    '''[[[end]]] (checksum: 68b329da9893e34099c7d8ad5cb9c940)'''
    AddPthreads(env, args)
    # AddNetwork(args)
    conf = Configure(args['prj_env'])
    if not conf.CheckLibWithHeader('edit', 'histedit.h', 'c'):
        print 'Did not find libedit.a or edit.lib, exiting!'
        Exit(1)
    args['prj_env'] = conf.Finish()


c = {}
c['PROG_NAME'] = 'com_github_osblinnikov_ultra_cloud_actor_framework_cash'
c['paths'] = ['sash']
#c['sourceFiles'] = ['libcaf_core.c']
#c['testFiles'] = ['libcaf_coreTest.c']
c['runFiles'] = ['main.cpp']
#c['defines'] = []
c['inclDeps'] = add_dependencies
#c['inclDepsDynamic'] = add_dependencies
#c['inclDepsStatic'] = add_dependencies
#c['inclDepsStatic_tests'] = add_dependencies
#c['inclDepsStatic_run'] = add_dependencies
DefaultLibraryConfig(c, env, args)