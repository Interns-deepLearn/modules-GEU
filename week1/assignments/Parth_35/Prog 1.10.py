#Name: Parth Trehan
#RollNo.: 2010660

def reverse(str):
	l = len(str)
	for i in range(l/2):
		t = str[i]
		str[i] = str[l-i]
		str[l-i-1] = t
	return str

def main():
	str = raw_input()
	print 'Reversed string',reverse(str)

main()