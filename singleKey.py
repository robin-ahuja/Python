'''A module to detech single key press'''
try:
    import msvcrt # this library is for windows only.
    def getkey():
        """
		wait for keypress and return a single character
		"""	
        return msvcrt.getch()
except ImportError:
    import sys
    import tty
    import termios

    def getkey():
        """wait for keypress and return a single character	"""
        fd = sys.stdin.fileno()
        original_attribute = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcgetattr(fd, termios.TCSADRAIN, original_attribute)
        return ch