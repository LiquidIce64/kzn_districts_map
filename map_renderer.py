import pandas as pd
from ipyleaflet import Map, Marker, Polygon, FullScreenControl, LegendControl
from ipywidgets import Layout


class MapRenderer:
    def __init__(self, district_data: pd.DataFrame, points_data: pd.DataFrame):
        self.__points_data = points_data
        self.__district_data = district_data

    def get_map(self) -> Map:
        """
        TODO:
        - Создать карту с центром в центре города (с медианой lat и медианой lon)
        - Для каждого района нарисовать Polygon с цветом районом
        - Для каждого района нарисовать неперемещаемый Marker в центре района с title=<название_района>
        - Для каждого района добавить в LegendControl цвет с соответствующим именем района
        - Добавить FullScreenControl в карту
        - Использовать в карте Layout(width='100%', height='800px')
        """
        raise NotImplementedError()
