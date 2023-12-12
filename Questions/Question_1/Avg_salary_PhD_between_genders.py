import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sys
from matplotlib.colors import LinearSegmentedColormap  # in order to add the gradient color


# **************************************************************************************************************
# Function  name: salary_for_phd_position_separated_by_men_and_women
# input:
# return value:
# ****************************************************************************************************************
def salary_for_phd_position_separated_by_men_and_women(df):
    # In the hi-tech industry, what types of positions do individuals with a Ph.D. typically hold? ( Male  Vs Female )
    phd_users = df.loc[(df['Education Level'] == 3)]
    phd_female = phd_users.loc[(df['Gender'] == 'Female')]  # Female
    phd_male = phd_users.loc[(df['Gender'] == 'Male')]  # Male
    top_phd_position_for_female_jobs = phd_female['Job Title'].value_counts().head(n=6)
    top_phd_position_for_male_jobs = phd_male['Job Title'].value_counts().head(n=6)
    res_female = top_phd_position_for_female_jobs.reset_index()
    res_male = top_phd_position_for_male_jobs.reset_index()
    print('*')
    list_of_top_rolls_for_female = list(res_female.loc[:, 'Job Title'])
    list_of_top_rolls_for_male = list(res_male.loc[:, 'Job Title'])
    print('*')

    top_rolls_for_female  = phd_female[phd_female['Job Title'].isin(list_of_top_rolls_for_female)]
    top_rolls_for_male = phd_male[phd_male['Job Title'].isin(list_of_top_rolls_for_male)]

    result_avg_salary_female = top_rolls_for_female.groupby(['Job Title'])['Salary'].mean()
    result_avg_salary_male = top_rolls_for_male.groupby(['Job Title'])['Salary'].mean()

    result_avg_salary_female = result_avg_salary_female.reset_index()
    result_avg_salary_female.sort_values(by='Salary', inplace=True, ascending=False)
    result_avg_salary_female = result_avg_salary_female.head(n=6)

    result_avg_salary_male = result_avg_salary_male.reset_index()
    result_avg_salary_male.sort_values(by='Salary', inplace=True, ascending=False)
    result_avg_salary_male = result_avg_salary_male.head(n=6)

    print('*')



    return result_avg_salary_female, result_avg_salary_male






if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')
    print(list(df.columns))

    font_properties = {'fontsize': 22,
                       'weight': 'heavy',
                       'ha': 'center',
                       'alpha': 0.9,
                       'color': 'Gray',
                       'fontname':'Franklin Gothic Medium Cond'
                       }
    res_female, res_male = salary_for_phd_position_separated_by_men_and_women(df)