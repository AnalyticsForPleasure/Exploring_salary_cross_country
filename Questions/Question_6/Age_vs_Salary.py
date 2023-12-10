import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# **************************************************************************************************************
# Function  name: my_funct
# input: entering 3 - x,y of the specific coordinate , mean age and mean salary
# return value: Returning the relative color for each point
# ***************************************************************************************************************
def my_funct(my_tup, mean_age, mean_salary):
    age, salary = my_tup
    if (age > mean_age) & (salary > mean_salary):
        return "pink"
    elif (age > mean_age) & (salary < mean_salary):
        return "green"
    elif (age < mean_age) & (salary < mean_salary):
        return "red"

    return "blue"


# Define a function to format tick labels with commas
def format_ticks_with_commas(value, _):
    return f"{value:,.0f}$"

# **************************************************************************************************************
# Function  name: creating_a_scatter_avg_chart
# input:
# return value:
# ***************************************************************************************************************
def creating_a_scatter_avg_chart(df, font_prop):

    df['Salary'] = df['Salary'].apply(lambda x: int(x))
    df['Age'] = df['Age'].apply(lambda x: int(x))
    df['Years of Experience'] = df['Years of Experience'].apply(lambda x: int(x))
    #print(df['Job Title'].value_counts())

    #job_type = 'Data Scientist'

    job_type = 'Project Engineer'
    relevant_data = df.loc[(df['Years of Experience'] <= 15) & (df['Job Title'] == job_type)]

    x_values = relevant_data['Salary']
    min_salary= x_values.min()
    max_salary = x_values.max()

    y_values = relevant_data['Age']
    min_Age = y_values.min()
    max_Age = y_values.max()

    # create new figure
    fig, ax = plt.subplots(figsize=(8.2, 5.4),  # width, height in inches
                           dpi=110)  # resolution of the figure
    mean_salary_ds = relevant_data['Salary'].mean()
    mean_age_ds = relevant_data['Age'].mean()
    relevant_data['color'] = relevant_data.loc[:, ['Age', 'Salary']].apply(
        lambda pair: my_funct(pair, mean_age_ds, mean_salary_ds), axis=1)
    ax.scatter(x_values, y_values, color=relevant_data['color'], s=80)
    ax.set_xlabel("Salary")
    ax.set_ylabel("Age")
    # Apply the formatter to the x-axis
    ax.xaxis.set_major_formatter(FuncFormatter(format_ticks_with_commas))
    plt.axvline(x=mean_salary_ds, linewidth=0.5)  # color=gray,
    plt.axhline(y=relevant_data['Age'].mean(), linewidth=0.5)  # color=GRAY1,
    ax.annotate('My avg Salary',
                xy=(mean_salary_ds, 30))
    ax.annotate('My avg Age',
                xy=(100000, mean_age_ds))


    ax.scatter([mean_salary_ds], [mean_age_ds],
               marker='o',
               linestyle='dashed',
               s=250,
               facecolor='none',
               edgecolor='blue')

    ax.set_title(f'Salary distribution within the role of a {job_type}',
                fontsize=font_prop['fontsize'],
                fontname=font_prop['fontname'],
                color='Black')

    # invert y axis
    ax.invert_yaxis()
    # change the appearance of ticks, tick labels, and gridlines
    ax.tick_params(top='on', bottom='off', labelbottom='off', labeltop='on')
    # # remove chart border
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)



    # Adding arrows inside the chart :

    # ax.annotate('Highest Salary', xy=(25, 6), xytext=(27, 12), size=14,
    #             arrowprops=dict(arrowstyle='->'), ha='center');
    # ax.annotate('Lowest Salary', xy=(25, 6), xytext=(27, 12), size=14,
    #             arrowprops=dict(arrowstyle='->'), ha='center');

    # ax.annotate('Youngest Age', xy=(25, 6), xytext=(27, 12), size=14,
    #             arrowprops=dict(arrowstyle='->'), ha='center');
    # ax.annotate('Oldest Age', xy=(25, 6), xytext=(27, 12), size=14,
    #             arrowprops=dict(arrowstyle='->'), ha='center');

    #
    # Upper - Left Corner
    ax.annotate('Lowest Salary', xy=(min_salary + 100 , min_Age ),
                xycoords='data',
                xytext=(min_salary + 10000, min_Age),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )
    ax.annotate('Youngest Age', xy=(min_salary + 100 , min_Age ),
                xycoords='data',
                xytext=(min_salary + 100, min_Age +3  ),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )

    # Down - Left Corner
    ax.annotate('Oldest Age', xy=(min_salary  , max_Age ),
                xycoords='data',
                xytext=(min_salary+min_salary*0.2 , max_Age),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )

    ax.annotate('Lowest Salary', xy=(min_salary , max_Age),
                xycoords='data',
                xytext=(min_salary  , max_Age-max_Age*0.05 ),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )

    # Upper - right Corner

    ax.annotate(' Highest Salary ', xy=(max_salary , min_Age),  # target
                xycoords='data',
                xytext=(max_salary - 11000, min_Age+min_Age*0.2),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )

    ax.annotate(' Youngest Age', xy=(max_salary , min_Age),  # target
                xycoords='data',
                xytext=(max_salary - max_salary*0.2, min_Age),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )

    # Down - right Corner
    ax.annotate('Oldest Age', xy=(max_salary  , max_Age ), # target
                xycoords='data',
                xytext=(max_salary , max_Age-max_Age*0.2),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )
    #
    ax.annotate('Highest Salary', xy=(max_salary , max_Age), # target
                xycoords='data',
                xytext=(max_salary -max_salary*0.2 , max_Age ),
                textcoords='data',
                arrowprops=dict(arrowstyle='->',
                                color='gray',
                                lw=2.5,
                                ls='--')
                )



    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    # configure plot font family to Arial
    # plt.rcParams['font.family'] = 'Arial'
    # # configure mathtext bold and italic font family to Arial
    # plt.rcParams['mathtext.fontset'] = 'custom'
    # plt.rcParams['mathtext.bf'] = 'Arial:bold'
    # plt.rcParams['mathtext.it'] = 'Arial:italic'

    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')

    # ['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience', 'Salary', 'Country', 'Race', 'Senior']

    font_properties = {'fontsize': 22,
                       'weight': 'heavy',
                       'ha': 'center',
                       'alpha': 0.9,
                       'color': 'Gray',
                       'fontname':'Franklin Gothic Medium Cond'
                       }

    res = creating_a_scatter_avg_chart(df, font_properties)
