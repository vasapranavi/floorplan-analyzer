from dataclasses import dataclass


@dataclass
class RowSegment():
    row_no: int
    col_start: int
    col_end: int

    def __repr__(self):
        return f'{self.row_no}:{self.col_start}-{self.col_end}'
