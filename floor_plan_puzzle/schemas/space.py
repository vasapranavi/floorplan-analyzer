from dataclasses import dataclass, field
from typing import Dict, List
from .row_segment import RowSegment


@dataclass
class Space():
    name: str = 'noname'
    furn_count: Dict[str, int] = field(default_factory=dict)
    segs: List[RowSegment] = field(default_factory=list)
    complete: bool = False

    def __repr__(self):
        return f'{self.name}: {[i for i in self.furn_count.items()]}\n{[s for s in self.segs]}'
