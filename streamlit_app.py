import streamlit
import pandas
streamlit.title('My name is Debaleena Biswas') 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
Fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['apple','strawbarries'])
Fruits_to_show = my_fruit_list.loc'apple'
streamlit.dataframe(Fruits_to_show)
