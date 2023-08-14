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

School_Summary_df.index.name = ''
School_Summary_df['Total School Budget'] = School_Summary_df['Total School Budget'].map('${:,.2f}'.format)
School_Summary_df['Per Student Budget'] = School_Summary_df['Per Student Budget'].map('${:,.2f}'.format)
School_Summary_df['Average Maths Score'] = School_Summary_df['Average Maths Score'].map('{:.6f}'.format)
School_Summary_df['Average Reading Score'] = School_Summary_df['Average Reading Score'].map('{:.6f}'.format)
School_Summary_df['% Passing Maths'] = School_Summary_df['% Passing Maths'].map('{:.6f}'.format)
School_Summary_df['% Passing Reading'] = School_Summary_df['% Passing Reading'].map('{:.6f}'.format)
School_Summary_df['% Overall Passing'] = School_Summary_df['% Overall Passing'].map('{:.6f}'.format)

School_Summary_df

#___________________________________________________________

Top_Performance_School_df = School_Summary_df.sort_values(["% Overall Passing"], ascending = False).head()
Top_Performance_School_df

#___________________________________________________________


Bottom_Performance_School_df = School_Summary_df.sort_values(["% Overall Passing"], ascending = True).head()
Bottom_Performance_School_df

#______________________________________________________________________

MYear_9 = school_data_complete.query("year == 9").groupby("school_name")["maths_score"].mean()
MYear_10 = school_data_complete.query("year == 10").groupby("school_name")["maths_score"].mean()
MYear_11 = school_data_complete.query("year == 11").groupby("school_name")["maths_score"].mean()
MYear_12 = school_data_complete.query("year == 12").groupby("school_name")["maths_score"].mean()

Maths_Score_Year_df = pd.DataFrame({"Year 9": MYear_9, "Year 10": MYear_10, "Year 11": MYear_11, "Year 12": MYear_12})

Maths_Score_Year_df.index.name = ''
Maths_Score_Year_df['Year 9'] = Maths_Score_Year_df['Year 9'].map('{:.6f}'.format)
Maths_Score_Year_df['Year 10'] = Maths_Score_Year_df['Year 10'].map('{:.6f}'.format)
Maths_Score_Year_df['Year 11'] = Maths_Score_Year_df['Year 11'].map('{:.6f}'.format)
Maths_Score_Year_df['Year 12'] = Maths_Score_Year_df['Year 12'].map('{:.6f}'.format)

Maths_Score_Year_df

#______________________________________________________________________

RYear_9 = school_data_complete.query("year == 9").groupby("school_name")["reading_score"].mean()
RYear_10 = school_data_complete.query("year == 10").groupby("school_name")["reading_score"].mean()
RYear_11 = school_data_complete.query("year == 11").groupby("school_name")["reading_score"].mean()
RYear_12 = school_data_complete.query("year == 12").groupby("school_name")["reading_score"].mean()

Reading_Score_Year_df = pd.DataFrame({"Year 9": RYear_9, "Year 10": RYear_10, "Year 11": RYear_11, "Year 12": RYear_12})

Reading_Score_Year_df.index.name = ''
Reading_Score_Year_df['Year 9'] = Reading_Score_Year_df['Year 9'].map('{:.6f}'.format)
Reading_Score_Year_df['Year 10'] = Reading_Score_Year_df['Year 10'].map('{:.6f}'.format)
Reading_Score_Year_df['Year 11'] = Reading_Score_Year_df['Year 11'].map('{:.6f}'.format)
Reading_Score_Year_df['Year 12'] = Reading_Score_Year_df['Year 12'].map('{:.6f}'.format)

Reading_Score_Year_df

#___________________________________________________________________________

spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]

School_Summary_df['Average Maths Score'] = School_Summary_df['Average Maths Score'].astype("float64", copy=None, errors='raise')
School_Summary_df['Average Reading Score'] = School_Summary_df['Average Reading Score'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Passing Maths'] = School_Summary_df['% Passing Maths'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Passing Reading'] = School_Summary_df['% Passing Reading'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Overall Passing'] = School_Summary_df['% Overall Passing'].astype("float64", copy=None, errors='raise')

School_Summary_df["Spending Ranges (Per Student)"] = pd.cut(SS_Per_Student_Budget, bins = spending_bins, labels=labels)
spending_math_scores = School_Summary_df.groupby(["Spending Ranges (Per Student)"])["Average Maths Score"].mean()
spending_reading_scores = School_Summary_df.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = School_Summary_df.groupby(["Spending Ranges (Per Student)"])["% Passing Maths"].mean()
spending_passing_reading = School_Summary_df.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = School_Summary_df.groupby(["Spending Ranges (Per Student)"])["% Overall Passing"].mean()

School_Spending_df= pd.DataFrame({"Average Maths Score":spending_math_scores, "Average Reading Score": spending_reading_scores, "% Passing Maths": spending_passing_math,
                                  "% Passing Reading": spending_passing_reading, "% Overall Passing":overall_passing_spending}, index = labels)

School_Spending_df.index.name = 'Spending Ranges (Per Student)'
School_Spending_df['Average Maths Score'] = School_Spending_df['Average Maths Score'].map('{:.2f}'.format)
School_Spending_df['Average Reading Score'] = School_Spending_df['Average Reading Score'].map('{:.2f}'.format)
School_Spending_df['% Passing Maths'] = School_Spending_df['% Passing Maths'].map('{:.2f}'.format)
School_Spending_df['% Passing Reading'] = School_Spending_df['% Passing Reading'].map('{:.2f}'.format)
School_Spending_df['% Overall Passing'] = School_Spending_df['% Overall Passing'].map('{:.2f}'.format)

School_Spending_df

#_____________________________________________________________________________________________________________________

school_size = [0, 1000, 2000, 5000]
labels = ["Small(<1000)", "Medium(1000-2000)", "Large(2000-5000)"]

School_Summary_df['Average Maths Score'] = School_Summary_df['Average Maths Score'].astype("float64", copy=None, errors='raise')
School_Summary_df['Average Reading Score'] = School_Summary_df['Average Reading Score'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Passing Maths'] = School_Summary_df['% Passing Maths'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Passing Reading'] = School_Summary_df['% Passing Reading'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Overall Passing'] = School_Summary_df['% Overall Passing'].astype("float64", copy=None, errors='raise')

School_Summary_df["Score by School size"] = pd.cut(SS_Total_students, bins = school_size, labels=labels)
school_size_math_scores = School_Summary_df.groupby(["Score by School size"])["Average Maths Score"].mean()
school_size_reading_scores = School_Summary_df.groupby(["Score by School size"])["Average Reading Score"].mean()
school_size_passing_maths = School_Summary_df.groupby(["Score by School size"])["% Passing Maths"].mean()
school_size_passing_reading = School_Summary_df.groupby(["Score by School size"])["% Passing Reading"].mean()
school_size_overall_passing = School_Summary_df.groupby(["Score by School size"])["% Overall Passing"].mean()

Scores_School_Size_df = pd.DataFrame({"Average Maths Score":school_size_math_scores, "Average Reading Score": school_size_reading_scores, "% Passing Maths": school_size_passing_maths,
                                  "% Passing Reading": school_size_passing_reading, "% Overall Passing":school_size_overall_passing}, index = labels)

Scores_School_Size_df.index.name = 'School Size'
Scores_School_Size_df['Average Maths Score'] = Scores_School_Size_df['Average Maths Score'].map('{:.6f}'.format)
Scores_School_Size_df['Average Reading Score'] = Scores_School_Size_df['Average Reading Score'].map('{:.6f}'.format)
Scores_School_Size_df['% Passing Maths'] = Scores_School_Size_df['% Passing Maths'].map('{:.6f}'.format)
Scores_School_Size_df['% Passing Reading'] = Scores_School_Size_df['% Passing Reading'].map('{:.6f}'.format)
Scores_School_Size_df['% Overall Passing'] = Scores_School_Size_df['% Overall Passing'].map('{:.6f}'.format)

Scores_School_Size_df
#______________________________________________________________________________________________________________________

labels = School_Summary_df["School Type"].unique()
School_Summary_df['Average Maths Score'] = School_Summary_df['Average Maths Score'].astype("float64", copy=None, errors='raise')
School_Summary_df['Average Reading Score'] = School_Summary_df['Average Reading Score'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Passing Maths'] = School_Summary_df['% Passing Maths'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Passing Reading'] = School_Summary_df['% Passing Reading'].astype("float64", copy=None, errors='raise')
School_Summary_df['% Overall Passing'] = School_Summary_df['% Overall Passing'].astype("float64", copy=None, errors='raise')

school_type_math_scores = School_Summary_df.groupby(["School Type"])["Average Maths Score"].mean()
school_type_reading_scores = School_Summary_df.groupby(["School Type"])["Average Reading Score"].mean()
school_type_passing_maths = School_Summary_df.groupby(["School Type"])["% Passing Maths"].mean()
school_type_passing_reading = School_Summary_df.groupby(["School Type"])["% Passing Reading"].mean()
school_type_overall_passing = School_Summary_df.groupby(["School Type"])["% Overall Passing"].mean()

Scores_School_Type_df = pd.DataFrame({"Average Maths Score":school_type_math_scores, "Average Reading Score": school_type_reading_scores, "% Passing Maths": school_type_passing_maths,
                                  "% Passing Reading": school_type_passing_reading, "% Overall Passing":school_type_overall_passing}, index = labels)

Scores_School_Type_df.index.name = 'School Type'
Scores_School_Type_df['Average Maths Score'] = Scores_School_Type_df['Average Maths Score'].map('{:.6f}'.format)
Scores_School_Type_df['Average Reading Score'] = Scores_School_Type_df['Average Reading Score'].map('{:.6f}'.format)
Scores_School_Type_df['% Passing Maths'] = Scores_School_Type_df['% Passing Maths'].map('{:.6f}'.format)
Scores_School_Type_df['% Passing Reading'] = Scores_School_Type_df['% Passing Reading'].map('{:.6f}'.format)
Scores_School_Type_df['% Overall Passing'] = Scores_School_Type_df['% Overall Passing'].map('{:.6f}'.format)

Scores_School_Type_df

#_________________________________________________________________________________________________________________________