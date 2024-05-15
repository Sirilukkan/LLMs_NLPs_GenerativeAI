import streamlit as st
from Langchain_code import gen_travel_plan

st.title("Travel Plan Generator")

country = st.sidebar.selectbox("Which country do you want to travel to?",("Japan", "South Korea", "Taiwan", "China", "Thailand",
"Vietnam", "Indonesia", "Switzerland", "England", "France", "Italy",
"Australia", "New Zealand", "United States", "Canada", "Mexico",
"Brazil", "Argentina", "Spain", "Portugal", "Germany", "Netherlands",
"Belgium", "Austria", "Greece", "Turkey", "Russia", "South Africa",
"Egypt", "Morocco", "United Arab Emirates", "Saudi Arabia", "India",
"Malaysia", "Singapore", "Philippines", "Sri Lanka", "Maldives",
"Czech Republic", "Hungary", "Poland", "Denmark", "Sweden", "Norway",
"Finland", "Ireland", "Scotland", "Croatia", "Cuba", "Peru"))

if country:
    response = gen_travel_plan(country)
    st.header('Places to Visit')
    places = response['places_name'].strip()
    st.write(places)
    spot_food_places = response['spot_food_places'].strip()
    plans = response['one_week_plan'].strip()
    st.write("**Popular Spots and Resturants**")
    st.write(spot_food_places)
    st.write("**One Week Plan**")
    st.write(plans)
