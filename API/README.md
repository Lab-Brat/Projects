# API for data processing
This repository contains scripts I wrote to perform a search of a value in a relatively large CSV file using a web API. 

## Information about data
The CSV file is 1.45GB and has approximately 60 million rows and 3 columns. The first column is products name, second is another product, to which the first one
has a recommendation, and the last column is a value representing similarity of two prodcuts (0<sim<1). 

## API written with The Python Standard Library
* search_csv.py: A simple search algorithm. It reads the CSV file stored on a local machine and performs the search on it;
* socket_server.py: Basic server written with 'socket' module, supports only 1 connection at a time. After connection has to be relaunched;
* socket_client.py: A client, sends requests containing two parameters - a string to be found in the CSV file, and the similarity threshold.


## API written with Flask and requests
* flask_api.py: Search algorithm with the Flask API combined together;
* flask_request.py: A Request sent to Flask API to get the search result.

## misc
* yt_flask: Test code I wrote to get accustomed to Flask, does not do any useful functionality;
* analysis.ipynb: Using pandas to search through the CSV file, very inefficient (takes about 450s for search, and additional 200 to read the CSV file);
* read_csv.py: Couple ways to access the CSV from the web, and a better algorithm that was used in search_csv.py.


## Running the API
To run the program, first run socket_server.py in a terminal, then in another terminal window launch socket_client.py. To search for a specific key, in socket_client.py 
change INPUT variable to the desired product and similarity value. 
