# To mount your Biowulf /data/[user]:

#Under root, add following command into your /etc/fstab.

//hpcdrive.nih.gov/data /data/biowulf-data-smb/dout2 cifs rw,sec=krb5i,username=dout2,domain=NIH.gov,vers=1.0,noauto,user 0 0

#Do following command

- [ ] kinit dout2@NIH.GOV

- [ ] mount /data/biowulf-data-smb/dout2

#For Xiaofeng, it is

- [ ] sudo mount -t cifs -o uid=200238860,gid=200238860,cruid=tanx2,sec=krb5i //hpcdrive.nih.gov/data /data/biowulf-data-smb/tanx2

# Mount LCBBData shared drive

#Under root, add following command into your /etc/fstab.

#NIDDK LCCB Data drive for TF20
- [ ] //128.231.112.239/LCBBData/Jiang_Lab /data/niddk-LCCBData cifs rw,domain=NIH.gov,vers=1.0,noauto,user 0 0

# NIDDK LCCB Data drive for TF20
- [ ] //128.231.112.180/LCBBData /data/niddk-LCCBData cifs rw,domain=NIH.gov,vers=1.0,noauto,user 0 0


#Do following command

- [ ] mount /data/niddk-LCCBData

# Mount the hl-share drive that contain Glacios data:

#Under root, add following command into your /etc/fstab.

- [ ] sudo vi /etc/fstab

###hl-share drive of MICEF dirshare for Glacios, etc.

- [ ] //hl-share.nhlbi.nih.gov/dirshare /data/hl-share cifs rw,username=dout2,domain=NIH.gov,vers=3.0,noauto,user 0 0
### Then, do following command

- [ ] mount /data/hl-share


# How to Find your uid and gid:
#Just do following command
- [ ] id usrname

Reference: https://hpc.nih.gov/docs/hpcdrive.html 


