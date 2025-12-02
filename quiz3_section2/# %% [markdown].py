# %% [markdown]
# # <span style="color:red"> QTM 151 - Practice Quiz </span>

# %% [markdown]
# <font size = 5>
# 
# **Submit as an HTML file** (see images below)
# 
# <font size = 3>
# 
# Step 1: Click the 3 dots in the toolbar for "More Actions"
# 
# <img src="practice_quiz_figures/step1.png" alt="drawing" width = "600"/>
# 
# ***
# Step 2: Choose "export"
# 
# <img src="practice_quiz_figures/step2.png" alt="drawing" width = "600"/>
# 
# ***
# Step 3: Select "HTML" from the dropdown window
# 
# <img src="practice_quiz_figures/step3.png" alt="drawing" width = "600"/>
# 
# ***
# Step 4: Select "Export" in the pop-up window.
# 
# <img src="practice_quiz_figures/step4.png" alt="drawing" width = "300"/>
# 
# Upload the .html file as your submission
# 

# %% [markdown]
# <font size="5"> 
# 
# Print your name below

# %%
# Write your answer here

print("Lynn Yin")

# %% [markdown]
# <font size = "5" >
# This quiz is open book 
# 
# - You can use the lecture notes
# - You will get partial credit for attempting the questions
# - To get full credit, the code should work as intended
# - You should <span style="color:red"> NOT </span> communicate with other students
# 
# Print the following message: <br>
# 
# "I will abide by Emory's code of conduct"

# %%
# Write your answer here:
print("I will abide by Emory's code of conduct.")

# %% [markdown]
# <font size = "5">
# 
# Import pandas

# %%
import pandas as pd


# %% [markdown]
# 
# <font size = "5">
# 
# (1) Replace the values of a column
# 
# <font size = "3">
# 
# - Consider the DataFrame ``df_movies`` created below.
# - In the "country" column, change the values "American" and "Korean" to "USA" and "ROK" respectively
# - Do this by using the ``.replace`` method.

# %%
# Create example DataFrame - **don't change this**
titles = ["Past Lives", "Citizen Kane", "Revenge", "Okja", "Shutter", 
    "A Tale of Two Sisters", "La Chinoise", "The Umbrellas of Cherbourg", "House",
    "Suspiria", "Blue Velvet"]
country = ["American", "American", "France", "Korean", "Thailand", "Korean", "France",
    "France", "Japan", "Italy", "American"]
runtime = [106, 119, 108, 120, 97, 115, 96, 91, 88, 98, 120]
year = [2023, 1941, 2017, 2017, 2004, 2003, 1967, 1964, 1977, 1977, 1986]
movie_dict = {"title" : titles, "country" : country, "runtime" : runtime, "year" : year}
df_movies = pd.DataFrame(movie_dict)


# your answer here
df_movies["country"] = df_movies["country"].replace({"American": "USA", "Korean": "ROK"})
print(df_movies)




# %% [markdown]
# <font size = "5">
# 
# (2) Recode a numeric column
# 
# <font size = "3">
# 
# - Consider the DataFrame ``df_movies`` created above
# - Recode the "year" column into a new column "year_brackets" <br>
# with the following categories:
# 
# $\qquad$ ``` ["1941-1967","1968-1999","2000-onwards"] ```
# 
# $\qquad$ HINT: Use the "pd.cut()" command.

# %%
# your code here

df_movies["year_brackets"] = pd.cut(
    df_movies["year"],
    bins=[1940, 1967, 2000, 100000],
    labels=["1941-1967", "1968-1999", "2000-onwards"]
)

print(df_movies)



# %% [markdown]
# <font size = "5">
# 
# (3) Rename column
# 
# <font size = "3">
# 
# - Consider the DataFrame ``df_movies`` created above
# - Rename the column "runtime" to "runtime(minutes)"

# %%
# Write your answer here:

df_movies = df_movies.rename(columns={"runtime": "runtime(minutes)"})
print(df_movies)


# %% [markdown]
# <font size = "5">
# 
# (4) Merge dataset
# 
# <font size = "3">
# 
# - Consider the DataFrames ``df_movies`` (created above) and ``df_scores`` (created below)
# - Create a new dataset using  ```pd.merge()``` using <br>
# "df_movies" as the primary dataset, and <br>
# "df_scores" as the secondary dataset, merging on <br>
# the column "title"
# - You should **ONLY** merge the "imdb_score" column <br>
# from the secondary dataset (not the "director" column)
# 
# HINT: Use ```[[...]]``` to extract a subset of columns <br>
# from the secondary dataset before merging

# %%
# create example DataFrame - don't change this
titles = ["Past Lives", "Citizen Kane", "Revenge", "Okja", "Shutter", 
    "A Tale of Two Sisters", "La Chinoise", "The Umbrellas of Cherbourg", "House",
    "Suspiria", "Blue Velvet"]
scores = [7.8, 8.2, 6.4, 7.3, 7.0, 7.1, 6.9, 7.8, 7.2, 7.3, 7.7]
directors = ["Celine Song", "Orson Welles", "Coralie Fargeat", "Bong Joon Ho", 
    "Banjong Pisanthanakun", "Kim Jee-woon", "Jean-Luc Godard", "Jacques Demy", 
    "Nobuhiko Obayashi", "Dario Argento", "David Lynch"]

movie_dict2 = {"title" : titles, "imdb_score" : scores, "director" : directors}
df_scores = pd.DataFrame(movie_dict2)

# Write your answer here:
merged = pd.merge(df_movies, df_scores[["title", "imdb_score"]],on="title",how="left")
print(merged)



# %% [markdown]
# <font size = "5">
# 
# (5) Aggregate and sort
# 
# <font size = "3">
# 
# - Using the merged dataset you created above, do the following in a single line by chaining:
#     - Group the dataset by "country"
#     - Aggregate the following statistics: average runtime, maximum runtime, average IMDB score, minimum IMDB score
#     - Score by average IMBD score in **descending order**
# 
# Print the resulting DataFrame
# 
# 

# %%
# Write your answer here:
df2= merged.groupby("country").agg(avg_runtime=("runtime(minutes)","mean"), max_runtime=("runtime(minutes)","max"), avg_IMDB=("imdb_score","mean"),min_IMDB=("imdb_score","min") ).sort_values("avg_IMDB", ascending=False)
print(df2)





# %% [markdown]
# <font size = "5">
# 
# (6) Query and Aggregate
# 
# <font size = "3">
# 
# Using the merged dataset you created above, do the following in a single line by chaining:
# 
# - Subset the observations for 'country == France' using ```.query()```
# - Sort the values by year (oldest first)
# - Extract the two oldest movies
# 
# Print the resulting DataFrame to the screen

# %%
# Write your answer here:
df3= merged.query("country == 'France'").sort_values("year").head(2)
print(df3)




