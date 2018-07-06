import sys
from math import log
'''
A Module to describe exception
'''
def convert(s):
    '''Convert to integer '''
    x = -1	
    try:	
        return int(x)
    except (ValueError, TypeError) as e:
        sys.stderr.write(str(e))
        raise    
		
def string_log(s):
    if not isinstance(s, int):
        raise TypeError("Argument must be integer")
    v = convert(s)
    return log(v)	