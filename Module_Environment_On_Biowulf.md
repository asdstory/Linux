#This instruction shows how to permenantly load the "/data/JiangLab/Apps/modulefiles" into your biowulf environment, e.g., after that, you can just module load RELION to use the "RELION/3.0.8 => RELION/3.1.biowulf.jiang-copy".

# Step01 - Login to your Biowulf account

- [ ] ssh -Y dout2@biowulf.nih.gov

# Step02 - Edit the ~/.bash_profile

- [ ] vi ~/.bash_profile
- [ ] module use /data/JiangLab/Apps/modulefiles #Add this line under "export PATH", as following
- [ ] Press esc
- [ ] :wq

````
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin

export PATH

module use /data/JiangLab/Apps/modulefiles


````

# Step03 - exit biowulf and login again, and try

- [ ] module spider relion 
#You will see more relion versions like this: 

``````````````
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RELION:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     Versions:
        RELION/2.1.0_jiang_cuda-arch-35
        RELION/2.1.0_jiang_cuda-arch-60
        RELION/2.1.0
        RELION/3.0_beta_jiang
        RELION/3.0_gpu_icc_jiang
        RELION/3.0.0.jiang
        RELION/3.0
        RELION/3.0.2.biowulf.jiang-copy
        RELION/3.0.2
        RELION/3.0.4.biowulf.jiang-copy
        RELION/3.0.4
        RELION/3.0.5
        RELION/3.0.6.biowulf.jiang-copy
        RELION/3.0.6
        RELION/3.0.7.biowulf.jiang-copy
        RELION/3.0.7
        RELION/3.0.8
        RELION/3.1-beta.biowulf.jiang-copy
        RELION/3.1-beta
        RELION/3.1.biowulf.jiang-copy
        RELION/3.1

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  For detailed information about a specific "RELION" module (including how to load the modules) use the module's full name.
  For example:

     $ module spider RELION/3.1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```````````````````````````



