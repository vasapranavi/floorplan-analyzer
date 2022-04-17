from floor_plan_puzzle.process.process_rows import processRows
from floor_plan_puzzle.process.sorting import resturnSorted
from floor_plan_puzzle.process.total import calTotal
from floor_plan_puzzle.utils.output import printOutput
from floor_plan_puzzle.utils.read_inputs import readFromFile, readInputFromCommandLine


def main():
    """
    :return: None
    """
    try:
        # Get the file name from the command line.
        file_name = readInputFromCommandLine()
        # Read the file.
        rows = readFromFile('../resources/'+file_name)
        # Process the rows.
        rooms = processRows(rows)
        # Calculate the total and print output.
        printOutput(calTotal(rooms))
        # Sort the rooms by name.
        resturnSorted(rooms)
        # Print the output.
        for room in rooms:
            printOutput(room)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
