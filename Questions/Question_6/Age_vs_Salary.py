import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


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

    df['Salary'] = df['Salary'].apply(lambda x: int(x))
    df['Age'] = df['Age'].apply(lambda x: int(x))
    df['Years of Experience'] = df['Years of Experience'].apply(lambda x: int(x))
    print(df['Job Title'].value_counts())
    relevant_data = df.loc[(df['Years of Experience'] <= 10) & (df['Job Title'] == 'Data Analyst')]

    min_age = df['Age'].min()
    max_age = df['Age'].max()
    min_age_for_a_data_analyst = relevant_data['Age'].min()
    max_age_for_a_data_analyst = relevant_data['Age'].max()

    min_salary = df['Salary'].min()
    max_salary = df['Salary'].max()
    min_salary_for_a_data_analyst = relevant_data['Salary'].min()
    max_salary_for_a_data_analyst = relevant_data['Salary'].max()

    x_values = relevant_data['Salary']
    y_values = relevant_data['Age']

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

    # invert y axis
    ax.invert_yaxis()

    # change the appearance of ticks, tick labels, and gridlines
    ax.tick_params(top='on', bottom='off', labelbottom='off', labeltop='on')

    # # remove chart border
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.show()
