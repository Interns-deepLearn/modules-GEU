#Name: Parth Trehan
#RollNo.: 2010660

def maxx(a,b):
	if a>=b:
		return a
	else:
		return b

def main():
	print 'Enter two numbers'
	a,b = raw_input().split()
	print 'The maximum between the two is',maxx(int(a),int(b))

main()