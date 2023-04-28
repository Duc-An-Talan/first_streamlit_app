import streamlit

streamlit.title("My Mom' New Healthy Diner ")
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page of the selected fruits only 

streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.title('Fruityvice Fruit Advice')

import requests
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json()) # just write the data to the screen
# take the json file and normalized it  
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output a table 
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
#streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)
#rajouter un fruit
add_my_fruit=streamlit.text_input('What fruit would you like to add?')
streamlit.write ('Thanks for adding', add_my_fruit)
#ça ne va pas marcher correctement
my_cur.execute("insert into fruit_load_list values ('from streamlit')")




