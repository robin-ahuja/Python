def generator123():
    yield 1
    yield 2
    yield 3
	
def getgenerator():
    gen = generator123()
    print next(gen)

if __name__ == '__main__':
    getgenerator()
    for val in generator123():
        print val