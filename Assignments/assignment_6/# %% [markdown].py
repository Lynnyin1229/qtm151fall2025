# %% [markdown]
# # <span style="color:red"> QTM 151 - Quiz 2 </span>

# %% [markdown]
# <font size = "6">
# 
# **Submit as an HTML file**

# %% [markdown]
# <font size = "5" >
# This quiz is open book 
# 
# - You can use the lecture notes
# - You will get partial credit for attempting the questions
# - To get full credit, the code should run as intended
# - You should <span style="color:red"> NOT </span> communicate with other students
# 
# Print the following message: <br>
# 
# "I will abide by Emory's code of conduct"
# 

# %%
# Write your answer here:

print("I will abide by Emory's code of conduct.")


# %% [markdown]
# <font size = "5">
# 
# Import libraries
# 

# %%
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import os


# %% [markdown]
# <font size = "5">
# 
# Preliminary check: can you load the data?
# 
# <font size = "3">
# 
# In the .zip file you opened, there is a comma-separated values file named<br> "fifa23_players.csv". Using Pandas, create a DataFrame object by reading in this file.
# 
# If you get an error, you must figure out what the issue is.
# 
# **Note**: This cell is just to test whether you can access the data correctly. If everything works, you can copy and paste the code later in the notebook if you prefer.

# %%
# make sure you can load the data
print(os.getcwd())
df = pd.read_csv("data_quiz/fifa23_players.csv")

# %% [markdown]
# <font size = "5">
# 
# (1) Debugging code
# 
# <font size = "3">
# 
# The following code cell causes an error. Determine what causes the error, and add a comment to the offending line, explaining what the issue is (imagine you are trying to help a struggling classmate)
# 
# Then in the following blank code cell, put a corrected version of the code cell which does not cause an error, and run it.

# %%
def test_grade(numeric_grade):
    if grade >= 55:
        return "status = pass" 
    else:
        return "status = fail" 

student_grade = 55
print(test_grade(student_grade))

# %%
# your corrected version of the above code cell 

def test_grade(grade):
    if grade >= 55:
        return "status = pass" 
    else:
        return "status = fail" 

grade = 55
print(test_grade(grade))
#the input of the function's parameter is called "numeric_grade", but inside the function body, it uses "grade", and later in the print(), its called "student_grade"
#so there is a name error for the code, all these parameters are the same one, so it should have the same name. When I change the parameter's name from "numeric_grade" to grade, the code works well.

# %% [markdown]
# <font size = "5">
# 
# (2) More debugging
# 
# <font size = "3">
# 
# The following code cell **attempts** to define a Numpy array with 3 elements:
# 
# - $z_1 = 1^2 + 2^2 = 5$
# - $z_2 = 3^2 + 4^2 = 25$
# - $z_3 = 5^2 + 2^2 = 29$
# 
# However, when you run the cell, you will **not** see these three numbers.
# 
# Determine what causes the behavior, explaining why the code is not correct (imagine you are trying to help a struggling classmate)
# 
# Then in the following blank code cell, put a corrected version of the code cell which gives the correct output, and run it.

# %%
x_vals = [1, 3, 5]
y_vals = [2, 4, 2]

z_vals = np.array(x_vals + y_vals)**2
print(z_vals)

# %%
# your corrected version of the above code cell 
x_vals = [1, 3, 5]
y_vals = [2, 4, 2]

z_vals = np.array(x_vals)**2 + np.array(y_vals)**2
print(z_vals)
#Since in the wrong code, z_vals = np.array(x_vals + y_vals)**2 will not change x_vals and y_vals to numpy array,so "x_vals + y_vals" 
#will only combine two list instead of element by element addition, result in 6 values. So we need to change x_als and y_vals to numpy array one by one, then do the multiplyion.

# %% [markdown]
# <font size = "4">
# 
# In the .zip file you opened, there is a comma-separated values file named<br> "fifa23_players.csv". Using Pandas, create a DataFrame object by reading in this file.
# 
# - This is a dataset of professional soccer players
# - Rows correspond to players (18,539)
# - Columns contain attributes of players (32)
# - View the dataset before starting to get a sense of its content
# 
# **Hint**: Lectures 9 and 11 will be helpful for the rest of the questions!
# 

# %% [markdown]
# <font size = "5">
# 
# (3) Using ``.query``
# 
# <font size = "3">
# 
# - View the dataset and look for the name of the column corresponding to height in cm (centimeters). (No code/output is expected for this part).
# 
# - Using the ``.query`` method, extract the subset of players whose value of the height variable is **greater than** 175 and assign it to a new DataFrame.
# 
# - **Note**: The relevant column name has a space (and parentheses!), so you will need to use the backtick/grave accent (`) in your code.
# 
# - Using ``.shape``, define an integer variable ``num_tall`` which is the number of players who are above this height threshold.

# %%
# Write your own code

df2 = df.query("`Height(in cm)` > 175")
num_tall = df2.shape[0]



# %% [markdown]
# <font size = "5">
# 
# (4) Create a function and apply it to a column <br>
# 
# <font size = "3">
# 
# Step 1:
# - Define a function with a single input argument "Overall" which classifies each player as follows:
#     - If "Overall > 85", the function returns the string "Top Performer"
#     - If "Overall <= 85", the function returns the string "Non Top-Performer"
# 
# Step 2:
# - Extract the column "Overall" from the FIFA players DataFrame, and assign it to a variable (which should be a Pandas Series) <br>
# 
# - Using the Pandas ``.apply`` method, create a new Pandas Series called "player_classification" which contains the appropriate string for each player.

# %%
# Write your own code
def count(overall):
    if overall > 85:
        return "Top Performer"
    else:
        return "Non Top-Performer"
df["Player_classification"] = df["Overall"].apply(count)


# %% [markdown]
# <font size = "5">
# 
# (5) Split a dataset into subsets
#  
# 
# <font size = "3">
# 
# - We will continue using the DataFrame you read in from "fifa23_players.csv"
# - Use ``.shape`` to define an integer variable called ``n``, which is the total number of rows in this DataFrame. <br>
# - Use ``numpy.random.uniform`` to create a random sample of size ``n`` from the uniform distribution between 0 and 1. Then store these random numbers as a new column ``random_var`` to the original DataFrame.<br> 
# - Use ``.query`` to extract all players with ```random_var < 0.4```, and assign it to a new DataFrame called ``groupA``
# - Use ``.query`` to extract all players with ```random_var >= 0.4```, and assign it to a new DataFrame called ``groupB``.
# 
# **Note**: In this way, we are assigning roughly 40% of the players to Group A, and roughly 60% to Group B
# 

# %%
# Write your own code
n = df.shape[0]
df["random_var"] = np.random.uniform(0,1,n)
GroupA = df.query("`random_var` < 0.4")
GroupB = df.query("`random_var` >= 0.4")


# %% [markdown]
# <font size = "5">
# 
# (6) Create two scatter plots of the groups
# 
# <font size = "3">
# 
# - This question requires the two datasets you created in part (5)
# - Use ``matplotlib.pyplot.subplots`` to create two side by side scatter plots (1 row, 2 columns)
# - In the left figure, plot the columns ``Age`` vs. ``Overall`` for the data in ``groupA`` (so the horizontal axis will correspond to "Age")
# - In the right figure, plot the columns ``Age`` vs. ``Overall`` for the data in ``groupB`` (so the horizontal axis will correspond to "Age")
# - Label the axes for both plots. Create a title for **both** plots, indicating whether Group A or Group B is shown.
# 
# **Note**: If the assignment into groups was done randomly, then we expect that the scatter plots will be **very similar**

# %%
# Your code here

fig, (axes1, axes2) = plt.subplots(1, 2)
axes1.scatter(GroupA["Age"], GroupA["Overall"])
axes1.set_title("Group A Age vs. Overall")
axes1.set_xlabel("Age")
axes1.set_ylabel("Overall")
axes2.scatter(GroupB["Age"], GroupB["Overall"])
axes2.set_title("Group B Age vs. Overall")
axes2.set_xlabel("Age")
axes2.set_ylabel("Overall")




