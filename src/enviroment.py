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