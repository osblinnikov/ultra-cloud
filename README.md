# Ultra-Cloud project

Implementation of actors suitable for real-time, embedded and distributed systems

The actors model suggests that every agent within the framework is a dynamic entity which communicates preferably only via message passing and can even create new agents. Parent actors can also serve only composition purpose without handling the actual workload. 

The simpicity, robustness and possibility of the clear remote monitoring of the developed system comes to the fore in real-time, embedded and distributed systems. 

Ultra-Cloud project implements this `restricted actors model`. In such topology of actors a concrete agent can send messages via its interfaces without knowing the exact destination of the message. Usage of the topology facilitates the code reusability, isolation of complexity and separation of concerns.

The topology specification in Ultra-Cloud project is stored in `ucl.yml` file. The implementation source code can be automatically generated for any programming langugage using [generator](./generator). The use of code-generators  means that the resulting code becomes fully accessable, debuggable and suitable for quick bug-fixes. The framework library doesn't need to carry all the heavy algorithms resulting in smaller footprint and faster program execution.

Ultra-Cloud project generator updates only the blocks of code which are enclosed within `/*[[[cog]]]*/` and `/*[[[end]]] (checksum: 28926fd84afa051f0bffc6691b831551) */` tags to allow changes in the actor's structure and messaging interface during the developmet. The checksum allows code-generator to detect the manual or incidental changes to the source-code and to notify developer about this. Your own changes to the source code will never be ovverriden without your participation!

ucl.yml
---

`ucl.yml` file is the cornerstone in the ultra-cloud project. This file keeps the description of the application's topology structure and it's exported interfaces. The following section is meant to describe this standard. 

In most cases developers doesn't need to know all the standard because Ultra-Cloud team is going to make a web-based GUI to help you with the construction and modification of this file. 

    * If you want it to happen then please provide your feedback in our issue tracker!


ucl.yml standard
---

1. `name`. First of all every topology and module has a **name**. In `ucl.yml` we create a `name` field in the notation of the Url path. E.g. `name:"github.com/osblinnikov/Ultra-Cloud/Dispatcher"`. For C it is translated to a struct "com_github_osblinnikov_ultra_cloud_Dispatcher" with constructor function "com_github_osblinnikov_ultra_cloud_Dispatcher_create". For Java the name will be translated into "com.github.osblinnikov.ultra_cloud.Dispatcher".  For C++ the name will be translated into "com::github::osblinnikov::ultra_cloud::Dispatcher". 

Developer should always keep in mind: if the module already used in other projects and there is a need in changing exported messaging interface it is better to create a copy of module with different name e.g Dispatcher2 or ImprovedDispatcher etc. This allows the community members to upgrade and test their apps when they will need or want it. At the same time it allows users to have different versions of the module simultaneously.

2. `gen` is a list of URL names of the generators which are going to be used with the topology. e.g

    "gen":[
      "github.com/osblinnikov/ultra-cloud/plugins/java",
      "github.com/osblinnikov/ultra-cloud/plugins/maven",
      "github.com/osblinnikov/ultra-cloud/plugins/gradle",
      "github.com/osblinnikov/ultra-cloud/plugins/c",
      "github.com/osblinnikov/ultra-cloud/plugins/cmake",
      "github.com/osblinnikov/ultra-cloud/plugins/snocs"
    ]
    
  * What every developer should remember is that different generators can be incompatible with each other e.g. they can overrite the same directories or files. To check if the generator is compatible with each other you can simply compare their directory structures. E.g. compare `github.com/osblinnikov/ultra-cloud/plugins/c` and `github.com/osblinnikov/ultra-cloud/plugins/java`. Notice that the files will be generated only if they have .tpl counterpart in the generator folder.
    

3. `emit` and `receive` are lists of the strings like this:
    
    "emit":[
      "emitInteger int",
      "emitStructure github.com/osblinnikov/ultra-cloud/generator/exampleType"
    ]
    
Separator " " separates `name` and `type`. The `name` field keeps an identificator which is unique for this module. The `type` field keeps a name of the structure which is going to be emitted/received. 

  * Keep in mind that every generator for different programming language expects that we specified it in the `depends` field or included it manually in the build automation system.

4. `depends` is a list which allows us to provide dependencies names. Any different generator in the field `gen` is free to have it's own behaviour of the dependencies inclusion. The main purpose of the `depends` field is to collect ALL the dependencies in the SINGLE place.

    "depends":[
      "superdomain.com/superprojectInC++",
      "superdomain.com/superprojectInJava"
    ]

  * Before code generation, make sure that all specified dependencies are installed into the workspace. If some dependencies are not installed then generators MUST skip them from inclusion because different build systems can have different dependencies.


The behaviour of the `github.com/osblinnikov/ultra-cloud/plugins/snocs` generator is to specify the dependencies in the SNonsfile (wrapper of SCons) pipeline so the compiler can find and build deps before building the module. The specified dependencies must also provide SNocsfile.
    
The behaviour of the `github.com/osblinnikov/ultra-cloud/plugins/maven` generator is to write the dependencies into pom.xml file with the hope that this module will be available in the build system.

5. `args` is a list of the strings like this:  

    "args":[
      "fakeArgument int",
      "initialStructureArray github.com/osblinnikov/ultra-cloud/generator/exampleType"
    ]
  
Separator " " separates `name` and `type`. The `name` field keeps an identificator which is unique for this module. The `type` field keeps a name of the structure which is going to be received.
  
  * Keep in mind that every generator for different programming language expects that we specified the module of this structure in the `depends` field or included it manually in the build automation system files.
  
6. `props` field is a list of the strings like `args`. But there is one key difference in the specification of arrays - in props you MUST provide "size" attribute along with the array type:

    "props":[
      "fakeProperty github.com/osblinnikov/ultra-cloud/generator/exampleType",
      "fakePropertyArray int[] 10",
      "fakePropertyArrayWithSizeFromArguments int[] fakeArgument"
    ]
  
7. `actors` field is a list of the actors objects like: 

    "actors":[{
      "name":"actor0",
      "type":"github.com/osblinnikov/ultra-cloud/generator/exampleActor",
      "args":[
        "1000L", /*timeout_milisec*/ 
        "fakePropertyArray" /*buffers*/ 
      }],
      "parallel":"fakeArgument", /*[optional] count of actor instances which will work in parallel*/
      "dispatchEvery":"1000L", /*[optional] if actor work+sleep more than the specified miliseconds then the dispatcher must launch it again*/
      "emit":["buffer0", "buffer1"], /*sends the emitted data directly into the specified buffers*/
      "receive":["buffer2", "buffer3", "export receiveInteger"] /*receives the emitted data directly from the specified buffers or exported connectors, the exporting of connectors allows Ultra-Cloud to build heirarchies of the actors topologies*/
    }]

8. `buffers` field is another cornerstone of the Ultra-Cloud project. The main feature of the buffers is that they always sit in the middle between the actors. 
 
New types of buffers can be created by anyone who need it. For example one would implement a buffer for the connection to the specifed WebSocket server. Another wants to convert the developed topology into the distributed application with proprietary network messaging.

Buffer must follow to the programming guidelines and interfaces of Ultra-Cloud project: BufferInterface and NetworkBufferInterface.

Developement of new buffer type (BufferInterface)
---


Development of new network buffer type (NetworkBufferInterface)
---

Stand-alone application can be easily installed across the cluster thus automaticaly becomes distributed.
The applications can (and will) be exactly the same everywhere in the cluster if you are using the standard Ultra-cloud Dispatcher. The only thing that differs from node to node is the ip-address:port candidates dynamically assigned to the client and discovered by STUN/TURN requests. During the startup of the applications Dispatcher will connect to the predefined master WebSocket server (which for example can be a Haproxy with fallback strategy to all the cluster computers). After that application will receive modifications to the local topology using diffs. These diffs affect Dispatcher which stops some actors and establishes more network connections to remote peers instead of stopped actors.

Every Dispatcher monitors the current connection status to the master and distributed peers. In case the peers will disappear - dispatcher immediatelly starts it's local copy of the actor to fill the application with data and at the same time notifies the master node about the lost peer. Master node can start looking for the solution and orchestrate other peers. Also master peer will send report about the problem and the new network solution.

  * Keep in mind that the local state stored in the faulty peer is lost! Usually it is the worst problem which distributed systems can suffer. The Ultra-Cloud solution for this is two folded:
  
      1. Try to keep actors state-less. The least number of actors will store the state - the better
      2. Configure master node to have actors replicas. This will duplicate traffic across the network, but it can also provide the way to sustain a sudden shutdown.

  
*.ucl.yml
---

`*.ucl.yml` is a subset of the `ucl.yml` which disallows usage of `actors` and `buffers` keys.
