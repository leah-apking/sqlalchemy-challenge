# sqlalchemy-challenge

### Part 1: Analyze and Explore the Climate Data

For this section we used Python and SQLAlchemy within our Jupyter notebook to do a basic climate analysis and data exploration. We began by using the create_engine function to connect to the SQLite database followed by automap_base to reflect the table into classes and linked the databased by creating a SQLAlchemy session.

To analyze the precipitation data we used the most recent date in the dataset to craft a query for the most recent 12 months of data selecting the data and precipitation values. This data was then loaded into a DataFrame and sorted by date before using Matplotlib to convert the DataFrame to a bar chart.

Next, we looked at the stations in our dataset and designed a query to determine the most active station. Focusing on this station we deigned a query to calculate the lowest, highest, and average temperatures. We then queried the data for the most recent 12 months of temperature observation data and created a histogram with Matplotlib to show the frequency of temperatures divided into 12 bins. 

### Part 2: Climate App with Flask

Now that we had explored the dataset and written a variety of queries, we had to use Flask to create an API based on those queries. The API included a homepage listing available routes, a precipitation page which returned a JSON representation of the dictionary we had previously retrieved, a stations page which returned a JSONified list of stations from the dataset, and a tobs page which returned a JSONified list of the temperature data used to create the histogram. The API also included pages which allowed users to provide a single start date or a pair of dates to form a range, these dates were then used to query the dataset and provide the minimum, average, and maximum temperatures for the date ranges provided.
