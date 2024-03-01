import streamlit as st

import pandas as pd

st.set_page_config(layout="wide",
                   page_title="MYTHO DATA",
                   page_icon=":COMPUTER:")



col1,col2=st.columns([1.2,2])

with col1 :
    st.image("images/banner3.png",use_column_width="always" , output_format='PNG')
with col2 :
    st.title("MYTHO DATA")
    information="""🚀 Welcome to the ultimate journey through Data Science, Matrix, the dynamic data science club, hosts engaging sessions delving into the fundamentals of Data Science, catering to beginners and enthusiasts alike. Renowned industry specialists grace our platform, sharing invaluable insights through informative talks, and enriching our members with real-world perspectives.

The club pulsates with creativity, fostering an environment where minds collide and innovate during exhilarating hackathons. Beyond serious learning, we infuse excitement with lively and intellectually stimulating quizzes, sprinkling fun amidst the educational journey.

Matrix thrives on the ethos of exploration, experimentation, and collaboration, sculpting a vibrant community passionate about unraveling the intricacies of data science. Join us to uncover the endless possibilities within this fascinating field, blending education and enjoyment seamlessly.\nIf you want to contact the organizer, feel free to reach out to Shrijeet Kumar at 9263644025.🔥📊🧠"""
    st.info(information)

    

st.write("Below you can find  the datasets of both the rounds!!")


col3,empty_col,col4= st.columns([1.5,0.5,1.5])


df=pd.read_csv("data.csv",sep=";")

counter = 0
for index, row in df.iterrows():
    if counter % 2 == 0:
        with col3:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[DATA SET]({row['dataset_url']})")
    else :
        with col4:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[DATA SET]({row['dataset_url']})")
    counter += 1