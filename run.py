'''
Author : Siddhi Venkata Sai Karthik Veeranki
mail ID : karthik.veeranki.2003@gmail.com
Institute : IIT Goa
'''


# importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


from google.colab import files
file_input = files.upload()       # upload the file IMDB-Movie-Data.csv


# A function to combine the values of the important columns
def extract_important_features(data_set):
    important_features = []
    for i in range(data_set.shape[0]):
        important_features.append(data_set['Title'][i] + ' ' + data_set['Actors'][i] + ' ' + data_set['Director'][i] + ' ' + data_set['Genre'][i])

    return important_features


# variable that stores contents of the required file
df = pd.read_csv('IMDB-Movie-Data.csv')


# Create a list of four columns for the recommendation engine
columns = ['Title','Actors','Director','Genre']


# Create a column to hold the combined strings
df['important_features'] = extract_important_features(df)


# Convert the text to a matrix of token counts
count_matrix = CountVectorizer().fit_transform(df['important_features'])


# Get the cosine similarity matrix from the count matrix
cos_similarity_matrix = cosine_similarity(count_matrix)


# input the title of the movie that the user watched
title = input("\nEnter the title of the movie that you have watched\n")


# Find the movie id
movie_id = df[df.Title == title]['Rank'].values[0] 


print('\nMovie ID = ',movie_id)   # displays the movie ID


# Create a list of enumerations for the similarity score. This list consists of all those movies similar to that of user's ones
scores = list(enumerate(cs[movie_id]))


# Sort the list in the decreasing order of preference 
sorted_scores = sorted(scores, key = lambda x: x[1], reverse = True)


# slice the list because the zeroth index contains the same movie which user enters
sorted_scores = sorted_scores[1:]


# iterate over the sorted_scores to print the top 20 recommended movies

print('\nTop 20 recommended movies to', title, 'are:\n')
i = 1
for movie in sorted_scores:
    if(i > 20):
        break
        
    movie_title = df[df.Rank == movie[0]]['Title'].values[0]
    print(i,end = ". ")
    print(movie_title)
    i += 1 
    
