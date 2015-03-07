Ultra-Cloud Generator
=====

Generator is:

0. Generator of Java, JavaScript, C or any other code from single ucl.yml file
1. Uses plugin-architecture - simply write your own generator-plugin and point ucl generator in "type" field of ucl.yml
2. Integrated into golang-like workspace structure (http://golang.org/doc/code.html), but can be easily configured

If you want to change default path to the Projects workspace directory just change 'PROJECTS_ROOT_PATH' variable in 'src/config.py' file. 

Usage
---

ucl gen [UclYmlFilePath] [options]

or 

generator [UclYmlFilePath] [options]

UclYmlFilePath can be absolute or relative to current path or 
relative to workspace sources root directory e.g.:

    ucl gen github.com/osblinnikov/generator/example -g c

Available options:

    -g {generator folder name e.g java, js, c, connector or any other folder you created in the plugin}
    -c        # execute cleaning for chosen Topology, will remove generated code from files

Other options can be Cog specific.

Examples:

    ucl gen .. -g c -c
    ucl gen example -g c
