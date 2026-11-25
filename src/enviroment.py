from abc import ABC, abstractmethod
from math import pow, sqrt

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

class CircleObstacle(Obstacle):
    def __init__(self, x: float, y: float, r: float, is_virtual: bool = False):
        super().__init__(is_virtual)
        self.center = (x, y)
        self.radius = r

    @property
    def center(self) -> tuple[float, float]:
        return self._center

    @center.setter
    def center(self, center: tuple[float, float]) -> None:
        self._center = center

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self._radius = radius

    def distance_and_closest_point(self, robot_pos: tuple[float, float], robot_radius: float) -> tuple[float, tuple[float, float], tuple[float, float]]:
        # funzione che restituisce, dato posizione e raggio del robot, la distanza del robot dall'ostacolo, il versore e il punto piu vicino
        # distanza, calcolata come distanza tra centro robot e centro ostacolo a cui vengono sottratti i raggi
        centers_distance = sqrt(pow((robot_pos[0] - self.center[0]), 2) + pow((robot_pos[1] - self.center[1]), 2))
        distance = centers_distance - self.radius - robot_radius
        verser = ((robot_pos[0] - self.center[0]) / centers_distance, (robot_pos[1] - self.center[1]) / centers_distance)
        closest_point = (self.center[0] + (self.radius * verser[0]), self.center[1] + (self.radius * verser[1]))

        return (distance, verser, closest_point)
 
class WallObstacle(Obstacle): 
    def __init__(self, width: float, height: float, is_virtual = False):
        super().__init__(is_virtual)
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, w: float) -> None:
        self._width = w

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, h: float) -> None: 
        self._height = h

    def distance_and_closest_point(self, robot_pos, robot_radius):
        


class Enviroment:
    def __init__(self, width: float, height: float, goal_x: float, goal_y: float):
        self.width = width
        self.height = height
        self.goal = (goal_x, goal_y)
        self._static_obstacles: list[Obstacle] = []
        self._virtual_obstacles: list[Obstacle] = []
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
    def goal(self, goal: tuple[float, float]) -> None:
        self._goal = goal

    @property
    def static_obstacles(self) -> list[Obstacle]:
        return self._static_obstacles

    @static_obstacles.setter
    def static_obstacles(self, obstacles: list[Obstacle] | tuple[Obstacle, ...]) -> None:
        self._static_obstacles.clear()
        for obstacle in obstacles:
            self.add_static_obstacle(obstacle)

    def add_static_obstacle(self, obstacle: Obstacle) -> None:
        self._static_obstacles.append(obstacle)

    @property
    def virtual_obstacles(self) -> list[Obstacle]:
        return self._virtual_obstacles

    @virtual_obstacles.setter
    def virtual_obstacles(self, obstacles: list[Obstacle] | tuple[Obstacle, ...]) -> None:
        self._virtual_obstacles.clear()
        for obstacle in obstacles:
            self.add_virtual_obstacle(obstacle)

    def add_virtual_obstacle(self, obstacle: Obstacle) -> None:
        self._virtual_obstacles.append(obstacle)