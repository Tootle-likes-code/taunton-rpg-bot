from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def get(self, pk_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, object_to_update=None, pk_id: int | None = None):
        pass

    def delete(self, object_to_delete=None, pk_id: int | None = None):
        pass

    def delete_range(self, objects_to_delete: list):
        pass
