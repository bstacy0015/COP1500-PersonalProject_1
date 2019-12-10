# COP1500-PersonalProject_1
The first personal project for my COP 1500 class.
I intend to do the "Data Analysis with Python" project.

### Goals
- Complete the project with a good grade.
- Begin my foundation for programming.
- Gain extra proficiency with mathematics, for my major.

### Boundaries / Scope
- Complete Course 6 of 9 in the [IBM Data Science Specialization](https://www.coursera.org/specializations/ibm-data-science): "Data Analysis with Python"

### Success criteria
- Pass the course by completing all graded assignments in the course with a passing grade.
- Create a program that can analyze data, retrieved either through manual or automatic means. 

### Constraints
- I will be auditing the course for free so will be able to read and view the course content but not submit projects or earn the certification.

### Assumptions
- The courses will be available for the duration of the semester.
-   I have all required software.
-   I should do all modules, once per week.

### Stakeholders
- Professor -  to get a good grade for the project
- Parents - they can see my prowess in computer science
- Perspective Employers - this project will be one of many in my portfolio

### Timelines
| Week |         Objective(s)        |Time    | Done? |
|:----:|:---------------------------:|:------:|:-----:|
|   1  | Importing Datasets          | 2h 15m |   ✓   |
|   2  | Data Wrangling              | 2h 18m |   ✓   |
| 3+4  | Exploratory Data Analysis   | 2h 18m |   ✓   |
| 5+6  | Model Development           | 2h 27m |   ✓   |
| 6+7  | Model Evaluation            | 2h 23m |   ✓   |
|   8  | Work on Independent Project | 3h     |   ✓   |
|   9  | Finish Independent Project  | 3h     |   ✓   |

 1. Importing Datasets. This week's course content was relatively simple, because it acted as an intro to the course. I learned about how packages work, and the basics of Pandas, a Python package about data science. I also learned how to use Anaconda, an environment that comes bundled with thousands of data science and visualization packages.
 2. Data Wrangling. I learned how pre-processing of data works, especially in Python. I learned how to remove data row or columns with the pandas "`dropna`" method, or how to clean data with the pandas "`replace`" method. I learned how to change units for rows and columns and how to normalize data with algebra and code, and work with different data types such as `str`, `obj`, and `int`/`float`, and how to change them. See [DataScience_2.pdf](https://github.com/bstacy0015/COP1500-PersonalProject_1/blob/master/DataScience_2.pdf) to read my notes.
 3. Exploratory Data Analysis. I learned how to use descriptive statistics and find the correlation of two variables, as well as conduct simple data visualization with Python. Using `describe()` and `value_counts()` allows me to see a summary of the festures of the data. I can create box plots with seaborn's `boxplot()` and a scatterplot with matplotlib's `scatter()`. I lastly learned how to use seaborn's `regplot()` to plot the regression line of data and how to run ANOVA tests and find correlation. See [DataScience3.pdf](https://github.com/bstacy0015/COP1500-PersonalProject_1/blob/master/DataScience_3.pdf) to read my notes.
 
 4. Model Development. Arguably the hardest section. I learned how to fit a regression line with one variable (simple linear regression → SLR) and multiple variables (multiple linear regression → MLR) with scikit-learn's `fit()` function. I then learned how to make polynomial regressions (i.e. degree > 1) with numpy's `polyfit()` function (or multivariable polynomial regressions with scikit-learn's `fit_transform()` function). I lastly learned simple model evaluation with mean squared error (MSE) or the coefficient of determination (R<sup>2</sup>). See [DataScience_4.pdf](https://github.com/bstacy0015/COP1500-PersonalProject_1/blob/master/DataScience_4.pdf) to read my notes.
 5. Model Evaluation. This section taught me the most of any other section, because model evaluation was something I was never exposed to. I was introduced to why data scientists need to partition data to be used for specific purposes, such as training the model and testing the model for accuracy. I learned about the balance between accuracy to training data and the accuracy to the model and how choosing the right order (degree) of the function will lead to proper model prediction, and how I can use tools in Python to choose the right order. Using *model selection* by simultaneously calculating the R<sup>2</sup> values of different best-fit equations of different orders, I can properly choose the right order. I can also use the (seemingly arbitrary) value α (alpha) to preform *ridge regression* to smooth my lines of best fit and prevent overfitting of my curve. Lastly, I learned how to effectively manage my data when evaluating my model's accuracy, by using *cross-validation* and *grid searching*. See [DataScience_5.pdf](https://github.com/bstacy0015/COP1500-PersonalProject_1/blob/master/DataScience_5.pdf) to read my notes.
