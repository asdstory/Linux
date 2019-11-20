# To mount your Biowulf /data/[user]:

kinit dout2@NIH.GOV

sudo mount -t cifs -o uid=200260959,gid=200260959,cruid=dout2,sec=krb5i //hpcdrive.nih.gov/data /data/biowulf-data-smb/dout2

sudo mount -t cifs -o uid=200238860,gid=200238860,cruid=tanx2,sec=krb5i //hpcdrive.nih.gov/data /data/biowulf-data-smb/tanx2

# Mount LCBBBData shared drive

#Under root, add following command into your /etc/fstab.
//128.231.112.239/LCBBBData/Jiang_Lab /data/niddk-LCBBBData cifs rw,domain=NIH.gov,vers=1.0,noauto,user 0 0

#Or,
sudo mount -t cifs -o uid=200260959,gid=200260959,cruid=dout2,sec=krb5i //128.231.112.239/LCBBBData/Jiang_Lab /data/niddk-LCBBBData



# How to Find your uid and gid:
id usrname

Reference: https://hpc.nih.gov/docs/hpcdrive.html 
