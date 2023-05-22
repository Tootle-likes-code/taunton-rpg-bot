from abc import ABC, abstractmethod


class AbstractUnitOfWork(ABC):
    def __exit__(self):
        self.rollback()

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
