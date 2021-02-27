# How to manage personal modules on Linux
## file name : 4.11.3.lua
## How to use: 
- [ ] module use --append ~/modulefiles
- [ ] module avail
- [ ] module load xxx
- [ ] 
### From: https://hpc.nih.gov/apps/modules.html#personal

```sh

local base = "/data/jianglab-nfs/programs/apps/imod_4.11.3/IMOD"
local description = "IMOD is a set of image processing, modeling and display programs used for tomographic reconstruction and for 3D reconstruction of EM serial sections and optical se$

whatis(description)

setenv("IMOD_DIR",base)
setenv("IMOD_JAVADIR","/usr/lib/jvm/java-11-openjdk-amd64")
setenv("IMOD_PLUGIN_DIR",pathJoin(base,"lib/imodplug"))
setenv("FOR_DISABLE_STACK_TRACE","1")
setenv("IMOD_QTLIBDIR",pathJoin(base,"qtlib"))
setenv("IMOD_CALIB_DIR","/usr/local/apps/IMOD/ImodCalib")
prepend_path("PATH", pathJoin(base, "bin"))
prepend_path("LD_LIBRARY_PATH", pathJoin(base, "lib"))
prepend_path("MANPATH", pathJoin(base, "man"))

local bashStr = 'submfg "$@"'
local cshStr = "submfg $*"
set_shell_function("subm",bashStr,cshStr)

```
