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

    names_of_Job_Title = df['Job Title'].unique()
    print(list(names_of_Job_Title)) # ['Software Engineer' 'Data Analyst' 'Manager' 'Sales Associate' 'Director', 'Marketing Analyst' 'Product Manager' 'Sales Manager', 'Marketing Coordinator' 'Scientist' 'Software Developer' 'HR Manager', 'Financial Analyst' 'Project Manager' 'Customer Servic
    print('*')
    # Classification of  job title:
    # Finance = Financial Manager , Financial Analyst
    # Hi - tech = Engineer , Software Engineer, Software Developer , Data Scientist , Research Scientist , Research director, Principal Scientist, Scientist , Data Analyst , Data Scientist, Full Stack Engineer , Front and Developer, Bank end Developer , director of data Science , Web Developer
    # Marketing = Director of marketing , Marketing Analyst , Marketing Manager, digital Marketing Manager , Content MArketing Manager
    # HR = Human Resources Manager , HR Generalist, HR CoorinatorHR Generalist, HR Coordinator , Receptionist
    # Sales = Sales Associate , Sales Director, Sales Representative, Sales Manager, Customer Service Representative , Sales Executive , Account Manager, Customer Success Rep
    # Operation = Director of Operation, Project Manager , Project Engineer, Operations Manager, Operations Director
    #
    # data = {'job_title': ['Financial Manager', 'Engineer', 'Software Engineer', 'Human Resources Manager',
    #                       'Sales Associate', 'Director of marketing', 'Financial Analyst', 'Data Scientist',
    #                       'Research Scientist', 'Sales Director', 'HR Coordinator', 'Project Manager',
    #                       'Marketing Manager', 'Full Stack Engineer']}
    # df = pd.DataFrame(data)


    # Define mapping of job titles to categories
    job_category_mapping = {
        'Financial Manager': 'Finance',
        'Financial Analyst': 'Finance',
        'Engineer': 'Hi-tech',
        'Software Engineer': 'Hi-tech',
        'Software Developer': 'Hi-tech',
        'Data Scientist': 'Hi-tech',
        'Research Scientist': 'Hi-tech',
        'Research director': 'Hi-tech',
        'Principal Scientist': 'Hi-tech',
        'Scientist': 'Hi-tech',
        'Data Analyst': 'Hi-tech',
        'Full Stack Engineer': 'Hi-tech',
        'Front and Developer': 'Hi-tech',
        'Bank end Developer': 'Hi-tech',
        'director of data Science': 'Hi-tech',
        'Web Developer': 'Hi-tech',
        'Director of marketing': 'Marketing',
        'Marketing Analyst': 'Marketing',
        'Marketing Manager': 'Marketing',
        'Social Media Man': 'Marketing',
        'digital Marketing Manager': 'Marketing',
        'Content Marketing Manager': 'Marketing',
        'Human Resources Manager': 'HR',
        'Juniour HR Coordinator': 'HR',
        'Juniour HR Generalist': 'HR',
        'HR Generalist': 'HR',
        'HR Coordinator': 'HR',
        'Administrative Assistant': 'HR',
        'Receptionist': 'HR',
        'Sales Associate': 'Sales',
        'Sales Director': 'Sales',
        'Customer Service Manager' : 'Sales',
        'Account Manager' : 'Sales',
        'Sales Representative': 'Sales',
        'Sales Manager': 'Sales',
        'Customer Service Representative': 'Sales',
        'Sales Executive': 'Sales',
        'Director of Operation': 'Operation',
        'Project Manager': 'Operation',
        'Project Engineer': 'Operation',
        'Operations Manager': 'Operation',
        'Operations Director': 'Operation'
    }

    # Create a new column 'label' based on the mapping
    df['Job_group'] = df['Job_Title'].map(job_category_mapping)

    # Display the result
    print(df)



    data_length = df.shape[0]
    print('*')

    groups_by_races = df.groupby('Race')
    for race, mini_df_by_race in groups_by_races:
        print("The race type is: ", race)
        print(mini_df_by_race)
        print(mini_df_by_race.shape[0])
        print('*')
