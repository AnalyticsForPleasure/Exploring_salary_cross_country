import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('/home/shay_diy/PycharmProjects/Exploring_salary_cross_country/data/salary_by_job_country/Salary.csv')
    print('*')

    relevent_data = df.loc[(df['Gender'] == 'Female') & (df['Education Level'] == 1)]
    print('*')
    relevent_data = relevent_data.loc[:, ['Salary', 'Race']]
    relevent_data_by_race = relevent_data.groupby('Race').mean().reset_index()
    relevent_data_by_race = relevent_data_by_race.sort_values('Salary', ascending=False)

    #plt.scatter(df['Race'], df['Salary'])
    sns.stripplot(y="Salary", x="Race", data=relevent_data)
    # Plot lines for the average
    sns.scatterplot(y="Salary", x="Race", data=relevent_data_by_race, marker='|', s=1000, color='k')
    plt.show()
    print('*')
    #                          df.loc[(df[team_abbreviation’] == 'LAL') & (df['pts'] > 30)]
    #
    # grouping_by_gender = df.groupby('Gender')
    # for gender, mini_df_gender in grouping_by_gender:
    #     print("Gender :",  gender)
    #     print(mini_df_gender)
    #     mini_df_gender.shape[0] # Female 6,684
    #     under_2_constrains= mini_df_gender.loc[mini_df_gender['Education Level'] == 1] # men of women with a bachelor degree - 1198 rows
    #     print('*')



        # gouping_by_race = under_2_constrains.groupby('Race')
        # for race , mini_df_race in gouping_by_race:
        #     print("Race :", race)
        #     print(mini_df_race)
        #     mean_by_group  = mini_df_race['Salary'].mean()
        #     #mini_df_race.shape[0]
        #     print(mean_by_group)
        #     print('*')





        # print('*')

        # groups_by_Country = df.groupby('Country')
        # for Country, mini_df_by_Country in groups_by_Country:
        #     print("The Country name : ", Country)
        #     print(mini_df_by_Country)
        #     print(mini_df_by_Country.shape[0])
        #     res = mini_df_by_Country['Race'].value_counts()
        #     print('*')


