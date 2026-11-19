from abc import ABC, abstractmethod

class Obstacle(ABC):
    def __init__(self, is_virtual: bool = False):
        self.is_virtual = is_virtual

    @property
    def is_virtual(self) -> bool:
        return self._is_virtual

    @is_virtual.setter
    def is_virtual(self, is_virtual: bool) -> None:
        self._is_virtual = is_virtual

    @abstractmethod
    def distance_and_closest_point(self, robot_pos: tuple[float, float], robot_radius: float) -> tuple[float, tuple[float, float], tuple[float, float]]:
        pass

class Enviroment:
    def __init__(self, width: float, height: float, goal_x: float, goal_y: float):
        self.width = width
        self.height = height
        self.goal = (goal_x, goal_y)
        self.static_obstacles = []
        self.virtual_obstacles = []

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, valore: float) -> None:
        self._width = valore

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, valore: float) -> None:
        self._height = valore

    @property
    def goal(self) -> tuple[float, float]:
        return self._goal

    @goal.setter
    def goal(self, x: float, y: float) -> None:
        self._goal = (x, y)


    