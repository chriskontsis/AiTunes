import math
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self):
        pass
    
    def makeRadar(self, df):
        avgMoods = df.drop(['name'], axis=1).mean().rename_axis('name').reset_index()
        print(avgMoods)
        # temp = df.drop(["name"], axis=1)
        # normalized_df = temp.rank(pct = True)
        # categories = list(normalized_df)

        # print(categories)
        # N = len(categories)

        #ax.set_title(str(df['name'].iloc[x*subs+y][:17] + "..."), fontsize=8)




def main():
    df = pd.read_csv("./Data/feature-data/calm_features.csv")
    viz = Visualizer()
    viz.makeRadar(df)
    #print(df)

if __name__ == "__main__":
    main() 