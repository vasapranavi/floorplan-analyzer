from schemas.space import Space


def calTotal(rooms):
    """
    :param rooms: (list) List of rooms.
    :return: (int) Total number of furnitures in all rooms.
    """
    total = Space()
    total.name = 'total'
    for r in rooms:
        # total += sum(r.furn_count.values())
        for k, v in r.furn_count.items():
            total.furn_count[k] = total.furn_count.get(k, 0) + v
    return total