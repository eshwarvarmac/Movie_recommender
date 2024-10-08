import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')

similarity = pickle.load(open('similarity.pkl','rb'))


movies_dict = pickle.load(open('moviesdict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


option = st.selectbox(
    'Enter the name of the movie you like:',
    movies['title'].values
)

def recommend(movie):
    l=[]
    index = movies[movies['title']==movie].index[0]
    distances = similarity[index]
    y = list(enumerate(distances))
    recommendations = sorted(y,reverse=True,key=lambda x:x[1])[1:6]
    for i in recommendations:
        movie_id=movies.iloc[i[0]].id

        l.append(movies.iloc[i[0]].title)
    return l

if st.button('Recommend'):
    y=recommend(option)
    for i in y:
        st.write(i)

