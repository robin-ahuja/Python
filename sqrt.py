def sqrt(x):
    '''
	Compute sqr using Alexendra equation
	'''
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess
		
def main():
    print(sqrt(2))
    print(sqrt(9))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print ('Cannot compute square root of negative number')
    print "Program continue here"		

if __name__ == '__main__':
    main()	