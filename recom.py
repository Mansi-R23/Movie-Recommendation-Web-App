# -*- coding: utf-8 -*-
"""
Created on Sat May 28 23:21:33 2022

@author: Mansi
"""



#movie recom
import requests
import streamlit as st
import pickle
import pandas as pd
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()





def recom(movie):
   
  index = mov[mov.title == movie]['index'].values[0]

  score = list(enumerate(similar[index]))
  sort = sorted(score, key = lambda x:x[1], reverse = True)

  print('Movies suggested for you : \n')

  i = 0
  recom_list_tit=[]
  recom_list_vote=[]
  recom_list_hm=[]
  for movies in sort:
   
    index = movies[0]
    title_from_index = mov[mov.index==index]['title'].values[0]
    st.header(title_from_index)
    vote_avg=mov[mov.index==index]['vote_average'].values[0]
    st.write("Rating  ","\t:",vote_avg)
    
    hp=mov[mov.index==index]['director'].values[0]
    st.write("Director        :",hp)
    
    st.text(" ")
    st.text(" ")
    st.text(" ")



    if (i<20):
        if(i!=0):
            recom_list_tit.append(title_from_index)
            recom_list_vote.append(vote_avg)
            recom_list_hm.append(hp)
     
        i+=1
      
    else:
        break

  return recom_list_tit,recom_list_vote,recom_list_hm
    
    
    
#========================================================================

    

movie_list = pickle.load(open('C:/Users/Manasi/Desktop/python_project/movie_dict.pkl','rb'))
mov=pd.DataFrame(movie_list)

similar = pickle.load(open('C:/Users/Manasi/Desktop/python_project/similar.pkl','rb'))
st.title('Hollywood Movie Recommendation ')
lottie_1 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_CTaizi.json")
st_lottie(lottie_1, speed=1, height=400, width=400, quality="medium", loop=True)


selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    mov['original_title'].values)


if st.button('Show Recommendation'):
    recom(selected_movie)
    
lottie_2 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_z5loe4p9.json")
st_lottie(lottie_2, speed=1, height=400, width=400, quality="medium", loop=True)    
  
    

     

        
    
        
        
        
        