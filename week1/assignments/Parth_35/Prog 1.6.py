#Name: Parth Trehan
#RollNo.: 2010660

def maxx(a,b,c):
	if a<b and a<c:
		if b<c:
			return c
		else:
			return b
	elif b<c and b<a:
		if c<a:
			return a
		else:
			return c
	else:
		if a<b:
			return b
		else:
			return a

def main():
	a,b,c = raw_input().split()
	print 'Maximum of the three number inputted is',maxx(int(a),int(b),int(c))

main()