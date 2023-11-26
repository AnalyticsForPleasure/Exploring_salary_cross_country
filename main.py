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


    # In the hi-tech industry, what types of positions do individuals with a Ph.D. typically hold? ( Male  Vs Female )

    res =df.loc[(df['Education Level'] == 3) & (df['Gender']=='Male')] # Female
    final_result =res['Job Title'].value_counts()

    print('*')

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
    # Finance = Financial Manager , Financial Analyst , Accountant
    # Hi - tech = Engineer , Software Engineer, Software Developer , Data Scientist , Research Scientist , Research director, Principal Scientist, Scientist , Data Analyst , Data Scientist, Full Stack Engineer , Front and Developer, Bank end Developer , director of data Science , Web Developer , IT Support, UX Designer, Network Enineer, help desk analyst, Graphic Designer, Web Developer, Chief Technology Officer, Chief  Data Officer, IT Support SpecialistPrecipal Engineer, Director of Product Managemnet
    # Marketing = Director of marketing , Marketing Analyst , Marketing Manager, digital Marketing Manager , Content Marketing Manager, Social Media Specialist, Product Designer , Marketing Coordinator, Creative Director, Business Analyst, Public Relations Manager
    # HR = Human Resources Manager , HR Generalist, HR Coordinator , Receptionist , Director , HR Manager, data entry clerk , Recruiter, Administrative Assistant, Office Manager, Training Specialist, Director of Human Resources, Human Resources Manager , Direcotor of Human Capital
    # Sales = Sales Associate , Sales Director, Sales Representative, Sales Manager, Customer Service Representative , Sales Executive , Account Manager, Customer Success Rep, Customer Service Rep,
    # Operation = Director of Operation, Project Manager , Project Engineer, Operations Manager, Operations Director , VP of Operations , Sales Operation Manager, Supply Chain Manager, Operations Analyst, Project Coodunator , Supply Chain Analyst ,

    # Define mapping of job titles to categories
    job_category_mapping = {
        'Financial Manager': 'Finance',
        'Financial Analyst': 'Finance',
        'Accountant': 'Finance',
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
        'IT Support': 'Hi-tech',
        'UX Designer': 'Hi-tech',
        'Network Engineer': 'Hi-tech',
        'Help Desk Analyst': 'Hi-tech',
        'Graphic Designer': 'Hi-tech',
        'Chief Technology Officer': 'Hi-tech',
        'Chief Data Officer': 'Hi-tech',
        'IT Support Specialist': 'Hi-tech',
        'Principal Engineer': 'Hi-tech',
        'Director of Product Management': 'Hi-tech',
        'Director of marketing': 'Marketing',
        'Marketing Analyst': 'Marketing',
        'Marketing Manager': 'Marketing',
        'Digital Marketing Manager': 'Marketing',
        'Content Marketing Manager': 'Marketing',
        'Social Media Specialist': 'Marketing',
        'Product Designer': 'Marketing',
        'Marketing Coordinator': 'Marketing',
        'Creative Director': 'Marketing',
        'Business Analyst': 'Marketing',
        'Public Relations Manager': 'Marketing',
        'Human Resources Manager': 'HR',
        'HR Generalist': 'HR',
        'HR Coordinator': 'HR',
        'Receptionist': 'HR',
        'Director': 'HR',
        'HR Manager': 'HR',
        'Data Entry Clerk': 'HR',
        'Recruiter': 'HR',
        'Administrative Assistant': 'HR',
        'Office Manager': 'HR',
        'Training Specialist': 'HR',
        'Director of Human Resources': 'HR',
        'Human Resources Manager': 'HR',
        'Director of Human Capital': 'HR',
        'Sales Associate': 'Sales',
        'Sales Director': 'Sales',
        'Sales Representative': 'Sales',
        'Sales Manager': 'Sales',
        'Customer Service Representative': 'Sales',
        'Sales Executive': 'Sales',
        'Account Manager': 'Sales',
        'Customer Success Rep': 'Sales',
        'Customer Service Rep': 'Sales',
        'Director of Operation': 'Operation',
        'Project Manager': 'Operation',
        'Project Engineer': 'Operation',
        'Operations Manager': 'Operation',
        'Operations Director': 'Operation',
        'VP of Operations': 'Operation',
        'Sales Operation Manager': 'Operation',
        'Supply Chain Manager': 'Operation',
        'Operations Analyst': 'Operation',
        'Project Coordinator': 'Operation',
        'Supply Chain Analyst': 'Operation'
    }

    # Create a new column 'label' based on the mapping
    df['Job_group'] = df['Job_Title'].map(job_category_mapping)

    # Display the result
    print(df)


    groups_by_races = df.groupby('Race')
    for race, mini_df_by_race in groups_by_races:
        print("The race type is: ", race)
        print(mini_df_by_race)
        print(mini_df_by_race.shape[0])
        print('*')


    data_length = df.shape[0]
    print('*')

    groups_by_races = df.groupby('Race')
    for race, mini_df_by_race in groups_by_races:
        print("The race type is: ", race)
        print(mini_df_by_race)
        print(mini_df_by_race.shape[0])
        print('*')
