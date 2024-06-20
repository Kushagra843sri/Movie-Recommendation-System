import streamlit as st
import pickle
import pandas as pd
import requests
import time


# Function to fetch movie poster
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=3d575036caf8f9290a7d87d105573fbc&language=en-US')
        data = response.json()
        if 'poster_path' in data and data['poster_path'] is not None:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return None  # Handle the case where the poster_path is not available
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster_url = fetch_poster(movie_id)
        if poster_url:
            recommended_movies_poster.append(poster_url)
        else:
            recommended_movies_poster.append(
                "https://via.placeholder.com/500")  # Placeholder image if poster is not available
    return recommended_movies, recommended_movies_poster


# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app layout
st.title('Movie Recommendation System')

# Movie selection dropdown
selected_movie_name = st.selectbox(
    'Which movie would you like to see recommendations for?',
    movies['title'].values
)

# Recommendation button
if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        time.sleep(2)  # Simulate loading time
        names, posters = recommend(selected_movie_name)

    # Display recommendations
    st.subheader('Recommended Movies:')
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], use_column_width=True)
            st.write(names[idx])

# Additional improvements
st.sidebar.header('About')
st.sidebar.write("""
This Movie Recommendation System uses content-based filtering to suggest movies similar to the one you like. 
Select a movie from the dropdown menu and click 'Recommend' to see the top 5 similar movies.
""")

# Example usage of other interactive widgets (optional)
st.sidebar.header('Settings')
option = st.sidebar.radio('Select recommendation algorithm:', ('Content-based', 'Collaborative Filtering'))
if option == 'Collaborative Filtering':
    st.sidebar.write("Collaborative Filtering is not yet implemented.")

# Adding a link to The Movie Database
st.sidebar.markdown(
    "[![TMDb](https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-2f78d82bbd4805d24f04cc8e3e9a95a4a93d03a987e8b8ae73a4ee2a72d9a42f.svg)](https://www.themoviedb.org/)")
