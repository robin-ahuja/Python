import sys
from urllib2 import urlopen

def fetch_words(url):
    """Fetch a list of words from URL
	
	Args: 
	    url: the url of a UTF-8 decode
	Return:
        the list of strings	
    """
    story = urlopen(url)
    story_words = []
    for line in story:
		line_words = line.split()
		for word in line_words:
			story_words.append(word)
    return story_words		

def print_Items(items):			
	for wrd in items:
		print wrd

def main(url):
    words = fetch_words(url)
    print_Items(words)
	
if __name__ == '__main__':
    main(sys.argv[1]) # The 0 argv is the module filename   