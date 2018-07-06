import sys

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")
		

if __name__ == '__main__':
    first(sys.argv)
