This project is a movie recommendation system, where in the user inputs a movies dataset and a movie that he likes, and the program will be able to output top 20 movies that are similar to this movie.
To solve this problem, I used two concepts in sklearn library in python.
1. count vectorizer: This converts text into vector based on the frequency of words in that text.
2. cosine similarity: This calculates the cosine angle between two vectors as A.B/||A||*||B||
So if the two vectors have same reviews, they have high cosine value.
Based on these two concepts, I have extracted reviews column from the dataset and from the entered movie, I calculate the cosine similarity of current movie and other movies.
Sorting them in decreasing order gives the movies in recommending order.

Earlier this was implemented in google colab, now I'm working on creating a user interface using flask (python web framework to integrate this python code with the frontend interface).