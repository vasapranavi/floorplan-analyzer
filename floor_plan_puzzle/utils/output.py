def printOutput(room):
    """
    :param room:
    :return: None
    """
    print(room.name + ':')
    print(', '.join('{}: {}'.format(k, v) for k, v in room.furn_count.items()))

