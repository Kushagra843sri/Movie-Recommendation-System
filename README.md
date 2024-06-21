# Movie-Recommendation-System

This project implements a movie recommendation system using machine learning techniques. The system is built using Python and utilizes collaborative filtering based on item similarity to provide personalized movie recommendations to users.
Dependency Management:
The project provides clear instructions for installing the required dependencies (pandas, scikit-learn, numpy, streamlit) using pip, ensuring a smooth setup process.

Dataset Integration:
Users are guided to download the tmdb dataset from the official website and place the necessary CSV files (tmdb_5000_credits.csv and tmdb_5000_movies.csv) in the project directory.

User-Friendly:
Streamlit app provides a straightforward interface with a dropdown for movie selection and a button to trigger recommendations.

Data Preprocessing:
The script handles data preprocessing by merging the credits and movies datasets, removing unnecessary columns, adding missing values and preparing the data for further analysis.

User-Item Matrix Creation:
A pivotal step in collaborative filtering, the project creates a user-item matrix, making it easier to compute recommendations based on user preferences.

Data Splitting:
The dataset is split into a training set and a testing set, following an 80:20 ratio. This ensures the model can be evaluated for its effectiveness.
Item Similarity Calculation:
Item-item similarity using cosine similarity is calculated and stored in similarity.pkl.

Recommendation Generation:
recommend() function generates top N recommended movies based on item similarity for a selected movie.

Customization:
The system is designed to allow customization and extension, as users can potentially modify the dataset and adjust the recommendation logic.
