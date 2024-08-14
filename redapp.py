import pandas as pd
import numpy as np
import streamlit as st
from sqlalchemy import create_engine
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# create SQLAlchemy engine
engine = create_engine('mysql+pymysql://root:Tanvi@localhost:3306/REDBUS' )

# query data from mysql database
query = "SELECT * FROM Buses"
data = pd.read_sql(query, engine)

# convert column to numeric datatype
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
data['Seat_Availability'] = pd.to_numeric(data['Seat_Availability'], errors='coerce')
data['Star_Rating'] = pd.to_numeric(data['Star_Rating'], errors='coerce')

# Main streamlit program
st.set_page_config(
    page_title="Redbus",
    page_icon=":redbus:",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #FFFFFF;
        margin-right: 20px;
        border-right: 2px solid #F0F0F0
    }
</style>
""", unsafe_allow_html=True)

st.title(":red[RED BUS]") 
st.header("Best online ticket booking app")
st.text("EASY TO BOOK TICKET AND EASY TO TRAVEL AND HASSEL FREE JOURNEY")

# sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home', 'Search Bus'],
        icons=['house-door-fill', 'search'],
        menu_icon='truck-front-fill',
        default_index=0,
        styles={
            "container": {'padding': '5!important', 'background-color': '#FAF9F6'},
            "icon": {'color': "#000000", "font-size": "23px"},
            "nav-link": {'font-size': '16px', 'text-align': 'left', 'margin': '0px', '--hover-color': '#EDEADE', 'font-weight': 'bold'},
            "nav-link-selector": {'background-color': '#E6E6FA', 'font-weight': 'bold'}
        }
    )

# home page
if selected == 'Home':
    st.subheader("India's No 1 online Bus Booking site ")
    st.subheader("Apno Ko Sapno Ko Kareeb Laye")
    st.markdown("""
    redBus is India's largest brand for online bus ticket booking and offers an easy-to-use online bus and 
    with over 36 million satisfied customers, 3500+ bus operators to choose from, and plenty of offers on bus ticket booking, 
    redBus makes road journeys super convenient for travellers. A leading platform for booking bus tickets,
    redBus has been the leader in online bus booking over the past 17 years across thousands of cities and lakhs of routes in India.
    redBus offers bus tickets from some of the top private bus operators, such as Orange Travels, VRL Travels, SRS Travels, Chartered Bus, 
    and Praveen Travels, and state government bus operators, such as APSRTC, TSRTC, GSRTC, Kerala RTC, TNSTC, RSRTC, UPSRTC, and more. With redBus, 
    customers can easily book bus tickets for different bus types, such as AC/non-AC, Sleeper, Seater, Volvo, Multi-axle, AC Sleeper, Electric buses, and more.
    """)
    st.image("https://newsroompost.com/wp-content/uploads/2020/05/redb.jpg",use_column_width=True)

# search Bus page 
if selected == "Search Bus":
    # Initialize filters
    bustype_filter = st.multiselect('Select Bus Type:', options=data['Bus_Type'].unique())
    select_route = st.multiselect('Select Route:', options=data['Route_Name'].unique())
    price = st.slider('Select Price Range:', min_value=int(data['Price'].min()), max_value=int(data['Price'].max()), value=(int(data['Price'].min()), int(data['Price'].max())))
    star_filter = st.slider('Select Star Rating Range:', min_value=float(data['Star_Rating'].min()), max_value=float(data['Star_Rating'].max()), value=(float(data['Star_Rating'].min()), float(data['Star_Rating'].max())))
    availability = st.slider('Select Seat Availability Range:', min_value=int(data['Seat_Availability'].min()), max_value=int(data['Seat_Availability'].max()), value=(int(data['Seat_Availability'].min()), int(data['Seat_Availability'].max())))

    # filter data based on user inputs
    filtered_data = data.copy() 

    if bustype_filter:
        filtered_data = filtered_data[filtered_data['Bus_Type'].isin(bustype_filter)]

    if select_route:
        filtered_data = filtered_data[filtered_data['Route_Name'].isin(select_route)]

    filtered_data = filtered_data[(filtered_data['Price'] >= price[0]) & (filtered_data['Price'] <= price[1])]
    filtered_data = filtered_data[(filtered_data['Star_Rating'] >= star_filter[0]) & (filtered_data['Star_Rating'] <= star_filter[1])]
    filtered_data = filtered_data[(filtered_data['Seat_Availability'] >= availability[0]) & (filtered_data['Seat_Availability'] <= availability[1])]

    # display filtered data
    st.write('Filtered Data:')
    st.dataframe(filtered_data)

    # add a download button to export the filtered data
    if not filtered_data.empty:
        st.download_button(
            label="Download Filtered Data",
            data=filtered_data.to_csv(index=False),
            file_name="filtered_data.csv",
            mime="text/csv"
        )
    else:
        st.warning("No data available with the selected filters.")
