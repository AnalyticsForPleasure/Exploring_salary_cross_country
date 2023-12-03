import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':

    labels_male = ['Data\nScientist','Research\nScientist','Software\nEngineer\nManager', 'Project\nEngineer','Product\nMarketing\nManager', 'Research\nDirector']
    labels_female =['Data\nScientist','Research\nScientist','Software\nEngineer\nManager', 'Project\nEngineer','Product\nMarketing\nManager', 'Research\nDirector']
    Male_PhD = [238, 203, 142,46,43,31]
    Female_PhD = [129, 75, 67,38,34,29]

    x = np.arange(len(labels_female))
    width = 0.5

    plt.figure(figsize=(12, 5))

    plt.subplot(121)
    fontdict_input = {'fontsize': 13, 'weight': 'heavy', 'ha': 'center', 'alpha': 0.9, 'color': 'Gray'}
    plt.title('Types of positions for male with a Ph.D', fontsize=18, fontdict=fontdict_input , fontname='Franklin Gothic Medium Cond')
    plt.bar(x - width / 2 + 0.08 , Male_PhD, width, label='test1', hatch='^', color=np.array((199, 66, 120)) / 255)
    plt.xticks([0, 1, 2, 3, 4, 5], labels_male, fontsize=12.5)

    plt.subplot(122)
    plt.title('Types of positions for female with a Ph.D', fontsize=18,  fontdict=fontdict_input , fontname='Franklin Gothic Medium Cond')
    plt.bar(x - width / 2 + 0.08, Female_PhD, width, hatch='/', color=np.array((199, 199, 92)) / 255)
    plt.xticks([0, 1, 2, 3, 4, 5], labels_female , fontsize=12.5)

    plt.figlegend(loc='upper right', ncol=1, labelspacing=0.4, fontsize=14, bbox_to_anchor=(1.11, 0.9))
    plt.tight_layout(w_pad=6)
    plt.show()

