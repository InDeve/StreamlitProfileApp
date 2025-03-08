
''' We want to load the title and description first '''

import streamlit as st
st.title("Anime Recommendation")
st.text("See an Anime recommendation based on users who like the same show as you do.")
st.text("""
  Wonder how this works? I'm using a KNN algorithm to find users that have rated your show highly and gauging that with other shows they have rated highly. Using purely numerical data, we can find interesting recommendations, who knows how accurate, without user input. 
        """)
st.caption("This example page only uses 1million rows of the data. _dataset based on_: https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?resource=download ")

loading_msg = st.empty()
loading_msg.info("Loading Model...")

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

import os
import pandas as pd


# ''' DATA PROCESSING AND LOADING '''

@st.cache_data
def load_data():
    anime_df = pd.read_parquet("ml_models/anime_filtered_1mil.parquet")
    # We drop duplicates so the data isn't redundant when selecting a point.
    anime_data_rating = anime_df.drop_duplicates(subset=['user_id','title'])
    # If the rating doesn't exist, fill it with 0 in the data pivot
    anime_data_pivot = anime_data_rating.pivot_table(index=['title'],
                                                 columns=['user_id'], values='my_score').fillna(0)
    anime_data_matrix = csr_matrix(anime_data_pivot.values)
    return anime_df, anime_data_matrix, anime_data_rating

anime_df, anime_data_matrix, anime_data_rating = load_data()
#st.dataframe(anime_df)

@st.cache_resource
def load_model():
    # Fit the model with KNN
    anime_model = NearestNeighbors(metric='euclidean', algorithm='brute')
    anime_model.fit(anime_data_matrix)
    # If the rating doesn't exist, fill it with 0 in the data pivot
    anime_data_pivot = anime_data_rating.pivot_table(index=['title'],
                                                    columns=['user_id'], values='my_score').fillna(0)
    return anime_data_pivot, anime_model

anime_data_pivot, anime_model = load_model()

# ''' CORE FUNCTION '''
@st.cache_data
# Get user show
def get_recommendations(screen_input):
  user_input = screen_input.lower().rstrip()
  try:
    # This is added for EN and JP name support
    names = ['title']
    # This will search through both EN and JP show names for the user's show
    user_show = anime_df.loc[anime_df[names].apply(lambda x: x.str.lower()).apply(lambda x: x.str.contains(user_input)).any(axis=1)]
    if user_show.empty:
      raise ValueError('Show not found')
    else:
      # Output the recommendation text here
      text = ''
      # for some reason we don't need to change this to grab names from EN and JP
      show_index = anime_data_pivot.index.get_loc(user_show.iloc[0]['title'])
      # use knn model to get the nearest neighbors. n_neighbors will be how many shows it gets - 1
      distances, indices = anime_model.kneighbors(anime_data_pivot.iloc[show_index,:].values.reshape(1,-1), n_neighbors=21)
      for i in range(0, len(distances.flatten())):
        if i == 0:
          # indexing: {0[0][1]} where 0[0][x] and x is the name type (JP-Romaji, EN, JP)
          text += 'If you\'ve watched {0}, then you might like:\n\n'.format(anime_data_pivot.index[show_index])
          # return text
        else:
          # indexing: {0} states the users show | {1[x]} where x displays the name type (JP-Romaji, EN, JP)
          text += '{0}: {1}\n\n'.format(i, anime_data_pivot.index[indices.flatten()[i]], distances.flatten()[i])
      return text
  except:
    return f'{user_input} could not be found'

# ''' USER INTERFACE '''
loading_msg.empty()

anime = st.text_input("Enter an Anime:")

if anime:
    st.write(get_recommendations(anime))