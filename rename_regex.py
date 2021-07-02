#How to use: Just "chmod +x rename,py" and then "python ./rename.py". 

import glob, re, os

path = os.getcwd()

for filename in glob.glob( path + '/*' ):
	pattern = r'(\d{3})_(\d{2})\.(\d{2})\.(\d{2})\.mrc'				
	replace = r'\1_\2_\3_\4.mrc'	
	if re.search( pattern, filename ):
		new_name = re.sub(pattern, replace, filename)
		print(filename + ' -> ' + new_name)
		os.rename(filename, new_name)	
	
