# As root, edit /etc/krb5.conf, delete any existing content, and add the following:
[logging]
 default = FILE:/var/log/krb5libs.log
 kdc = FILE:/var/log/krb5kdc.log
 admin_server = FILE:/var/log/kadmind.log

[libdefaults]
 default_realm = NIH.GOV
 dns_lookup_realm = false
 dns_lookup_kdc = false
 ticket_lifetime = 24h
 renew_lifetime = 7d
 forwardable = true

[realms]
 NIH.GOV = {
  kdc = nihdcadhub.nih.gov
  kdc = nihdcadhub2.nih.gov
  kdc = nihdcadhub3.nih.gov
  admin_server = nihdcadhub.nih.gov
 }

[domain_realm]
 .nih.gov = NIH.GOV
 nih.gov = NIH.GOV
 .cit.nih.gov = NIH.GOV
 cit.nih.gov = NIH.GOV

#As your non-root user account, obtain a Kerberos ticket by running: kinit your_user_name@NIH.GOV, replacing your_user_name with your NIH login username. Type your NIH network password when prompted.
#NOTE: the Kerberos ticket acquired above will expire after 12 hours, which may cause the mount to hang. It can be renewed within its lifetime (7 days),

kinit dout2@NIH.GOV

# To mount your Biowulf /data/[user]:

sudo mount -t cifs -o uid=200260959,gid=200260959,cruid=dout2,sec=krb5i //hpcdrive.nih.gov/data /data/biowulf-data-smb/dout2

sudo mount -t cifs -o uid=200238860,gid=200238860,cruid=tanx2,sec=krb5i //hpcdrive.nih.gov/data /data/biowulf-data-smb/tanx2

# Mount LCBBBData shared drive

sudo mount -t cifs -o uid=200260959,gid=200260959,cruid=dout2,sec=krb5i //128.231.112.239/LCBBBData/Jiang_Lab /data/LCBBBData

# How to Find your uid and gid:
id usrname

Reference: https://hpc.nih.gov/docs/hpcdrive.html 