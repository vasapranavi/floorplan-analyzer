import unittest
class TestInputs(unittest.TestCase):
    def test_readFromFile(self):
        """
        Test if the read_fromFile function works
        """
        from floor_plan_puzzle.utils.read_inputs import readFromFile
        self.assertEqual(readFromFile('../test_inputs/text_input.txt'), ['testinput'])
    def test_readInputFromCommandLine(self):
        """
        Test if the read_inputFromCommandLine function works
        """
        from floor_plan_puzzle.utils.read_inputs import readInputFromCommandLine
        import sys
        sys.argv = ['test_read_inputFromCommandLine', '-i', 'tests/test_inputs/text_input.txt']
        self.assertEqual(readInputFromCommandLine(), 'tests/test_inputs/test_input.txt')

