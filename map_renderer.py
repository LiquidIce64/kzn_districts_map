import pandas as pd
from ipyleaflet import Map, Marker, Polygon, FullScreenControl, LegendControl
from ipywidgets import Layout
import ast


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
        map_center = (self.__points_data['lat'].mean(), self.__points_data['lon'].mean())
        m = Map(center=map_center, layout=Layout(width='100%', height='800px'))
        legend = LegendControl({}, title="Районы Казани", position="bottomright")
        for district, points, center, color in self.__district_data.to_numpy():
            points = [tuple(p) for p in ast.literal_eval(points)]
            center = ast.literal_eval(center)
            m.add(Polygon(
                locations=points,
                color=color,
                fill_color=color
            ))
            m.add(Marker(location=center, title=district, draggable=False))
            legend.add_legend_element(key=district, value=color)
        m.add(legend)
        m.add(FullScreenControl())
        return m
