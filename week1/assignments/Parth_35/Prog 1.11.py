#Name: Parth Trehan
#RollNo.: 2010660

def reverse(str):
	l = len(str)
	str1 = ""
	for i in str:
		str1 = i + str1
	return str1

def main():
	str = raw_input()
	print 'Reversed string',reverse(str)

main()