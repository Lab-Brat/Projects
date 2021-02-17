# API for data processing
This repository contains scripts I wrote to perform a search of a value in a relatively large CSV file using a web API. 

## Information about data
The CSV file is 1.45GB and has approximately 60 million rows and 3 columns. The first column is products name, second is another product, to which the first one
has a recommendation, and the last column is a value representing similarity of two prodcuts (0<sim<1). 

## API without using only Python Standard Library
* search_csv.py: A simple search algorithm. It reads the CSV file stored on a local machine and performs the search on it;
* socket_server.py: Basic server written with 'socket' module, supports only 1 connection at a time. After connection has to be relaunched;
* socket_client.py: A client, sends requests containing two parameters - a string to be found in the CSV file, and the similarity threshold.

## Running the API
To run the program, first run socket_server.py in a terminal, then in another terminal window launch socket_client.py. To search for the required key, in socket_client.py 
change INPUT variable to the desired product and similarity value. 
