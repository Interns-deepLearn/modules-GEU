#Name: Parth Trehan
#RollNo.: 2010660

def is_pallindrome(str):
	l = len(str)
	for i in range(0,l):
		if str[i]!=str[l-i-1]:
			return False
	return True

def main():
	print 'Enter string'
	str = raw_input()
	if is_pallindrome(str) == True:
		print 'Pallindrome'
	else:
		print 'Not Pallindrome'

main()