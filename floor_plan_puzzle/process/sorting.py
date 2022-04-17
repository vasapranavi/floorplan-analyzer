def resturnSorted(rooms):
    """
    :param rooms: (list) List of rooms.
    :return: (list) List of rooms sorted by name.
    """
    return rooms.sort(key=lambda x: x.name)