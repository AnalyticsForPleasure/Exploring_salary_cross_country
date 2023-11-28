import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap # in order to add the gradient color
import seaborn as sns

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
    res_female =  top_phd_position_for_female_jobs.reset_index()
    res_male = top_phd_position_for_male_jobs.reset_index()
    print('*')

    return res_female , res_male

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

    labels_male = list(res_male.loc[:,'Job Title'])
    my_new_labels_male = []

    for current_label in labels_male:
        res = fix_str(current_label)
        my_new_labels_male.append(res)
        print('*')

    #labels_male = res_male.loc[:,'Job Title'] # df.loc[:k, 'pts']
    print('*')
    #['Data\nScientist', 'Research\nScientist', 'Software\nEngineer\nManager', 'Project\nEngineer','Product\nMarketing\nManager', 'Research\nDirector']
    labels_female =res_female.loc[:,'Job Title']
    print('*')
    #['Data\nScientist', 'Research\nScientist', 'Software\nEngineer\nManager', 'Project\nEngineer', 'Product\nMarketing\nManager', 'Research\nDirector']
    Male_PhD = res_male.loc[:,'count']
    Female_PhD = res_female.loc[:,'count']

    x = np.arange(len(labels_female))
    width = 0.5

    plt.figure(figsize=(12, 5))

    plt.subplot(121)
    fontdict_input = {'fontsize': 13, 'weight': 'heavy', 'ha': 'center', 'alpha': 0.9, 'color': 'Gray'}
    plt.title('Types of positions for male with a Ph.D', fontsize=18, fontdict=fontdict_input,
              fontname='Franklin Gothic Medium Cond')
    plt.bar(x - width / 2 + 0.08, Male_PhD, width, label='test1', hatch='^', color=np.array((199, 66, 120)) / 255)
    plt.xticks([0, 1, 2, 3, 4, 5], my_new_labels_male, fontsize=12.5)

    plt.subplot(122)
    plt.title('Types of positions for female with a Ph.D', fontsize=18, fontdict=fontdict_input,
              fontname='Franklin Gothic Medium Cond')
    plt.bar(x - width / 2 + 0.08, Female_PhD, width, hatch='/', color=np.array((199, 199, 92)) / 255)
    plt.xticks([0, 1, 2, 3, 4, 5], labels_female, fontsize=12.5)

    plt.figlegend(loc='upper right', ncol=1, labelspacing=0.4, fontsize=14, bbox_to_anchor=(1.11, 0.9))
    plt.tight_layout(w_pad=6)
    plt.show()






if __name__ == '__main__':
    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')
    print(list(df.columns))

    names_of_races = df['Race'].unique()
    # ['White' 'Hispanic' 'Asian' 'Korean' 'Chinese' 'Australian' 'Welsh', 'African American' 'Mixed' 'Black']
    print(list(names_of_races))

    names_of_countries = df['Country'].unique()
    print(list(names_of_countries))  # ['UK' 'USA' 'Canada' 'China' 'Australia']
    print('*')

    names_of_Job_Title = df['Job Title'].unique()
    # ['Software Engineer' 'Data Analyst' 'Manager' 'Sales Associate' 'Director', 'Marketing Analyst' 'Product Manager'
    # 'Sales Manager', 'Marketing Coordinator' 'Scientist' 'Software Developer' 'HR Manager', 'Financial Analyst'
    # 'Project Manager' 'Customer Servic]
    print(list(
        names_of_Job_Title))
    print('*')

    # groups_by_races = df.groupby('Race')
    # for race, mini_df_by_race in groups_by_races:
    #     print("The race type is: ", race)
    #     print(mini_df_by_race)
    #     print(mini_df_by_race.shape[0])
    #     print('*')
    #
    # data_length = df.shape[0]
    # print('*')



    res_female, res_female =top_phd_position_for_men_and_women(df)
    multi_bar_subplots_chart_for_PhD(res_female ,res_female )
    print('*')
