# REDBUS PROJECT-Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

### PROJECT STATEMENT:
The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, 
analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, 
schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, 
this project can significantly improve operational efficiency and strategic planning in the transportation industry.
Data Set Requirements & Explanation:

### Technical Tags:
●	Web Scraping
●	Selenium
●	Streamlit
●	SQL
●	Data Analysis
●	Python (jupyter)
●	Interactive Application

### Data Set Explanation:
   The scraped dataset for this project contained detailed information about bus services available on Redbus, the fields are:
   Bustype,Bus RouteName, Bus RouteLink, Price, Seat availability,Departing Time, ReachingTime,Duration 

## Approach :
### 1) Data scapping using selenium and cleaning:
    First we installed all the important packages we need .like panadas,selenium(keys,web DriverWait,By,expected conditions),time
    for streamlit application-streamlit, MySQLconnector/SQLAlchemy,streamlit-option-menu 
     1) first we start importing all this nececessary packages using pip install command.
     2) we define web driver(chrome diver) to get and open the Red bus URL and maximizing the browser window for better visibility.
     3) Then we write the code for scapping the data for corresponding state link we provide,it followed by gathering all bus routes,bus routesname ,Route link,
        and all the bus information.
     4) The scrapped data we stored into CSV file with state name.
     5) like this we scapped each 17 state bus detailes ,each stored corresponding each state CSV files
     6) This CSV files content, we put in one CSV file.
     7) The workflow continues by establishing a connection between python and a MYSQL database.
     8) In MySQL we create one database and in that database we create one table, and in that table we inserted the csv file data.
     9) Here we clean the data and our data is ready for filteration ,connection is closed between database and python.        
### 2) streamlit webapplication :(redapp.py)
       1) The process start with importing streamlit and other required packages.
       2) Then we configure the web apllication page according to how we want to build.
       3) we set the connection between MySQL and python using the specific database we create earlier. 
       4) we write filteration code based on Routename, Bus type, price star rating and Seat availability.
       5) we write code for- retrived data displayed in table format when user provide input.
## How to run streamlit code:
      In your IDE terminal type:**streamlit run redapp.py(your file name like here redapp.py)**
## The solution can be applied to various business scenarios including:
●	Travel Aggregators: Providing real-time bus schedules and seat availability for customers.
●	Market Analysis: Analyzing travel patterns and preferences for market research.
●	Customer Service: Enhancing user experience by offering customized travel options based on data insights.
●	Competitor Analysis: Comparing pricing and service levels with competitors.
