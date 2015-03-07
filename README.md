# Ultra-Cloud project

Implementation of actors suitable for real-time, embedded and distributed systems

The actors model suppose that every agent within the framework is a dynamic entity which can even create other agents. Parent actors can also serve only composition purpose without handling the actual workload. 

Ultra-Cloud project implements a restricted actors model. The simpicity, robustness and possibility of the clear remote monitoring of the developed system comes to the fore in real-time, embedded and distributed systems. In this particular usecase the actors model better be simplified to a topology of actors which is very convinient for the system description and monitoring.

In the topology of actors the concrete agent can send messages to the topology without knowing the destinations of the message. The use of such topology facilitates the code reusability and complexity isolation in the special places called topology descriptions.

In Ultra-Cloud project the topology specification is stored in the ucl.yml file but the implementation of this specification for each programming langugage can be automatically generated.

To enable and facilitate changes in the concrete actor interface Ultra-Cloud project uses basic description of the actor and stores it in the `*.ucl.yml` where `*` is the name of the actor implementation. Basically the `ACTORNAME.ucl.yml` file is a subset of `ucl.yml` specification. The main difference between actor `*.ucl.yml` and topology `ucl.yml` is that developer can't create internal topology in `*.ucl.yml` for the actor. In Ultra-Cloud Project the actor is an atom of the application's internal structure.

ucl.yml
---

`ucl.yml` file is the cornerstone in the ultra-cloud project. This file keeps the description of C, Java, JavaScript topology internal structure and exported interface. 

First of all every topology and module has a **name**. In `ucl.yml` we create a `name` field in the notation of the Url path. E.g. "github.com/osblinnikov/ultra-cloud/cnets/MapBuffer". For C this will generate a structure "com_github_osblinnikov_ultra_cloud_cnets_MapBuffer" and constructor function "com_github_osblinnikov_ultra_cloud_cnets_MapBuffer_create". For Java the actual package name will be translated into "com.github.osblinnikov.ultra_cloud.cnets.MapBuffer".

Let's consider versioning of our module. `ver` field in `ucl.yml` allows us to keep track of versions of the module. But developer should always keep in mind: if the module already used in other projects but there is a need in changing exported interface in the `ucl.yml` it is better to create a different name of the module e.g MapBuffer2 or ImprovedMapBuffer etc. This allows the community members to upgrade their apps and test it again when they will need it or wanted. At the same time it allows users to have different versions of your module in the same application

*.ucl.yml
---

`*.ucl.yml` is a subset of the `ucl.yml` which disallows usage of `topology` key.
