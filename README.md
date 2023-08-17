# Pandas_Challenge
## Analysis Summary

This section briefly explains coding used for analysis of budget and percentage achieved by students in an local government area.

### Local Government Area:

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/47dfeaec-9d1c-47da-8525-3d72d2d010ab)

In section performance of all the schools located in the local Government area are analysed. The combined school and student data is considered as base data. In order to obtain the required data statical analysis (mean, max , sum ) were performed on the various columns of the combined data and resulting panda series were initially combined into a dataframe. The columns were formated using the .map() function of Dataframe.  

### School Summary:

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/86091e42-2590-4b3f-8815-41c3c9f95b72)

In section performance of each school is analysed. The combined school and student data is considered as base data. In order to obtain the required data statical analysis (mean, max , sum ) were performed on the various columns of the combined data and also by grouping the data with *school name*. The resulting panda series were initially combined into a dataframe. The columns were formated using the .map() function of Dataframe.

### Top and Bottom Performing Schools:

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/f1359b5a-3d0c-4748-a580-3584f25c15a2)

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/ae390e14-2448-4f27-bff4-08a91505f7c1)

The school summary dataframe generated in the previous section is used for selecting top and bottom performing schools. The schools were sorted using *"sort_values()"* function of pandas. 

### Maths and Reading Scores:

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/c6ce8a59-44dd-40a4-9c73-4bcb95d98941)

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/049b0cc8-1585-49d9-b032-b09749528078)

Using query function of pandas on combined school dataframe generated initially, data was grouped based on *school name*. Statistical analysis was performed to obtain the mathematical and reading scores for Year 9, 10, 11 and 12 respectively. Similar to the above sections, *map* functions of pandas was use to format the various columns of the datframe for cleaner formatting.

### Performance Assessment of School based on Spending, Size and Type:

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/d44e3b4b-3fb5-41c4-96e7-c0650f42e080)

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/58ef59b0-e769-44eb-bf75-f40b77ace69f)

![image](https://github.com/pkrachakonda/Pandas_Challenge/assets/20739237/07745d8f-6241-4725-b4e2-e8cf1da7ff21)

Based on bins, spending range and school size range definition provided as part of the challenge (in BootCampSpot (BCS) website), school summary dataframe generated in second section is used as base dataset. The columns were convereted from *object* dtype format to float64 format using astype() function of pandas, in order to be used for this secion. Based on the instructions provided in BCS, cut function of panads is applied on the data and passing percentages of maths and reading for schools were assessed based on
- Spending per student
- Size of school and
- What type of school.

Similar to the above sections, the columns were formated as per instructions in BCS.

## Conclusions:
- Medium size (1000 - 2000) *Independent* schools with per student spending range less than $630 have ***performed comparatively*** better than *Government* schools. On an average total budget of *Government schools* were ***200% higher*** than the Independent schools with an average per student spending of *$643* whereas for Independent schools, it was approx. *$598*.
- The *variability* of both maths and readings scores for all years are within ***normal distribution range***, i.e., within 2σ, with ***z score ranging from -1.8 to 1.7***, on an average. Performance of female students were *slightly (1-2%)* better than their counterparts in *reading* and were similar in *maths*.
