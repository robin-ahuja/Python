import unittest
import  os
def analyze_text(filename):
    """calculate the no. of lines in a file
    args:
         filename: the name of file to analyze
    Raises:
         IOError: if filename doesn't exists
    Return:
         the no. of lines and characters count in a tuple
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    print chars
    return (lines, chars)

class TextAnalyzerTest(unittest.TestCase):
    """Test for analyze_text() function"""

    def setUp(self):
        """Fixture that creates file for the text method to use"""
        self.filename = "text_analyze_test_file.txt"
        with open(self.filename,'w') as f:
            f.write('we are enable user to learn python \n'
                    'testing whether user can understand it \n'
                    'do need to grab it for fully understanding')

    def tearDown(self):
        """fixture that delete the text file"""
        try:
            os.remove(self.filename)
        except:
            pass
    def test_function_run(self):
        """Basic smoke test"""
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 3)

    def test_characters_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 118)

    def test_no_such_file(self):
        """check that proper exception thrown if no such file"""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_file_Deletion(self):
        """check that function doesn't delete the file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))
if __name__ == '__main__':
    unittest.main()
