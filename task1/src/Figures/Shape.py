from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_area(self):
        pass