import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# **************************************************************************************************************
# Function  name: format_with_commas
# input:
# return value:
# ****************************************************************************************************************
def format_with_commas(value, pos):
    return f'{value:,.0f}'
# **************************************************************************************************************
# Function  name: creating_a_distributed_dot_plot_for_each_department
# input:
# return value:
# ****************************************************************************************************************
def creating_a_distributed_dot_plot_for_each_department(df_raw, font_prop):
    # Mean and Median
    df = df_raw[['Salary', 'Job Title']].groupby('Job Title').apply(lambda x: x.mean())
    df.sort_values('Salary', ascending=False, inplace=True)
    df.reset_index(inplace=True)
    print('*')

    # Draw horizontal lines
    fig, ax = plt.subplots(figsize=(16, 9), dpi=80)
    ax.hlines(y=df.index, xmin=0, xmax=df['Salary'].max(), color='gray', alpha=0.5, linewidth=.7, linestyles='dashdot')
    ax.tick_params(labelleft=True, labelright=False, left=True, right=False)
    # Draw the Dots
    df_raw.sort_values(by=['Salary'], inplace=True)
    groups = df_raw.groupby(['Job Title'])
    for idx, (group_name, mini_df) in enumerate(groups):
        num_circles_per_job_title = mini_df.shape[0]
        median_salary_for_each_group = mini_df['Salary'].median()
        ax.scatter(y=np.repeat(idx, num_circles_per_job_title),  # position over the y-axis
                   x=mini_df['Salary'],  # position over the x-axis
                   s=125,
                   edgecolors='gray', c='lightblue', alpha=0.8)
        ax.scatter(y=idx, x=median_salary_for_each_group, s=125, c='mediumblue', alpha=0.6)

    ax.xaxis.set_major_formatter(FuncFormatter(format_with_commas))

    ax.text(180000, 10, "$Blue \; dots \; are \; the \: median$", fontdict={'size': 12}, c='blue',
            fontname=font_prop['fontname'])

    # Decorations
    lightblue_patch = plt.plot([], [], marker="o", ms=10, ls="", mec=None, color='mediumblue', label="Median")
    plt.legend(handles=lightblue_patch)
    ax.set_title('Salary distribution across HR positions',fontdict={'size': 50}, fontsize=font_prop['fontsize'],
                 fontname=font_prop['fontname'])
    ax.set_xlabel('Salary - In U.S dollars ( $ )', alpha=0.7, fontsize=22, fontname=font_prop['fontname'])
    ax.set_yticks(df.index)
    ax.set_yticklabels(df['Job Title'].str.title(), alpha=0.7, fontname=font_prop['fontname'], fontsize=15)
    ax.set_xlim(1, df['Salary'].max() + 2000)
    plt.xticks(alpha=0.7)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.grid(axis='both', alpha=.4, linewidth=.1)

    plt.savefig('Salary_distribution_across_positions.jpg', dpi=250, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    df_raw = pd.read_csv(
        '/home/shay_diy/PycharmProjects/Exploring_salary_cross_country/data/salary_by_job_country/hr.csv')
    font_properties = {'fontsize': 32,
                       'weight': 'heavy',
                       'ha': 'center',
                       'alpha': 0.9,
                       'color': 'Gray',
                       'fontname': 'Franklin Gothic Medium Cond'
                       }

    creating_a_distributed_dot_plot_for_each_department(df_raw, font_properties)




