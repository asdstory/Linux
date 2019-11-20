# To mount your Biowulf /data/[user]:

#Under root, add following command into your /etc/fstab.

//hpcdrive.nih.gov/data /data/biowulf-data-smb/dout2 cifs rw,sec=krb5i,username=dout2,domain=NIH.gov,vers=1.0,noauto,user 0 0

#Do following command
kinit dout2@NIH.GOV

sudo mount -t cifs -o uid=200260959,gid=200260959,cruid=dout2,sec=krb5i //hpcdrive.nih.gov/data /data/biowulf-data-smb/dout2

#For Xiaofeng, it is
sudo mount -t cifs -o uid=200238860,gid=200238860,cruid=tanx2,sec=krb5i //hpcdrive.nih.gov/data /data/biowulf-data-smb/tanx2

# Mount LCBBBData shared drive

#Under root, add following command into your /etc/fstab.
//128.231.112.239/LCBBBData/Jiang_Lab /data/niddk-LCBBBData cifs rw,domain=NIH.gov,vers=1.0,noauto,user 0 0

#Do following command
sudo mount -t cifs -o user=dout2 //128.231.112.239/LCBBData/Jiang_Lab /data/niddk-LCBBData



# How to Find your uid and gid:
#Just do following command
id usrname

Reference: https://hpc.nih.gov/docs/hpcdrive.html 
