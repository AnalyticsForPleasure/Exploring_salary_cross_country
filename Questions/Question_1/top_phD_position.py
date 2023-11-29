import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sys
from matplotlib.colors import LinearSegmentedColormap  # in order to add the gradient color


# Datasets:
# https://www.kaggle.com/datasets/amirmahdiabbootalebi/salary-by-job-title-and-country
# https://www.kaggle.com/datasets/lorenzovzquez/data-jobs-salaries
# https://www.kaggle.com/datasets/aijobs/global-salaries-in-ai-ml-data-science
# https://www.kaggle.com/datasets/andrewmvd/data-analyst-jobs

# **************************************************************************************************************
# Function  name: top_phd_position_for_men_and_women
# input:
# return value:
# ****************************************************************************************************************
def top_phd_position_for_men_and_women(df):
    # In the hi-tech industry, what types of positions do individuals with a Ph.D. typically hold? ( Male  Vs Female )
    phd_users = df.loc[(df['Education Level'] == 3)]
    phd_female = phd_users.loc[(df['Gender'] == 'Female')]  # Female
    phd_male = phd_users.loc[(df['Gender'] == 'Male')]  # Male
    top_phd_position_for_female_jobs = phd_female['Job Title'].value_counts().head(n=6)
    top_phd_position_for_male_jobs = phd_male['Job Title'].value_counts().head(n=6)
    res_female = top_phd_position_for_female_jobs.reset_index()
    res_male = top_phd_position_for_male_jobs.reset_index()
    print('*')

    return res_female, res_male

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
        ax[idx_gender].text(i, value + 0.1, str(value), ha='center', va='bottom',fontname='Franklin Gothic Medium Cond' )

# **************************************************************************************************************
# Function  name: multi_bar_subplots_chart_for_PhD2
# input:
# return value:
# ***************************************************************************************************************
def multi_bar_subplots_chart_for_PhD2(res_female, res_male):

    fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(16, 9))
    data_per_gender = {'female': res_female, 'male': res_male}
    colors = {'female': 'lightpink', 'male': 'lightblue'}
    fontdict_input = {'fontsize': 13, 'weight': 'heavy', 'ha': 'center', 'alpha': 0.9, 'color': 'Gray'}

    fig.suptitle('PhD Position Gender Comparison in the High-Tech Industry', fontdict=fontdict_input, fontsize=22, fontname='Franklin Gothic Medium Cond')

    for idx, gender in enumerate(['female', 'male']):

        gender_phd_count = data_per_gender[gender].loc[:, 'count']
        gender_labels = list(res_male.loc[:, 'Job Title'])
        ax[idx].set_title(f'Types of positions for {gender} with a Ph.D', fontsize=18, fontdict=fontdict_input,fontname='Franklin Gothic Medium Cond')
        ax[idx].bar(break_into_separate_word(gender_labels), gender_phd_count, color=colors[gender], width=0.9 )


        add_numbers_for_each_bar_chart(gender_phd_count, ax, idx_gender=idx)
        plt.savefig('Gender Comparison.jpg', dpi=250, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')
    print(list(df.columns))

    res_female, res_male = top_phd_position_for_men_and_women(df)
    #res = pd.concat([res_male, res_female], axis=1)
    multi_bar_subplots_chart_for_PhD2(res_female, res_male)
    print('*')
