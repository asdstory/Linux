Suppose you have several versions of the mythical UCC compiler suite:

$ module avail ucc
---------- /opt/apps/modulefiles/Core -----------
ucc/8.1   ucc/9.2   ucc/11.1   ucc/12.2 (D)
and you would like to make the 11.1 version the default. Lmod searches three different ways to mark a version as a default in the following order. The first way is to make a symbolic link between a file named “default” and the desired default version.:

$ cd /opt/apps/modulefiles/Core/ucc; ln -s 11.1.lua default
A second way to mark a default is with a .modulerc.lua file in the same directory as the modulefiles.:

module_version("ucc/11.1", "default")
A third way to mark a default is with a .modulerc file in the same directory as the modulefiles.:

#%Module
module-version ucc/11.1 default
There is a four method to pick the default module. If you create a .version file in the ucc directory that contains:

#%Module
set   ModulesVersion   "11.1"
Please note that a .modulerc.lua, .modulerc or .version file must be in the same directory as the 11.1.lua file in order for Lmod to read it.

Using any of the above three ways will change the default to version 11.1.

$ module avail ucc
---------- /opt/apps/modulefiles/Core -----------
ucc/8.1   ucc/9.2   ucc/11.1 (D)   ucc/12.2
Lmod Order of Marking a Default
As stated above, there are four files used to mark a default:

#. default symlink
#. .modulerc.lua
#. .modulerc
#. .version
Lmod searches in this order. If it finds the a number earlier in the list then the other are ignored. In other words if your site as both a default symlink and a .modulerc.lua file then the default file is used and the .modulerc.lua file is ignored.

*Reference: https://lmod.readthedocs.io/en/latest/060_locating.html

