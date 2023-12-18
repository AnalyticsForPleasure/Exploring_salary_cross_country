import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# **************************************************************************************************************
# Function  name: preparing_the_matrix_before_illustration
# input: creating a matrix in size of 4*8
# return value: full counter matrix
# ***************************************************************************************************************
def preparing_the_matrix_before_illustration(df):
    df_male = df.loc[df['Gender'] == 'Male', :]
    list_of_top_rolls_for_male = ['Bank end Developer', 'Front and Developer', 'Full Stack Engineer',
                                  'Software Developer', 'Software Engineer', 'Principal Engineer',
                                  'director of data Science', 'Chief Data Officer']
    new_df_male = df_male[df_male['Job Title'].isin(list_of_top_rolls_for_male)]
    print(f'{len(df_male["Job Title"].unique())}')
    print(f'{len(df_male["Education Level"].unique())}')
    columns_names = df_male["Education Level"].unique()
    rows_names = ['Bank end Developer', 'Front and Developer', 'Full Stack Engineer', 'Software Developer',
                  'Software Engineer', 'Principal Engineer', 'director of data Science', 'Chief Data Officer']
    print('*')

    matrix = pd.DataFrame(data=np.zeros((8, 4)),
                          index=rows_names,
                          dtype=int)
    for idx, current_row in new_df_male.iterrows():
        matrix.loc[current_row['Job Title'], current_row['Education Level']] += 1
    print('*')
    old_names = [0, 1, 2, 3]
    new_names = ['Highschool', 'Bsc', 'Master', 'PhD']
    matrix.rename(columns=dict(zip(old_names, new_names)), inplace=True)

    return matrix

# **************************************************************************************************************
# Function  name: creating_the_heatmap
# input:
# return value:
# ***************************************************************************************************************
def creating_the_heatmap(matrix,font_prop):
    ax = sns.heatmap(matrix,
                     vmin=0,
                     vmax=matrix.to_numpy().max(),
                     center=0,
                     cmap=sns.diverging_palette(20, 220, n=200),
                     square=False
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    )
    ax.set_title('Hi-Tech Workforce Insights: \n Education Levels and Job Titles Heat Map', fontdict={'size': 50}, fontsize=font_prop['fontsize'],
                 fontname=font_prop['fontname'])
    plt.savefig('heatmap_chart.jpg', dpi=250, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')

    font_properties = {'fontsize': 32,
                       'weight': 'heavy',
                       'ha': 'center',
                       'alpha': 0.9,
                       'color': 'Gray',
                       'fontname': 'Franklin Gothic Medium Cond'
                       }


    result = preparing_the_matrix_before_illustration(df)
    creating_the_heatmap(result,font_properties )
    print('*')
