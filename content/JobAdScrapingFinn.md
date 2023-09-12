Title: Web Scraping Job Postings with Python
Date: 2023-09-12
Category: Blog

## Introduction

This blog post will discuss a Python script that scrapes job postings from a website and stores the data in an Elasticsearch database. The script uses the BeautifulSoup library to parse the HTML of the web pages and extract the relevant information. The script also uses the requests library to send HTTP requests to the website and retrieve the HTML of the web pages. The extracted data is then converted into a markdown format and stored in an Elasticsearch database.

## Code Explanation

The script starts by importing the necessary libraries. The BeautifulSoup library is used to parse the HTML of the web pages and extract the relevant information. The requests library is used to send HTTP requests to the website and retrieve the HTML of the web pages.

The script defines a function called `extract_text_from` that takes a URL as an argument. This function sends a GET request to the URL and parses the HTML of the web page. It then uses BeautifulSoup's select_one method to navigate to the specific elements of the web page and extract the text from these elements. The extracted text is then converted into a markdown format.

The script then sends a GET request to the website's Atom feed and parses the XML response. It loops through each entry in the feed, sends a GET request to the URL of the entry, and calls the `extract_text_from` function to extract the text from the web page. The extracted text and other data are then stored in a dictionary and added to a list.

Finally, the script creates an ElasticsearchStore from the documents, generates embeddings for the documents using the OpenAIEmbeddings, and creates a retriever tool that can be used to search for relevant job postings.

## Code Execution

To run the script, you would need to have the necessary libraries installed and an Elasticsearch server running. You can call the `extract_text_from` function with a URL to extract the text from a web page. The function returns the extracted text in a markdown format and a dictionary with additional data.

The script also creates a retriever tool that can be used to search for relevant job postings. You can use the `search_finn` method of the retriever tool to search for job postings. The method takes a query as an argument and returns the top 3 most relevant job postings.

## Conclusion

This blog post discussed a Python script that scrapes job postings from a website and stores the data in an Elasticsearch database. The script uses the BeautifulSoup and requests libraries to scrape the web pages and extract the relevant information. The extracted data is then converted into a markdown format and stored in an Elasticsearch database. The script also creates a retriever tool that can be used to search for relevant job postings. This script is a useful tool for anyone interested in web scraping or data storage and retrieval, and can be easily modified to scrape other websites or store the data in a different format or database.
