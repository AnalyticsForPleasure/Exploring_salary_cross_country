import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def creating_distribution_for_age_and_experience(df, font_prop):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
    # Chart 1:
    sns.histplot(df["Age"], kde=True, ax=axs[0])
    axs[0].set_title("Age Distribution" ,fontname = font_prop['fontname'], fontsize=  font_prop['fontsize'])
    # Chart 2: :
    sns.histplot(df["Years of Experience"], kde=True, ax=axs[1])
    axs[1].set_title("Years of Experience Distribution",fontname = font_prop['fontname'], fontsize=  font_prop['fontsize'])
    plt.ylabel('Number of times with the same years experience')
    plt.tight_layout()

    plt.savefig('Distribution_by_Age_and_Experience.jpg', dpi=250, bbox_inches='tight')
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


    creating_distribution_for_age_and_experience(df,font_properties)
    print('*')

