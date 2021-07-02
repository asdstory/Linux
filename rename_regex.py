import glob, re, os

#path = r"D:\Downloads\new\new"
path = os.getcwd()

for filename in glob.glob( path + '\\*' ):
	pattern = r'\.'
	replace = r' '
	spaces_name = re.sub(pattern, replace, filename)

	pattern = r'(\d{3})_(\d{2})\.(\d{2})\.(\d{2})\.mrc' 	
	replace = r'$1_$2_$3_$4.mrc'				
	new_name = re.sub(pattern, replace, spaces_name)
	print(filename + ' -> ' + new_name)
	os.rename(filename, new_name)
