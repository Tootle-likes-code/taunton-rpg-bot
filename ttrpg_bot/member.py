from dataclasses import dataclass


@dataclass
class Member:
    id: int
    name: str

    def __hash__(self):
        return hash(self.id) + hash(self.name)
