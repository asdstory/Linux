# Synchronize files from remote server to local drive

#First, cd into your local folder that you want the data to be transfered
#Then, do rsync as follows:

rsync -r -a -v -e ssh dout2@tf20leginon.jianglab.science:/data1/frames/2019-10-29-TYD-sidH-corrected-averages/*sum_DW.mrc ./

# Synchronize the whole foder from remote server to local drive

#On our own Linux computer, cd /data/nhlbi-nfs/lab-jiang/EM-PROCESSED-DATA/dout2/PnuC

rsync -r -a -v -e ssh dout2@tf20leginon.jianglab.science:/data1/frames/2019-11-28-TYD-PnuC_3NR-corrected-averages ./

rsync -r -a -v -e ssh dout2@tf20leginon.jianglab.science:/data1/frames/2019-11-05-Tongyi-sidH-30-finished-frames ./

# Synchronize from one directory to another (both are local drive)

rsync -r -a -z -h -v ~/Desktop/2019-10-29-TYD-sidH-corrected-averages ./

# Transfer from shared folder to Biowulf

#Login to hpcdrive.nih.gov

ssh -X dout2@hpcdrive.nih.gov

#mkdir a new folder and cd into it

mkdir xxx

cd xxx

#do rsync, like: 

rsync -r -a -v -e ssh smb://hl-share.nhlbi.nih.gov/bbc/Lab-Jiang/ ./

# For Mac, just cd to your folder on your Mac,

cd /Volumes/bbc/Lab-Jiang/EM-RAW-DATA/jiangy6

#Do rsync 
rsync -r -a -v -e ssh /Volumes/bbc/Lab-Jiang/EM-RAW-DATA/dout2/PnuC/2019-10-08-PnuC-C8-Krios_counting-finished-frames jiangy6@helix.nih.gov:/data/jiangy6/ 

# Transfer from one folder to another (local drive)

#make a new folder

mkdir xxx
cd xxx

#Then,do

rsync -a -v /data/dout2/20190429Krios_PnuC-C8/2019-04-29-PnuC-C8_Krios_patch-7-corrected-averages/*_sum_DW.mrc ./

rsync -a -v /data/nhlbi-nfs/lab-jiang/EM-PROCESSED-DATA/dout2/sidH-30/2019-11-05-Tongyi-sidH-30-corrected-averages/*_sum_DW.mrc ./
