import unittest
class TestInputs(unittest.TestCase):
    def test_processRows(self):
        from floor_plan_puzzle.process.process_rows import processRows
        expected = 2
        actual = len(processRows(['|               |\n', '|  (office)     |\n', '|               |\n', '|           W   |\n', '|               |\n', '|   S           |\n', '|           +---+--------+\n', '|          /P           S|\n', '|         /              |\n', '|        /   (kitchen)   |\n', '+-------+                |\n', '         \\               |\n', '          \\   SSWP       |\n', '           +-------------+']))
        self.assertEqual(expected, actual)

