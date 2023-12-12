import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sys
import matplotlib.ticker as mticker
import locale

from matplotlib.colors import LinearSegmentedColormap  # in order to add the gradient color


# **************************************************************************************************************
# Function  name: break_into_separate_word
# input:
# return value:
# ***************************************************************************************************************
def break_into_separate_word(labels):
    separate_words_for_each_label = []
    for label in labels:
        separate_words_per_label = '\n'.join(label.split())
        separate_words_for_each_label.append(separate_words_per_label)

    return separate_words_for_each_label

# **************************************************************************************************************
# Function  name: add_numbers_to_plots
# input:
# return value:
# ***************************************************************************************************************
def add_numbers_for_each_bar_chart(values, ax, idx_gender):
    # Add numbers on top of the bars
    for i, value in enumerate(values):

        ax[idx_gender].text(i, value + 0.1, str(value), ha='center', va='bottom', fontname='Franklin Gothic Medium Cond')
        print('*')


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
    result_avg_salary_female['Salary'] = result_avg_salary_female['Salary'].apply(lambda x: int(x))
    #result_avg_salary_female['Salary'] = result_avg_salary_female['Salary'].apply(lambda x: "{:,}".format(x))
    print('*')
    result_avg_salary_male = result_avg_salary_male.reset_index()
    result_avg_salary_male.sort_values(by='Salary', inplace=True, ascending=False)
    result_avg_salary_male = result_avg_salary_male.head(n=6)
    result_avg_salary_male['Salary'] = result_avg_salary_male['Salary'].apply(lambda x: int(x))
    #result_avg_salary_male['Salary'] = result_avg_salary_male['Salary'].apply(lambda x: "{:,}".format(x))
    print('*')

    print('*')
    return result_avg_salary_female, result_avg_salary_male


# **************************************************************************************************************
# Function name: multi_bar_subplots_chart_for_PhD
# input:
# return value:
# ***************************************************************************************************************
def multi_bar_subplots_chart_Avg_salary_for_PhD(result_avg_salary_female, result_avg_salary_male, font_prop):
    fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(16, 9))
    data_per_gender = {'female': result_avg_salary_female, 'male': result_avg_salary_male}
    colors = {'female': 'lightpink', 'male': 'lightblue'}

    fig.suptitle('Comparing the average salary for Ph.D. positions in the High-Tech Industry by gender',
                 fontsize=font_prop['fontsize'],
                 fontname=font_prop['fontname'],
                 color='Black')




    for idx, gender in enumerate(['female', 'male']):
        gender_phd_count = data_per_gender[gender].loc[:, 'Salary']
        gender_labels = list(result_avg_salary_male.loc[:, 'Job Title'])
        ax[idx].set_title(f'Average salary for positions open to {gender} with a Ph.D', fontsize=18, fontdict=font_prop,
                          fontname=font_prop['fontname'])
        ax[idx].bar(break_into_separate_word(gender_labels), gender_phd_count, color=colors[gender], width=0.9)

        add_numbers_for_each_bar_chart(gender_phd_count, ax, idx_gender=idx)
        plt.savefig('Gender Comparison by Salary.jpg', dpi=250, bbox_inches='tight')
    plt.show()



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
    result_avg_salary_female, result_avg_salary_male = salary_for_phd_position_separated_by_men_and_women(df)
    multi_bar_subplots_chart_Avg_salary_for_PhD(result_avg_salary_female, result_avg_salary_male, font_properties)
    print('*')