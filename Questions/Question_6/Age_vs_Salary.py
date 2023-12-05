import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv \
        ('/home/shay_diy/PycharmProjects/Exploring_salary_cross_country/data/salary_by_job_country/Salary.csv')

    relevent_data =  df.loc[(df['Job Title'] == 'Data Analyst')]

    min_age = df['Age'].min()
    max_age = df['Age'].max()
    min_age_for_a_data_analyst = relevent_data['Age'].min()
    max_age_for_a_data_analyst = relevent_data['Age'].max()

    min_salary = df['Salary'].min()
    max_salary = df['Salary'].max()
    min_salary_for_a_data_analyst = relevent_data['Salary'].min()
    max_salary_for_a_data_analyst = relevent_data['Salary'].max()
    print('*')

    # Creating the chart :

    # define colors
    GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
    GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
    GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
    BLUE1, BLUE2, BLUE3, BLUE4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
    RED1, RED2 = '#C3514E', '#E6BAB7'
    GREEN1, GREEN2 = '#0C8040', '#9ABB59'
    ORANGE1 = '#F79747'

    # configure plot font family to Arial
    plt.rcParams['font.family'] = 'Arial'
    # configure mathtext bold and italic font family to Arial
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.bf'] = 'Arial:bold'
    plt.rcParams['mathtext.it'] = 'Arial:italic'

    # Adding the coordinates
    relevent_data['Salary'] = relevent_data['Salary'].apply(lambda x: int(x))
    relevent_data['Age'] = relevent_data['Age'].apply(lambda x: int(x))

    relevent_data['coordinates'] = relevent_data.apply(lambda row: (row['Salary'], row['Age']), axis=1)
    x_values = relevent_data['Gender']
    y_values =  np.array([relevent_data['coordinates']])
    print('*')

    # create new figure
    fig, ax1 = plt.subplots(figsize=(8.2, 5.4),  # width, height in inches
                            dpi=110)  # resolution of the figure

    # tune the subplot layout by setting sides of the figure
    fig.subplots_adjust(left=0.262, right=0.875, top=0.605, bottom=0.06)

    # draw colored scatterplot
    #colors = [GRAY7, RED1, RED1, RED1, GRAY7, RED1, GRAY7]
    ax1.scatter(y_values[:, 0], y_values[:, 1], s=80) # color=colors



    # annotate with colored labels with offsets
    #txt_colors = [GRAY6, RED1, RED1, RED1, GRAY6, RED1, GRAY6]
    #offsets = [(10, -4), (-35, -18), (-7, -18), (10, -4),
    #           (10, -4), (10, -4), (10, -4)]

    # for i, n in enumerate(x_values):
    #     ax1.annotate('Model ' + n,  # Model X text of the annotation
    #                  y_values[i],  # (x,y) point to annotate
    #                  #xytext=offsets[i],  # (x,y) to place the text at
    #                  textcoords='offset points',  # offset (in points)
    #                  #color=txt_colors[i],
    #                  fontsize=11)

