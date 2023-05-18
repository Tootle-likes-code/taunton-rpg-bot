from dataclasses import dataclass, field

from ttrpg_base.group import Group
from ttrpg_base.member import Member
from ttrpg_base.session import Session


@dataclass
class SessionAttendance:
    group: Group
    session: Session
    confirmed_members: set[Member] = field(default_factory=set, init=False)
    
    def confirm_attending(self, member: Member, is_attending: bool = True) -> None:
        if is_attending:
            self._add_confirmed_member(member)
        else:
            self._remove_confirmed_member(member)

    def _add_confirmed_member(self, member):
        self.confirmed_members.add(member)

    def _remove_confirmed_member(self, member):
        self.confirmed_members.remove(member)

    def is_attending(self, member: Member) -> bool:
        return member in self.confirmed_members

    def number_attending(self) -> int:
        return len(self.confirmed_members)
