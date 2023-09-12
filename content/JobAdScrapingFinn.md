Title: Introduction to Web Scraping and Text Extraction with Python
Date: 2023-09-12
Category: Blog

One of the most common tasks in data analysis is extracting information from public websites. In Python, we have several libraries, like Beautiful Soup and requests, that make it simple to scrape web data. In this article, we're going to discuss how to extract website data with Python using these libraries. We're also going to cover XML data parsing using xmltodict, and we'll be using langchain.vectorstore, langchain.embeddings, and langchain.schema for vector store manipulation and document embeddings.

Let's consider the Python script below. Here's an overview of what it does: 

1. Fetches an XML feed of job listings from "https://www.finn.no/feed/job/atom.xml?rows=1500".

2. Parses the XML data to retrieve listing URLs.

3. Visits each URL to scrape job details.

4. Structures the data and enhances it for further analysis.

```python
from langchain.vectorstores import ElasticsearchStore
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
import requests
from bs4 import BeautifulSoup
import xmltodict
from langchain.agents.agent_toolkits import create_retriever_tool, create_conversational_retrieval_agent
from langchain.chat_models import ChatOpenAI
```

The above lines are importing all the necessary libraries for our script. We'll be using the requests library to send HTTP requests, BeautifulSoup to parse HTML and extract the information we want, xmltodict to parse the XML data feed, and langchain related libraries for retrieving and manipulating the scraped data.

Next, we define a method `extract_text_from(url)`. This function accepts a URL and uses requests and BeautifulSoup to parse the HTML and extract the required data.

```python
def extract_text_from(url):
    # rest of the code...
```

In this function, we start by making a request to the passed url and using BeautifulSoup to parse the HTML. We then use the `select_one` method to select specific parts of the HTML that correspond to the data we want to extract.

Once we have all the desired data, we create a dictionary to store it, and a markdown string for display. The extracted data is then returned from the function.

Next, the script fetches and parses an XML feed of job listings:

```python
r = requests.get("https://www.finn.no/feed/job/atom.xml?rows=1500")
xml = r.text
raw = xmltodict.parse(xml)
```

In the loops that follow, the script visits each job listing URL, extracts the details using the `extract_text_from` function, and stores the result in the `pages` array.

Now that we have the job data, we separate the text content and metadata for each page:

```python
docs, metadatas = [], []
# rest of the code...
```

Afterwards, the documents are converted into Document objects and embedded into an ElasticsearchStore. Once stored, the ElasticsearchStore is converted to a retriever that can be queried to find similar documents:

```python
documents = [Document(page_content=string, metadata=meta) for string, meta in zip(docs, metadatas)]
# rest of the code...
```

Lastly, the script creates a ChatOpenAI instance and a retrieval tool, and combines them into a conversational retrieval agent that can be used to find similar job listings based on user input:

```python
llm = ChatOpenAI(temperature = 0, model_name = "gpt-3")
agent_executor = create_conversational_retrieval_agent(llm, tools, verbose=True)
# agent interaction here...
```

So, there you have it! The script does a great job scraping and extracting relevant data from a series of web pages to fulfill a specific purpose. This blog only covers the high level of the script, and you can deep dive into each step to get a full understanding of the concepts and techniques used here.
