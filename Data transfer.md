# Synchronize from TF20 remote server to local drivee

#First, cd into your local folder that you want the data to be transfered
#Then, do rsync as follows:

- [ ] rsync -r -a -v -e ssh dout2@tf20leginon.jianglab.science:/data1/frames/2019-10-29-TYD-sidH-corrected-averages/*sum_DW.mrc ./

#On our own Linux computer, cd /data/nhlbi-nfs/lab-jiang/EM-PROCESSED-DATA/dout2/PnuC

- [ ] rsync -r -a -v -e ssh dout2@tf20leginon.jianglab.science:/data1/frames/2019-11-28-TYD-PnuC_3NR-corrected-averages ./

- [ ] rsync -r -a -v -e ssh dout2@tf20leginon.jianglab.science:/data1/frames/2019-11-05-Tongyi-sidH-30-finished-frames ./

Or, just:

- [ ] rsync -r -a -v -e ssh dout2@tf20leginon.jianglab.science:/data1/frames/2020-09-30-TYD-RhopH-2pulldown* .

# Transfer from shared folder to Biowulf

#Login to hpcdrive.nih.gov

- [ ] ssh -X dout2@hpcdrive.nih.gov

#mkdir a new folder and cd into it

mkdir xxx

cd xxx

#do rsync, like: 

- [ ] rsync -r -a -v -e ssh smb://hl-share.nhlbi.nih.gov/bbc/Lab-Jiang/ ./

# Transfer from shared lab folder to Biowulf

```sh
rsync -avP -e ssh * helix.nih.gov:/data/dout2/20210702Glacios/Fractions/

```


# Transfer from micefdata1 to biowulf

- [ ] login to the micefdata1: ssh dout2@micefdata1.niddk.nih.gov
- [ ] cd to your project folder
- [ ] rsync -advz ./2020-01-06-PnuC_0NR_C8-leginon-counting-corrected-averages helix.nih.gov:/data/dout2/20200106Krios_PnuC_0NR_C8/

- [ ] rsync -a -d -v -z -e ssh dout2@micefdata1.niddk.nih.gov:/data/nhlbi/dout2/20200302-PnuC_0NR_Nano/2020-03-02-PnuC_0NR_Nano-leginon-counting-corrected-averages/*sum.mrc . 

# Transfer from micefdata1 to lab folder

- [ ] rsync --remove-source-files --progress -a -d -v -z -e ssh dout2@micefdata1.niddk.nih.gov:/data/nhlbi/dout2/20210629Krios_rOAT1-LMNG/2021-06-29-00-00-OAT_LMNG-finished-frames .

# Transfer from Linux local folder to Biowulf

- [ ] rsync -a -d -v -z -e ssh * helix.nih.gov:/data/dout2/20210125Krios_Tomo_PnuCT0-C8/TomoSeries/
- [ ] rsync --progress -avdzh -e ssh * helix.nih.gov:/data/dout2/20210629Krios_rOAT1-LMNG/finished-frames/ 
- [ ] rsync --progress -avdzh -e ssh 3dws10.jianglab.science:/data/nhlbi-nfs/lab-jiang/EM-RAW-DATA/dout2/OAT/20210629Krios_rOAT1-LMNG/2021-06-29-00-00-OAT_LMNG-finished-frames/* .
- [ ] rsync -a -d -v -z -e ssh  *.tif helix.nih.gov://data/dout2/20210122Gracios_PnuCT-3NR-C8/finished-frames

# Transfer from Biowulf to local folder

- [ ] rsync -a -d -v -z -e ssh helix.nih.gov:/data/dout2/20210122Gracios_PnuCT-3NR-C8 .
- [ ] rsync --remove-source-files -av -e ssh helix.nih.gov:/data/dout2/20210412Glacios_UGT1A9-UDPGA .
- [ ] rsync -avzhe ssh --progress helix.nih.gov:/data/dout2/20210524Krios_rOAT1-LMNG/finished-frames .

# For Mac, just cd to your folder on your Mac,

- [ ] cd /Volumes/bbc/Lab-Jiang/EM-RAW-DATA/jiangy6

#Do rsync 
- [ ] rsync -r -a -v -e ssh /Volumes/bbc/Lab-Jiang/EM-RAW-DATA/dout2/PnuC/2019-10-08-PnuC-C8-Krios_counting-finished-frames jiangy6@helix.nih.gov:/data/jiangy6/ 

# Transfer from one folder to another (local drive)

#make a new folder

mkdir xxx
cd xxx

#Then,do

- [ ] rsync -a -v /data/nhlbi-nfs/lab-jiang/EM-PROCESSED-DATA/dout2/CBFSMMHC/2019-11-30-TYD-CBFSMMHC-corrected-averages/*_sum_DW.mrc ./

- [ ] rsync -a -v /data/nhlbi-nfs/lab-jiang/EM-PROCESSED-DATA/dout2/CBFSMMHC/2019-11-30-TYD-CBFSMMHC-corrected-averages/*_sum_DW.mrc ./

- [ ] rsync -a -v /data/nhlbi-nfs/lab-jiang/EM-RAW-DATA/dout2/PnuC/2020-01-06-PnuC-leginon-counting-failed-frames ./

#cd to the destination folder, and do 

- [ ] rsync -a -v /data/biowulf-data-smb/dout2/20200106Krios_PnuC_0NR_C8/2020-01-06-PnuC_0NR_C8-leginon-counting-finished-frames/*.tif ./

# Pre-screening of the raw image
#After transfer data to the lab folder, it is much better for further data processing if we can preview and delete bad images, e.g. whole image were just shot on carbon membane.

## Preview of all images

- [ ] cd to /data/nhlbi-nfs/lab-jiang/EM-PROCESSED-DATA/dout2/PnuC/2019-12-23-TYD-PnuC_0NR-C8-corrected-averages/dosef_quick_png
- [ ] gwenview .

#Screening and delete original image if reasonable, both in EM-RAW folder and EM-PROCESSed foler.

- [ ] find . -name "PnuC_0NR-C8_4x3s_031_Dec23*" -type f -delete 

OR we can also delete mutiple files using regular expression, like this

- [ ] find . -name "PnuC_0NR-C8_3x6s_28[3-9]_Dec25*" -type f -delete





