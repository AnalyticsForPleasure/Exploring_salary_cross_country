import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import matthews_corrcoef
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)  # To see all rows
    pd.set_option('display.max_columns', 500)  # To see all columns
    pd.set_option('display.width', 1000)

    df = pd.read_csv('../../data/salary_by_job_country/Salary.csv')
    df_male = df.loc[df['Gender'] == 'Male', :]
    # encode = LabelEncoder()
    # df_male["encoded_jobtitle"] = encode.fit_transform(df_male["Job Title"])
    # groups = df.groupby('Job Title')
    print(f'{len(df_male["Job Title"].unique())}')
    print(f'{len(df_male["Education Level"].unique())}')
    columns_names = df_male["Education Level"].unique()
    rows_names = df_male["Job Title"].unique()

    matrix = pd.DataFrame(data=np.zeros((96, 4)),
                          index=rows_names,
                          # columns=['Highschool', 'Bsc', 'Master', 'PhD'],
                          dtype=int)

    for idx, current_row in df_male.iterrows():
        matrix.loc[current_row['Job Title'], current_row['Education Level']] += 1
    print('*')

    old_names = [0, 1, 2, 3]
    new_names = ['Highschool', 'Bsc', 'Master', 'PhD']
    matrix.rename(columns=dict(zip(old_names, new_names)), inplace=True)

    ax = sns.heatmap(
        matrix,
        vmin=0, vmax=matrix.to_numpy().max(), center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=False
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    )

    plt.show()
    # corr = df_male.loc[:,["encoded_jobtitle", "Education Level"]].corr()
    # print(corr)

    # ax = sns.heatmap(
    #     corr,
    #     vmin=-1, vmax=1, center=0,
    #     cmap=sns.diverging_palette(20, 220, n=200),
    #     square=True
    # )
    # ax.set_xticklabels(
    #     ax.get_xticklabels(),
    #     rotation=45,
    #     horizontalalignment='right'
    # );
