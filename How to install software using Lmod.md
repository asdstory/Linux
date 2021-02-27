# How to manage personal modules on Linux

## How to set up:
### You can make copies of the system modulefiles in "/usr/local/lmod/modulefiles" to use as templates, edit and save as your own lua file. 
- [ ] scp -r /data/jianglab-nfs/programs/modulefiles/IMOD .

## How to use: 
- [ ] module use --append ~/modulefiles
- [ ] module avail
- [ ] module load xxx
- [ ] 
### From: https://hpc.nih.gov/apps/modules.html#personal
### File name : 4.11.3.lua
```sh

local base = "/data/jianglab-nfs/programs/apps/imod_4.11.3/IMOD"
local description = "IMOD is a set of image processing, modeling and display programs used for tomographic reconstruction and for 3D reconstruction of EM serial sections and optical sections."

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
### File name: 4.10.10.lua

```sh
-- Susan

local version     = myModuleVersion()
local app         = myModuleName()
local base = "/usr/local/apps/IMOD/imod_"..version
local description = "IMOD is a set of image processing, modeling and display programs used for tomographic reconstruction and for 3D reconstruction of EM serial sections and optical sections."

whatis(description)
whatis("Version " .. version)

setenv("IMOD_DIR",base)
setenv("IMOD_JAVADIR","/usr/local/java")
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

if (mode() == "load") then
   if ( os.getenv("SLURM_CPUS_ON_NODE") == nil) then
      setenv("IMOD_PROCESSORS", "1")
   else
      setenv("IMOD_PROCESSORS", os.getenv("SLURM_CPUS_ON_NODE"))
   end
    LmodMessage("[+] Loading IMOD ", version, ". Running with ",os.getenv("IMOD_PROCESSORS")," CPUs" )
end
if (mode() == "unload") then
    LmodMessage("[-] Unloading IMOD ", version, " ...")
end

```
