#Name: Parth Trehan
#RollNo.: 2010660

def length(str):
	count = 0
	for i in str:
		count = count+1
	return count

def main():
	str = raw_input()
	print 'Length of string is',length(str)

main()