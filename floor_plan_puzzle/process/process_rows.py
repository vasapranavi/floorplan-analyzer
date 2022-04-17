from re import finditer, search
from floor_plan_puzzle.schemas.row_segment import RowSegment
from floor_plan_puzzle.schemas.space import Space


def processRows(rows):
    """
    :param rows: (list) List of rows from the file.
    :return: (list) List of rows with spaces.
    """
    furn_types = 'WPSC'
    workspaces = []
    rooms = []
    # rows = readFromFile('floorplan02.txt')
    rows.pop(0)

    for no, row in enumerate(rows):
        found = list(finditer(r'[^/\\|+-]+', row))
        if found:
            rsegs = [RowSegment(no, rs.start(), rs.end()) for rs in found]
            for ws in workspaces:
                for rs in rsegs:
                    if max(ws.segs[-1].col_start, rs.col_start) < min(ws.segs[-1].col_end, rs.col_end):  # add rs to ws
                        ws.segs.append(rs)
                        rsegs.remove(rs)
                        break
                else:  # no rs added => complete
                    text = ''.join([rows[s.row_no][s.col_start:s.col_end] for s in ws.segs])
                    name = search(r'\(\w+\)', text)
                    if name:
                        ws.name = name[0][1:-1]
                        ws.furn_count = {f: text.count(f) for f in furn_types}
                        rooms.append(ws)
                    ws.complete = True
            # reset ws list to only not complete
            workspaces = [ws for ws in workspaces if ws.complete == False]
            # create new wss with remaining rss
            for rs in rsegs:
                newws = Space()
                newws.segs.append(rs)
                workspaces.append(newws)
    return rooms
