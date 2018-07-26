import unittest

def digit(x):
    """convert a integer in to list of digits
    args:
        x: numbers
    Return:
          a list of digits
    """
    digs = []
    while x !=0:
        div, mod = divmod(x, 10)
        digs.append(mod)
        x = div
    return digs


def is_Palindrome(x):
    """determine if no is palindrome
    Args :
        x: the no. of checks of palindromicity
    """
    digs = digit(x)
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False
        return True


class Tests(unittest.TestCase):
    """Test for is_palindrome number"""
    def test_negative(self):
        """check that no is not palindrome"""
        self.assertFalse(is_Palindrome(1234))

    def test_positive(self):
        """check that no. if positive"""
        self.assertTrue(is_Palindrome(12321))

    def test_single_digit(self):
        """check that it works for single digit no."""
        for i in range(10):
            self.assertTrue(is_Palindrome(i))


if __name__ == '__main__':
        unittest.main()
