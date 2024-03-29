from math import pi
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self):
        pass
    
    def makeRadar(self, df, title):
        avgMoods = df.drop(['name'], axis=1).mean().rename_axis('name').reset_index()
        categories = list(avgMoods.iloc[:,0].tolist())
        N = len(categories)

        normalized = avgMoods.iloc[:,1].rank(pct=True)
        values = normalized.tolist()
        values += values[:1]

        print(values)
        print(categories)
        
        #ax.set_title(str(df['name'].iloc[x*subs+y][:17] + "..."), fontsize=8)

        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1], categories, color='Black', size=9)
        ax.set_title(title, fontsize=16)
        ax.plot(angles, values, linewidth=1, linestyle='solid') 
        ax.fill(angles, values, 'b', alpha=0.1)
        plt.show()



def main():
    df = pd.read_csv("./Data/feature-data/calm_features.csv")
    viz = Visualizer()
    viz.makeRadar(df, "Calm")
    #print(df)

if __name__ == "__main__":
    main() 