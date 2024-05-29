import pandas as pd
import math


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Коллинеарны
    return 1 if val > 0 else 2  # Против или по часовой стрелке


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def convex_hull(points):
    # находим стартовую точку
    start = points[0]
    for p in points:
        if p[1] < start[1] or p[1] == start[1] and p[0] < start[0]:
            start = p

    # сортируем остальные точки по углу
    points = [[p, math.atan2(p[1] - start[1], p[0] - start[0])] for p in points if p != start]
    points.sort(key=lambda x: x[1], reverse=True)

    # среди точек с одинаковым углом отбираем дальние
    queue = []
    prev_ang = -1
    for p, ang in points:
        if ang == prev_ang:
            if dist(start, p) > dist(start, queue[-1]):
                queue[-1] = p
        else:
            queue.append(p)
        prev_ang = ang

    queue.append(start)  # добавляем стартовую точку в конец, чтобы последняя точка проверялась на левый поворот

    # добавляем точки, проверяя на левый поворот
    hull = [start]
    for p in queue:
        while len(hull) >= 2 and orientation(p, hull[-1], hull[-2]) != 2:
            hull.pop()
        hull.append(p)

    hull.pop()  # убираем дублирующуюся начальную точку с конца

    return hull


DISTRICT_COLORS = [
    "green",
    "blue",
    "yellow",
    "red",
    "pink",
    "white",
    "black",
    "brown"
]


class ConvexHullBuilder:
    def __init__(self, points: pd.DataFrame):
        self.__points = points

    def get_convex_hull(self) -> pd.DataFrame:
        """
        Формат выходного датафрейма:
        - district
            Название района
        - points
            Список точек выпуклой оболочки района
        - center
            Кортеж центра района (lat, lon)
        - color
            Цвет оболочки района
        """
        district_df = pd.DataFrame(columns=('district', 'points', 'center', 'color'))
        i = 0
        for district in self.__points.district.unique():
            district_points = self.__points[self.__points['district'] == district].loc[:, ['lat', 'lon']]
            points = district_points.values.tolist()
            hull = convex_hull(points)
            center = (district_points['lat'].mean(), district_points['lon'].mean())
            color = DISTRICT_COLORS[i]
            district_df.loc[i] = [district, hull, center, color]
            i += 1
        return district_df
