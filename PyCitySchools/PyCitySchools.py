import pandas as pd
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
Total_Budget = (school_data_complete.groupby("school_name")["budget"].max()).sum()
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
# ----------------------------------------------------------
#import pandas as pd
#from pathlib import Path

# File to Load (Remember to Change These)
#school_data_to_load = Path("Resources/schools_complete.csv")
#student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
#school_data = pd.read_csv(school_data_to_load)
#student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.
#school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
SS_School_Name = school_data_complete.groupby("school_name")['school_name'].unique()
SS_Total_School_Budget = school_data_complete.groupby("school_name")["budget"].max()
SS_Total_students = school_data_complete.groupby("school_name")["size"].count()
SS_School_Type = school_data_complete.groupby("school_name")['type'].agg(max)
SS_Per_Student_Budget = SS_Total_School_Budget/SS_Total_students
SS_Average_Maths_Score = school_data_complete.groupby("school_name")["maths_score"].mean()
SS_Average_Reading_Score = school_data_complete.groupby("school_name")["reading_score"].mean()
SS_Percentage_Maths = (school_data_complete[school_data_complete["maths_score"] >= 50].groupby("school_name")["maths_score"].count()/SS_Total_students)*100
SS_Percentage_Reading = (school_data_complete[school_data_complete["reading_score"] >= 50].groupby("school_name")["reading_score"].count()/SS_Total_students)*100
SS_Overall_Passing = ((school_data_complete.query("maths_score >= 50").query("reading_score >= 50").groupby("school_name")["maths_score"].count())/SS_Total_students)*100

School_Summary_df = pd.DataFrame({"School Type": SS_School_Type, "Total Students": SS_Total_students, "Total School Budget": SS_Total_School_Budget, "Per Student Budget": SS_Per_Student_Budget,
                                            "Average Maths Score": SS_Average_Maths_Score, "Average Reading Score": SS_Average_Reading_Score, "% Passing Maths": SS_Percentage_Maths, "% Passing Reading": SS_Percentage_Reading,
                                            "% Overall Passing": SS_Overall_Passing})


School_Summary_df['Total School Budget'] = School_Summary_df['Total School Budget'].map('${:,.2f}'.format)
School_Summary_df['Per Student Budget'] = School_Summary_df['Per Student Budget'].map('${:,.2f}'.format)
School_Summary_df['Average Maths Score'] = School_Summary_df['Average Maths Score'].map('{:.6f}'.format)
School_Summary_df['Average Reading Score'] = School_Summary_df['Average Reading Score'].map('{:.6f}'.format)
School_Summary_df['% Passing Maths'] = School_Summary_df['% Passing Maths'].map('{:.6f}'.format)
School_Summary_df['% Passing Reading'] = School_Summary_df['% Passing Reading'].map('{:.6f}'.format)
School_Summary_df['% Overall Passing'] = School_Summary_df['% Overall Passing'].map('{:.6f}'.format)

School_Summary_df

#___________________________________________________________________________

Top_Performance_School_df = School_Summary_df.sort_values(["% Overall Passing"], ascending = False).head()

Top_Performance_School_df

#____________________________________________________________________________


Bottom_Performance_School_df = School_Summary_df.sort_values(["% Overall Passing"], ascending = True).head()

Bottom_Performance_School_df