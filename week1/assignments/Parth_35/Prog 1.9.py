#Name: Parth Trehan
#RollNo.: 2010660

def translate(str):
	consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
	str1 = ""
	for i in str:
		if i in consonants:
			str1 = str1+i+'o'+i
		else:
			str1 = str1+i

	return str1

def main():
	str = raw_input()
	print 'Converted format',translate(str)

main()