
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
    AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_opencl',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_opencl'))
    AddDependency(args,'com_github_osblinnikov_ultra_cloud_actor_framework_libcaf_core',join(args['PROJECTS_ROOT_PATH'],'src/github.com/osblinnikov/ultra-cloud/actor-framework/libcaf_core'))
    '''[[[end]]] (checksum: 68b329da9893e34099c7d8ad5cb9c940)'''
    AddPthreads(env, args)
    # AddNetwork(args)

def add_unit_test(testName, additionalFiles=[]):
    args['PROG_NAME'] = 'com_github_osblinnikov_ultra_cloud_actor_framework_unit_testing_'+testName
    args['prj_env'] = env.Clone()
    add_dependencies(env, args)
    env.Default(PrefixTest(args, '', ['test_'+testName+'.cpp','test.cpp']+additionalFiles))

add_unit_test('ripemd_160')
add_unit_test('variant')
add_unit_test('atom')
add_unit_test('metaprogramming')
#add_unit_test(intrusive_containers)
add_unit_test('match')
add_unit_test('message')
add_unit_test('serialization')
add_unit_test('uniform_type')
add_unit_test('fixed_vector')
add_unit_test('intrusive_ptr')
add_unit_test('spawn', ['ping_pong.cpp'])
add_unit_test('simple_reply_response')
add_unit_test('serial_reply')
add_unit_test('or_else')
add_unit_test('either')
add_unit_test('constructor_attach')
add_unit_test('custom_exception_handler')
add_unit_test('typed_spawn')
add_unit_test('actor_lifetime')
add_unit_test('message_lifetime')
add_unit_test('local_group')
add_unit_test('sync_send')
add_unit_test('broker')
add_unit_test('remote_actor', ['ping_pong.cpp'])
add_unit_test('typed_remote_actor')
add_unit_test('unpublish')
add_unit_test('optional')
add_unit_test('fixed_stack_actor')
add_unit_test('actor_pool')
if args['MSVC_VERSION'] == None and args['COMPILER_CODE'] != 'mingw':
  add_unit_test('profiled_coordinator')