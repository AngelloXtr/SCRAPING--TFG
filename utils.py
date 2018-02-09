# -- coding: utf-8 --

def count_itetrations(word,file_path):
	f = open(file_path,"r")
	data = f.read()
	f.close()
	data = data.split()

	n_iterations = 0
	for line in data:
		if word.upper() in line.upper():
			n_iterations = n_iterations+1
			print line

	return n_iterations

print count_itetrations("España","output.txt")