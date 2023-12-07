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
    print('*')
    # Adding the coordinates
    df['Salary'] = df['Salary'].apply(lambda x: int(x))
    df['Age'] = df['Age'].apply(lambda x: int(x))

    # df['coordinates'] = df.apply(lambda row: (row['Salary'], row['Age']), axis=1)

    relevent_data = df.loc[(df['Job Title'] == 'Data Analyst') & (df['Years of Experience'] == 3)]
    # relevent_data =  df.loc[(df['Job Title'] == 'Data Analyst')]
    result = relevent_data['Years of Experience'].value_counts()
    relevent_data.shape[0]
    print('*')
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
    x_values = relevent_data['Salary']
    y_values = relevent_data['Age']
    print('*')

    # create new figure
    fig, ax = plt.subplots(figsize=(8.2, 5.4),  # width, height in inches
                           dpi=110)  # resolution of the figure

    # tune the subplot layout by setting sides of the figure
    fig.subplots_adjust(left=0.262, right=0.875, top=0.605, bottom=0.06)

    # draw colored scatterplot
    colors = [GRAY7, RED1, RED1, RED1, GRAY7, RED1, GRAY8]  # GRAY7
    colors = plt.cm.Dark2(range(len(y_values)))
    ax.scatter(x_values, y_values, color=plt.cm.Dark2(range(len(y_values))), s=80)

    # annotate with colored labels with offsets
    txt_colors = [GRAY6, RED1, RED1, RED1, GRAY6, RED1]  # GRAY6

    for i, coord in enumerate(zip(x_values, y_values)):
        ax.annotate('Worker ' + str(i),  # Model X text of the annotation
                    xy=coord,  # (x,y) point to annotate
                    xytext=(0, 0),  # (x,y) to place the text at
                    textcoords='offset points',  # offset (in points)
                    color=colors[i],
                    fontsize=11)

    # draw prior year average point

    # draw prior year average vertical and horizontal ref lines
    # plt.axvline(x=72, color=GRAY1, linewidth=0.5)
    # plt.axhline(y=900, color=GRAY1, linewidth=0.5)
    #
    # # annotate prior year average point
    # ax1.text(64, 880, 'Prior Year Avg.', color=GRAY3, fontsize=12, fontweight='bold')
    # ax1.text(66.6, 980, '(all models)', color=GRAY3, fontsize=10)
    #
    # # set the data limits for the y-axis and x-axis
    # ax1.set_xlim([350, 19500])  # min and max values for the salaries
    # ax1.set_ylim([21, 62])  # min and max values for the ages
    #
    # # invert y axis
    ax.invert_yaxis()
    #
    # # set properties for axes object
    # xticks = list(range(60, 95, 5))  # calculate x ticks
    # yticks = list(range(0, 1600, 200))  # calculate y ticks
    # plt.setp(ax1,
    #          xticks=xticks,  # set x ticks
    #          xticklabels=[str(i) + '%' for i in xticks],  # with n% labels
    #          yticks=yticks)
    #
    # # change the appearance of ticks, tick labels, and gridlines
    ax.tick_params(top='on', bottom='off', labelbottom='off', labeltop='on')

    # # remove chart border
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.show()
