import streamlit
import pandas
streamlit.title('My name is Debaleena Biswas') 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
Fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana','Lemon'])
Fruits_to_show = my_fruit_list.loc[Fruits_selected]
streamlit.dataframe(my_fruit_list)
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response= request.get("https://fruityvice.com/api/fruit/"+fruit_choice)
