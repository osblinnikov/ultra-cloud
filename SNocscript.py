
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
  AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_core',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_core'))
  AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_io',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_io'))
  AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_opencl',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_opencl'))
  AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_riac',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_riac'))

c = {}
c['PROG_NAME'] = 'com_github_osblinnikov_ultra_cloud_parent'
c['inclDeps'] = add_dependencies
DefaultParentConfig(c, env, args)