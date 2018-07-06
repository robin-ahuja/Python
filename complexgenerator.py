def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct(iterable):
    """Return distinct item by eliminiating duplicates """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)
		
def run_take():
    items = [2,4,6,8,10]
    for item in take(3, items):
        print(item)

		
def run_distinct():
    items = [2,4,6,8,8,10,10]
    for item in distinct(items):
        print(item)

def run_pipeline():
    items = [3,6,6,7,8,3,3]
    for item in take(3, distinct(items)):
        print(item)
if __name__ == '__main__':
    run_take()
    run_distinct()
    print "===================="
    run_pipeline()