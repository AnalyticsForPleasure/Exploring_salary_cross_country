import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import dataframe_image as dfi


# **************************************************************************************************************
# Function  name: preparing_the_matrix_before_illustration
# input: creating a matrix in size of 4*8
# return value: full counter matrix
# ***************************************************************************************************************
def preparing_the_matrix_before_illustration(df):
    df_male = df.loc[df['Gender'] == 'Male', :]
    list_of_top_rolls_for_male_matrix_1 = ['Bank end Developer', 'Full Stack Engineer',
                                           'Software Developer', 'Software Engineer', 'Principal Engineer',
                                           'director of data Science', 'Chief Data Officer']

    list_of_top_rolls_for_male_matrix_2 = ['Sales Associate', 'Sales Director', 'Sales Representative',
                                           'Customer Service Representative', 'Sales Executive',
                                           'Account Manager', 'Customer Success Rep']

    list_of_top_rolls_for_male_matrix_3 = ['Director of Operation', 'Project Manager',
                                           'Project Engineer', 'Operations Manager',
                                           'VP of Operations', 'Supply Chain Manager', 'Supply Chain Analyst']

    data_filters_dfs = [df_male[df_male['Job Title'].isin(list_of_top_rolls_for_male_matrix_1)],
                        df_male[df_male['Job Title'].isin(list_of_top_rolls_for_male_matrix_2)],
                        df_male[df_male['Job Title'].isin(list_of_top_rolls_for_male_matrix_3)]]

    print(f'{len(df_male["Job Title"].unique())}')
    print(f'{len(df_male["Education Level"].unique())}')

    dict_rows = {
        'rows_names_rd': ['Bank end Developer', 'Full Stack Engineer', 'Software Developer', 'Software Engineer',
                          'Principal Engineer', 'director of data Science', 'Chief Data Officer'],
        'rows_names_sales': ['Sales Associate', 'Sales Director', 'Sales Representative',
                             'Customer Service Representative', 'Sales Executive', 'Account Manager',
                             'Customer Success Rep'],
        'rows_names_operations': ['Director of Operation', 'Project Manager', 'Project Engineer', 'Operations Manager',
                                  'VP of Operations', 'Supply Chain Manager', 'Supply Chain Analyst']}
    accumulate_dataframes = []
    for rows_names in dict_rows.values():
        accumulate_dataframes.append(pd.DataFrame(data=np.zeros((7, 4)),
                                                  index=rows_names,
                                                  dtype=int))

    old_names = range(4)
    new_names = ['Highschool', 'Bsc', 'Master', 'PhD']

    for datafilter, accumulate_df in zip(data_filters_dfs, accumulate_dataframes):
        for idx, current_row in datafilter.iterrows():
            accumulate_df.loc[current_row['Job Title'], current_row['Education Level']] += 1
        accumulate_df.rename(columns=dict(zip(old_names, new_names)), inplace=True)

    return accumulate_dataframes


# **************************************************************************************************************
# Function  name: creating_the_heatmap
# input:
# return value:
# ***************************************************************************************************************
def creating_the_heatmap(matrix, matrix_sales, matrix_operations, font_prop):
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))

    ax[0] = sns.heatmap(matrix,
                        vmin=0,
                        vmax=matrix.to_numpy().max(),
                        center=0,
                        cmap="Greens",
                        # cmap=sns.diverging_palette(20, 220, n=200),
                        square=True,
                        ax=ax[0],
                        cbar=False,  # color bar scale
                        linewidth=3.5,
                        annot=True,
                        fmt='.3g'
                        )

    ax[1] = sns.heatmap(matrix_sales,
                        vmin=0,
                        vmax=matrix_sales.to_numpy().max(),
                        cmap="Blues",
                        center=0,
                        # cmap=sns.diverging_palette(20, 220, n=200),
                        square=True,
                        ax=ax[1],
                        cbar=False,
                        linewidth=3.5,
                        annot=True,
                        fmt='.3g'
                        )

    ax[2] = sns.heatmap(matrix_operations,
                        vmin=0,
                        vmax=matrix_operations.to_numpy().max(),
                        cmap="Purples",
                        center=0,
                        # cmap=sns.diverging_palette(20, 220, n=200),
                        square=True,
                        ax=ax[2],
                        cbar=False,
                        linewidth=3.5,
                        annot=True,
                        fmt='.3g'
                        )

    ax[0].set_title('R&D Positions', fontsize=16, fontname=font_prop['fontname'])
    ax[1].set_title('Sales Positions ', fontsize=16, fontname=font_prop['fontname'])
    ax[2].set_title('Operations Positions ', fontsize=16, fontname=font_prop['fontname'])

    # plt.title('Exploring the Relationship Between Education Levels and Job Titles',fontname=font_prop['fontname'], color =font_prop['color'],fontsize =font_prop['fontsize'])
    ax[1].text(8.75, -0.75, 'Exploring the Relationship Between Education Levels and Job Titles',
               fontname=font_prop['fontname'], horizontalalignment='right',
               color=font_prop['color'], fontsize=font_prop['fontsize'])

    # Adding rectangle for information inside the chart
    ax[0].annotate('Highest values', xy=(1.1, 3), fontsize=9, color='black', weight='bold')  # , horizontala
    ax[0].add_patch(patches.Rectangle(
        (1, 3),  # offset
        2.0,  # columns
        1.0,  # rows
        edgecolor='Black',
        fill=False,
        lw=2
    ))

    # Adding rectangle for information inside the chart
    ax[2].annotate('Highest values', xy=(2.35, 2), fontsize=9, color='black', weight='bold')  # , horizontala
    ax[2].add_patch(patches.Rectangle(
        (3, 2),  # offset (x,y)
        1.0,  # columns - x
        1.0,  # rows - y
        edgecolor='Black',
        fill=False,
        lw=2
    ))

    plt.savefig('3_heatmaps_chart.jpg', dpi=250, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')
    column_headers = list(df.columns.values)
    print('*')

    font_properties = {'fontsize': 32,
                       'weight': 'heavy',
                       'ha': 'center',
                       'alpha': 0.9,
                       'color': 'Gray',
                       'fontname': 'Franklin Gothic Medium Cond'
                       }

    result, result_2, result_3 = preparing_the_matrix_before_illustration(df)
    creating_the_heatmap(result, result_2, result_3, font_properties)
    print('*')
