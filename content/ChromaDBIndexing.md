Title: Demystifying a Python Script: Web Scraping and Text Processing with Python
Date: 2023-09-13
Category: Blog

A web scraping and text processing Python script may look overwhelming at first, but in this blog post, we will break it down bit by bit. This Python script focuses on fetching, processing, and visualizing job application listing data from the website 'finn.no' using Python.

Let's get started.

```python
from langchain.vectorstores import ElasticsearchStore
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
import requests
from bs4 import BeautifulSoup
import xmltodict
from langchain.agents.agent_toolkits import create_retriever_tool, create_conversational_retrieval_agent
from langchain.chat_models import ChatOpenAI
import chromadb
from langchain.vectorstores import Chroma
from langchain.indexes import SQLRecordManager
from langchain.indexes import index
```
In this part, the script imports all the required modules. BeautifulSoup is used for parsing HTML and extracting data, xmltodict for mapping XML data to Python dictionaries, requests for firing HTTP requests, etc.

```python
def extract_text_from(url):
    response = requests.get(url)
    ...
    element = soup.select_one(...)
    ...
    if element:
        text = '\n'.join(child.get_text().strip() for child in element.children if child.name)
    else:
        text = ''
    ...
    return markdown_str, data
```
This function is the main web scraping function that extracts text from a given URL using BeautifulSoup, a Python library for parsing HTML and XML documents.

```python
r = requests.get("https://www.finn.no/feed/job/atom.xml?rows=500")
xml = r.text
raw = xmltodict.parse(xml)
```
This code fetches and parses a job feed from 'finn.no'. It begins by making a GET request to the webpage. The response, in XML format, is then parsed into a Python dictionary using the xmltodict module.

```python
pages = []
counter = 0
for info in raw['feed']['entry']:
    url = info['link']['@href']
    if 'https://www.finn.no/' in url:
        markdown, data = extract_text_from(url)
        pages.append({...})
    counter += 1
    print(f"Done with url: {url}. {counter} of X done.")
```
The script then loops over each job listing, retrieves the URL, and uses the `extract_text_from` function to parse the data. Every extracted piece of information is stored in a list called `pages`.

```python
docs, metadatas = [], []
for page in pages:
    ...
    docs.extend([page['text']])
    metadatas.extend([{...}])
```
This part of the script prepares the data for the next processing stage. We arrange the information into two lists, `docs` and `metadatas`.

```python
documents = [Document(page_content=string, metadata=meta) for string, meta in zip(docs, metadatas)]
```
Each page of processed data is wrapped into a `Document`, allowing easier handling of data in the next steps.

```python
embeddings = OpenAIEmbeddings()
collection_name = "finn-test-index"
persistent_client = chromadb.PersistentClient()
collection = persistent_client.get_or_create_collection(collection_name)

langchain_chroma = Chroma(...)
record_manager = SQLRecordManager(...)
record_manager.create_schema()
```
The script then sets up a vector store. This involves setting up an embedding method, a client for the DB, fetch/creating the required collection, and initializing a `langchain_chroma` object.

```python
index(documents, record_manager, langchain_chroma, cleanup="full", source_id_key="source")
```
Here, the script indexes the documents using the `index` function. This makes the documents searchable by a retriever tool on the vector store created earlier.

```python
retriever = langchain_chroma.as_retriever(search_kwargs={'k': 3})

tool = create_retriever_tool(retriever, "search_finn", "Søk etter relevante stillinger på finn.no.")
tools = [tool]
```
We then initialize a retriever tool that will search the indexed documents when deployed.

```python
llm = ChatOpenAI(temperature = 0, model_name = "gpt-4")
agent_executor = create_conversational_retrieval_agent(llm, tools, verbose=True)
result = agent_executor({"input": "Jeg ser etter en fast jobb som servitør."})
```
Finally, the Python script sets up a GPT-4 model as the language model, then uses the retriever tool established earlier to create a conversational retrieval agent to search for content based on user input. 

To summarize, this script is a showcase of how we can combine web scraping, data extraction, and powerful language processing tools to create an insightful application with Python. Web scraping is an invaluable tool that, when used correctly, can provide us with vast amounts of data that isn't readily available while combining it with the likes of language models can help derive valuable insights from unstructured text data.
