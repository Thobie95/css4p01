import pandas as pd
df = pd.read_csv('movie_dataset.csv')
pd.set_option('display.max_rows', None)
print(df)



df.columns = df.columns.str.replace(' ', '_')
pd.set_option('display.max_rows', None)
print(df)


# Check for missing values in each column
print(df.isnull().sum())
df = df.dropna()


#movies released in 2016
movies_2016_count = df[df['Year'] == 2016].shape[0]
print(movies_2016_count)

#highest-rated movie
highest_rated_index = df['Rating'].idxmax()
highest_rated_movie = df.loc[highest_rated_index]
print("The highest-rated movie is:")
print(highest_rated_movie[['Title', 'Rating']])

# Average revenue
average_revenue = df['Revenue_(Millions)'].mean()
print("The average revenue of all movies in the dataset is: ${:.2f} million".format(average_revenue))


#2015 to 2017
filtered_movies = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_to_2017 = filtered_movies['Revenue_(Millions)'].mean()
print("from 2015 to 2017: ${:.2f} million".format(average_revenue_2015_to_2017))


#movies released in 2016
movies_2016_count = (df['Year'] == 2016).sum()
print("The number of movies released in the year 2016 is:", movies_2016_count)


#Christopher Nolan movvies
nolan_movies_count = (df['Director'] == 'Christopher Nolan').sum()
print(nolan_movies_count)


#at least 8.0 rating
high_rated_movies_count = (df['Rating'] >= 8.0).sum()
print(high_rated_movies_count)

# Christopher Nolan movies
nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()
print(median_rating_nolan_movies)

#highest rating
average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()
print(year_highest_average_rating)
print(highest_average_rating)


# movies count
movies_count_by_year = df['Year'].value_counts().sort_index()
movies_2006 = movies_count_by_year.loc[2006]
movies_2016 = movies_count_by_year.loc[2016]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(percentage_increase)


#common actor
from collections import Counter
all_actors = ', '.join(df['Actors'])
individual_actors = all_actors.split(', ')
actor_counts = Counter(individual_actors)
print(most_common_actor)


#genres
all_genres_list = df['Genre'].str.split(', ')
unique_genres = set()
for genres_list in all_genres_list:
    unique_genres.update(genres_list)
num_unique_genres = len(unique_genres)
print(num_unique_genres)



# correlation analysis
numeric_columns = df.select_dtypes(include=['number'])
correlation_matrix = numeric_columns.corr()
print("Correlation Matrix:")
print(correlation_matrix)

