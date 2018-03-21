#Name: Parth Trehan
#RollNo.: 2010660

def main():
		
	print('Enter base and exponent')
	b,exp = raw_input().split()
	ans = 1
	for i in range(int(exp)):
		ans = ans*int(b)
	return ans

value = main()
print "value is",value