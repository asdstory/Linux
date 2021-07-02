import glob, re, os

path = r"D:\Downloads\new\new"

for filename in glob.glob( path + '\\*' ):
	pattern = r'\.'
	replace = r' '
	spaces_name = re.sub(pattern, replace, filename)

	pattern = r'(.*) (19|20)(\d{2}).* (.{3})$'				# movie
	replace = r'\1 (\2\3).\4'								# movie
	#pattern = r'(.*) [sS](\d\d)[eE](\d\d).* (.{3})' 		# tv show
	#replace = r'\1 [\2x\3].\4'								# tv show
	new_name = re.sub(pattern, replace, spaces_name)
	print(filename + ' -> ' + new_name)
	os.rename(filename, new_name)
