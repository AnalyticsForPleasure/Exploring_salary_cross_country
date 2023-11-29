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
# Function  name: fix_str- helper function
# input:
# return value:
# ***************************************************************************************************************
def fix_str(my_label):
    pos = my_label.find(' ')
    final_str = my_label[:pos] + '\n' + my_label[pos:]
    return final_str


# **************************************************************************************************************
# Function  name: multi_bar_plot_chart_for_PhD
# input:
# return value:
# ***************************************************************************************************************
def multi_bar_subplots_chart_for_PhD(res_female, res_male):
    # plt.style.use('seaborn')  # This line is responsible for the gray background
    labels_male = list(res_male.loc[:, 'Job Title'])
    labels_female = list(res_female.loc[:, 'Job Title'])
    print('*')
    my_new_labels_male = []
    my_new_labels_female = []

    for current_label in labels_male:
        res = fix_str(current_label)
        my_new_labels_male.append(res)
        print('*')

    for current_label in labels_female:
        res = fix_str(current_label)
        my_new_labels_female.append(res)
        print('*')

    Male_PhD = res_male.loc[:, 'count']
    Female_PhD = res_female.loc[:, 'count']
    print('*')

    x = np.arange(len(labels_female))
    width = 0.8

    fontdict_input = {'fontsize': 13, 'weight': 'heavy', 'ha': 'center', 'alpha': 0.9, 'color': 'Gray'}

    fig, axes = plt.subplots(1, 2, sharex=True, figsize=(10, 5))
    fig.suptitle('PhD Position Gender Comparison in the High-Tech Industry', fontdict=fontdict_input, fontsize=22,
                 fontname='Franklin Gothic Medium Cond')

    # Chart number 1 - Male
    axes[0].set_title('Types of positions for male with a Ph.D', fontsize=18, fontdict=fontdict_input,
                      fontname='Franklin Gothic Medium Cond')
    axes[0].bar(x - width / 2 + 0.08, Male_PhD, width, label='test1', color='cornflowerblue')
    axes[0].set_xticks([0, 1, 2, 3, 4, 5], my_new_labels_male, fontsize=12.5)

    # Chart number 2 - Female
    axes[1].set_title('Types of positions for female with a Ph.D', fontsize=18, fontdict=fontdict_input,
                      fontname='Franklin Gothic Medium Cond')
    axes[1].bar(x - width / 2 + 0.08, Female_PhD, width, color='navy')
    axes[1].set_xticks([0, 1, 2, 3, 4, 5], my_new_labels_female, fontsize=12.5)
    # axes[1].text(x=1, y=0.5, s='F', ha='left', va='bottom', fontdict=fontdict_input)

    plt.figlegend(loc='upper right', ncol=1, labelspacing=0.4, fontsize=14, bbox_to_anchor=(1.11, 0.9))
    plt.tight_layout(w_pad=6)
    plt.show()


def break_into_separate_word(labels):
    separate_words_for_each_label = []
    for label in labels:
        separate_words_per_label = '\n'.join(label.split())
        separate_words_for_each_label.append(separate_words_per_label)

    return separate_words_for_each_label


def add_numbers_to_plots(values, ax, idx_gender):
    # Add numbers on top of the bars
    for i, value in enumerate(values):
        ax[idx_gender].text(i, value + 0.1, str(value), ha='center', va='bottom')


def multi_bar_subplots_chart_for_PhD2(res_female, res_male):
    fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(16, 9))
    data_per_gender = {'female': res_female, 'male': res_male}
    colors = {'female': 'lightpink', 'male': 'lightblue'}

    for idx, gender in enumerate(['female', 'male']):
        gender_phd_count = data_per_gender[gender].loc[:, 'count']
        gender_labels = list(res_male.loc[:, 'Job Title'])
        ax[idx].bar(break_into_separate_word(gender_labels), gender_phd_count, color=colors[gender], width=0.9)
        ax[idx].set_title(gender.upper())

        add_numbers_to_plots(gender_phd_count, ax, idx_gender=idx)

    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')
    print(list(df.columns))

    res_female, res_male = top_phd_position_for_men_and_women(df)
    res = pd.concat([res_male, res_female], axis=1)
    multi_bar_subplots_chart_for_PhD2(res_female, res_male)
    print('*')
