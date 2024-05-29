import pandas as pd
from cheat.convex_hull_builder import ConvexHullBuilder

# Поменяйте путь на свой
PATH_TO_SAVE = ""

points_df = pd.read_csv("points.csv")

builder = ConvexHullBuilder(points_df)

result_df = builder.get_convex_hull()

result_df.to_csv(PATH_TO_SAVE, index=False)