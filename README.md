# Project Submission: YouTube Data Harvesting and Warehousing using SQL, MongoDB, and Streamlit

##Introduction

The "YouTube Data Harvesting and Warehousing" project is a comprehensive solution that allows users to access, analyze, and manage data from various YouTube channels. This project combines SQL, MongoDB, and Streamlit to create an intuitive application for retrieving, storing, and querying YouTube channel and video data.

##Project Overview

This project comprises the following key components:

###Streamlit Application: A user-friendly interface developed with the Streamlit library, enabling users to interact with the application for data retrieval and analysis.

###YouTube API Integration: Seamless integration with the YouTube API to extract channel and video data using provided channel IDs.

###MongoDB Data Lake: A flexible and scalable storage solution for storing unstructured and semi-structured data retrieved from YouTube.

###SQL Data Warehouse: Data migration from the MongoDB data lake to a SQL database (MySQL), facilitating efficient querying and analysis via SQL.

###Data Visualization: Utilization of Streamlit's data visualization capabilities to present retrieved data through charts and graphs, making it easier for users to gain insights.

##Technologies Used

The project leverages the following technologies:

###Python: The primary programming language used for application development and scripting tasks.

###Streamlit: A Python library employed for creating interactive web applications and data visualizations.

###YouTube API: Google API serves as the conduit for accessing channel and video data from YouTube.

###MongoDB: A NoSQL database employed as a data lake for storing YouTube data.

###SQL (MySQL): A relational database used as a data warehouse for storing the migrated YouTube data.

###SQLAlchemy: A Python library utilized for database connectivity and interaction.

###Pandas: A data manipulation library used for data processing and analysis.

###Matplotlib: A data visualization library that facilitates the creation of charts and graphs.

##References

Streamlit Documentation: https://docs.streamlit.io/
YouTube API Documentation: https://developers.google.com/youtube
MongoDB Documentation: https://docs.mongodb.com/
SQLAlchemy Documentation: https://docs.sqlalchemy.org/
Python Documentation: https://docs.python.org/
Matplotlib Documentation: https://matplotlib.org/

##Installation and Setup

To run the "YouTube Data Harvesting and Warehousing" project, follow these steps:

Install Python: Ensure Python is installed on your machine.

Install Required Libraries: Use the package manager (pip or conda) to install essential Python libraries, including Streamlit, the MongoDB driver, SQLAlchemy, Pandas, and Matplotlib.

Set Up Google API: Create a Google API project and acquire the necessary API credentials to access the YouTube API.

Configure Databases: Set up both a MongoDB database and an SQL database (MySQL) to store the data.

Configure Application: Update the configuration file or environment variables with the requisite API credentials and database connection details.

Run the Application: Start the Streamlit application via the command-line interface.

##Usages

After completing the setup, users can access the "YouTube Data Harvesting and Warehousing" application through a web browser. The application offers the following capabilities:

Input a YouTube channel ID to retrieve data related to that channel.
Store the obtained data in the MongoDB data lake.
Gather and store data for multiple YouTube channels in the data lake.
Choose a channel and transfer its data from the data lake to the SQL data warehouse.
Search and extract data from the SQL database using various search options.
Perform data analysis and visualize data through Streamlit's built-in chart and graph capabilities.

##Features

The "YouTube Data Harvesting and Warehousing" application provides the following features:

-Retrieval of channel and video data from YouTube using the YouTube API.
-Storage of data in a MongoDB database as a data lake.
-Migration of data from the data lake to a SQL database for efficient querying and analysis.
-Advanced search options and the ability to join tables for complex queries.
-Data analysis and visualization through charts and graphs, enhancing data interpretation.
-Support for managing data from multiple YouTube channels.

##Future Enhancements

The project has ample room for future improvements, including:

Authentication and User Management: Implement user authentication and management to secure access.
Scheduled Data Harvesting: Automate data harvesting for selected YouTube channels at regular intervals.
Advanced Search and Filtering: Enhance search functionality with advanced criteria and filtering options.
Additional Data Sources: Extend the project to support data retrieval from other social media platforms or streaming services.
Advanced Data Analysis: Incorporate advanced analytics techniques and machine learning for deeper insights.
Export and Reporting: Add features to export data and generate reports in various formats.

##Conclusion

The "YouTube Data Harvesting and Warehousing" project offers a robust solution for accessing, storing, and analyzing YouTube channel and video data. By combining SQL, MongoDB, and Streamlit, this project empowers users to interact with YouTube data easily and gain valuable insights. Its flexibility, scalability, and data visualization capabilities make it a valuable tool for anyone interested in harnessing the wealth of information available on YouTube.
