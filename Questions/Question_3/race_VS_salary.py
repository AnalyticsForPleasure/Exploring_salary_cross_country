import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# **************************************************************************************************************
# Function  name: retrieving_the_mean_salary_of_a_asian_data_analyst
# input: entering the dataframe
# return value:
# ***************************************************************************************************************

def retrieving_the_mean_salary_of_a_asian_data_analyst(df):
    male_data = df.loc[(df['Gender'] == 'Male')]
    relevent_data = male_data.loc[(male_data['Race'] == 'Asian') & (male_data['Job Title'] == 'Data Analyst')]
    relevent_data2 = relevent_data.loc[
        (relevent_data['Years of Experience'] >= 5) & (relevent_data['Years of Experience'] <= 10)]
    result = relevent_data2.groupby(['Country'])['Salary'].mean()
    final_result = result.reset_index()
    Years_of_experience_result = relevent_data2.groupby(['Country'])['Salary'].count()
    Years_of_experience_result_std = relevent_data2.groupby(['Country'])['Salary'].std()
    return final_result



# **************************************************************************************************************
# Function  name: creating_an_opposite_bar_chart
# input: entering the dataframe
# return value:
# ***************************************************************************************************************
def creating_an_opposite_bar_chart(final_result , font_prop):

    countries  = final_result.loc[:,'Country']
    avg_salary  = final_result.loc[:,'Salary']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # increase space below subplot
    fig.subplots_adjust(bottom=0.3)
    ax.bar(countries,
           avg_salary,
           width=0.3,
           )
    # invert y axis
    ax.invert_yaxis()
    # label x axis
    ax.set_xticks(range(len(final_result)))
    ax.set_xticklabels(countries,
                       fontdict={'fontsize': 14})

    norm = plt.Normalize(min(avg_salary), max(avg_salary))


    colors = ['darkgreen', 'green', 'lightgreen', 'darkgreen']

    bars = ax.bar(countries, avg_salary, color=colors)
    ax.set_title(f'The average salary for male Asian data analysts across the identical continents', fontsize=18, fontdict=font_prop,fontname=font_prop['fontname'])
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)


    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('/home/shay_diy/PycharmProjects/Exploring_salary_cross_country/data/salary_by_job_country/Salary.csv')
    print('*')


    font_properties = {'fontsize': 22,
                       'weight': 'heavy',
                       'ha': 'center',
                       'alpha': 0.9,
                       'color': 'Gray',
                       'fontname':'Franklin Gothic Medium Cond'
                       }


    res = retrieving_the_mean_salary_of_a_asian_data_analyst(df)
    creating_an_opposite_bar_chart(res,font_properties )

    print('*')



