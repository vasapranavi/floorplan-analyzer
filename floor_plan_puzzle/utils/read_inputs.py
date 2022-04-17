def readFromFile(filename):
    """
    :param filename: (str) The name of the file to read from.
    :return: (list) The list of lines from the file.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def readInputFromCommandLine():
    """
    :return: (str) Returns the input from the command line.
    """
    while True:
        try:
            return input('Please enter file path:')
        except EOFError:
            return None
