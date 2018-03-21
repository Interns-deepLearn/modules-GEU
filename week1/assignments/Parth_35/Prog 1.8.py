#Name: Parth Trehan
#RollNo.: 2010660

def fun(str):
	vowel="AaEeIiOoUu"
	if len(str) == 1:
		if str in vowel:
			return True
		else:
			print 'Enter vowel, forky'
			return False
	else:
		print 'Just a character'
		return False

def main():
	print 'Enter a character'
	str = raw_input()
	print fun(str)

main()