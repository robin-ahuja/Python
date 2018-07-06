def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b
		

def print_inifinite():
    for item in lucas():
        print item
		
if __name__ == '__main__':
    print_inifinite()