import numpy as np, pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
Total_Schools = len(school_data_complete["school_name"].unique())
Total_Students = len(school_data_complete["student_name"])
Total_Budget = (pd.pivot_table(school_data_complete, values='budget', index='School ID', aggfunc = np.max)).sum()[0] # Reference for pivot_table: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html
Average_Maths_Score = school_data_complete["maths_score"].mean()
Average_Reading_Score = school_data_complete["reading_score"].mean()
Percentage_Maths = (((school_data_complete["maths_score"] >= 50).value_counts()[0])/Total_Students)*100
Percentage_Reading =(((school_data_complete["reading_score"] >= 50).value_counts()[0])/Total_Students)*100
Overall_Passing = (((school_data_complete[["maths_score","reading_score"]] >= 50).value_counts()[0])/Total_Students)*100

LGA_Summary_df = pd.DataFrame({
                            "Total Schools"        : Total_Schools,
                            "Total Students"       : Total_Students,
                            "Total Budget"         : Total_Budget,
                            "Average Maths Score"  : Average_Maths_Score,
                            "Average Reading Score": Average_Reading_Score,
                            "% Passing Maths"      : Percentage_Maths,
                            "% Passing Reading"    : Percentage_Reading,
                            "% Overall Passing"    : Overall_Passing
                               }, index=[0])

LGA_Summary_df['Total Students'] = LGA_Summary_df['Total Students'].map('{:,}'.format)
LGA_Summary_df['Total Budget'] = LGA_Summary_df['Total Budget'].map('${:,.2f}'.format)
LGA_Summary_df['Average Maths Score'] = LGA_Summary_df['Average Maths Score'].map('{:.6f}'.format)
LGA_Summary_df['Average Reading Score'] = LGA_Summary_df['Average Reading Score'].map('{:.6f}'.format)
LGA_Summary_df['% Passing Maths'] = LGA_Summary_df['% Passing Maths'].map('{:.6f}'.format)
LGA_Summary_df['% Passing Reading'] = LGA_Summary_df['% Passing Reading'].map('{:.6f}'.format)
LGA_Summary_df['% Overall Passing'] = LGA_Summary_df['% Overall Passing'].map('{:.6f}'.format)

LGA_Summary_df