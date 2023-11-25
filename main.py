import pandas as pd
import numpy as np

# Datasets:
# https://www.kaggle.com/datasets/amirmahdiabbootalebi/salary-by-job-title-and-country
# https://www.kaggle.com/datasets/lorenzovzquez/data-jobs-salaries
# https://www.kaggle.com/datasets/aijobs/global-salaries-in-ai-ml-data-science
# https://www.kaggle.com/datasets/andrewmvd/data-analyst-jobs


if __name__ == '__main__':
    df = pd.read_csv('data/salary_by_job_country/Salary.csv')
    print(list(df.columns))

    names_of_races = df['Race'].unique()
    print(list(
        names_of_races))  # ['White' 'Hispanic' 'Asian' 'Korean' 'Chinese' 'Australian' 'Welsh', 'African American' 'Mixed' 'Black']

    names_of_countries = df['Country'].unique()
    print(list(names_of_countries))  # ['UK' 'USA' 'Canada' 'China' 'Australia']
    print('*')

    data_length = df.shape[0]
    print('*')

    groups_by_races = df.groupby('Race')
    for race, mini_df_by_race in groups_by_races:
        print("The race type is: ", race)
        print(mini_df_by_race)
        print(mini_df_by_race.shape[0])
        print('*')
