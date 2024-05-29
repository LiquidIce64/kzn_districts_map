import pandas as pd


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
        raise NotImplementedError()
