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

    # Adding the coordinates
    df['Salary'] = df['Salary'].apply(lambda x: int(x))
    df['Age'] = df['Age'].apply(lambda x: int(x))

    df['coordinates'] = df.apply(lambda row: (row['Salary'], row['Age']), axis=1)

    relevent_data = df.loc[(df['Job Title'] == 'Data Analyst') & (df['Years of Experience'] == 6)]
    #relevent_data =  df.loc[(df['Job Title'] == 'Data Analyst')]
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
    # relevent_data['Salary'] = relevent_data['Salary'].apply(lambda x: int(x))
    # relevent_data['Age'] = relevent_data['Age'].apply(lambda x: int(x))
    #
    # relevent_data['coordinates'] = relevent_data.apply(lambda row: (row['Salary'], row['Age']), axis=1)
    x_values = relevent_data['Gender']
    y_values =  np.array([relevent_data['coordinates']])
    print('*')

    # create new figure
    fig, ax1 = plt.subplots(figsize=(8.2, 5.4),  # width, height in inches
                            dpi=110)  # resolution of the figure

    # tune the subplot layout by setting sides of the figure
    fig.subplots_adjust(left=0.262, right=0.875, top=0.605, bottom=0.06)

    # draw colored scatterplot
    colors = [GRAY7, RED1, RED1, RED1, GRAY7, RED1] # GRAY7
    ax1.scatter(y_values[:, 0], y_values[:, 1], color=colors, s=80)

    # annotate with colored labels with offsets
    txt_colors = [GRAY6, RED1, RED1, RED1, GRAY6, RED1] #  GRAY6
    offsets = [(10, -4), (-35, -18), (-7, -18), (10, -4),
               (10, -4), (10, -4)]

    #TODO: need to digure out the problem - > c' argument has 6 elements, which is inconsistent with 'x' and 'y' with size 1.
    for i, n in enumerate(x_values):
        ax1.annotate('Worker ' + n,  # Model X text of the annotation
                     y_values[i],  # (x,y) point to annotate
                     xytext=offsets[i],  # (x,y) to place the text at
                     textcoords='offset points',  # offset (in points)
                     color=txt_colors[i],
                     fontsize=11)

    # draw prior year average point
    ax1.scatter([72], [900], color=GRAY1, s=80)

    # draw prior year average vertical and horizontal ref lines
    plt.axvline(x=72, color=GRAY1, linewidth=0.5)
    plt.axhline(y=900, color=GRAY1, linewidth=0.5)

    # annotate prior year average point
    ax1.text(64, 880, 'Prior Year Avg.', color=GRAY3, fontsize=12, fontweight='bold')
    ax1.text(66.6, 980, '(all models)', color=GRAY3, fontsize=10)

    # set the data limits for the y-axis and x-axis
    ax1.set_xlim([350, 19500]) # min and max values for the salaries
    ax1.set_ylim([21, 62]) # min and max values for the ages

    # invert y axis
    ax1.invert_yaxis()

    # set properties for axes object
    xticks = list(range(60, 95, 5))  # calculate x ticks
    yticks = list(range(0, 1600, 200))  # calculate y ticks
    plt.setp(ax1,
             xticks=xticks,  # set x ticks
             xticklabels=[str(i) + '%' for i in xticks],  # with n% labels
             yticks=yticks)

    # change the appearance of ticks, tick labels, and gridlines
    ax1.tick_params(top='on', bottom='off', labelbottom='off', labeltop='on')

    # remove chart border
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)


    plt.show()