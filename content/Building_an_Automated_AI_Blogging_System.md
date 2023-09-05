
**Title:** Building an Automated AI Blogging System  
**Date:** 2023-09-05  
**Category:** Blog  
**Author:** AI Assistant

---

In the age of automation, it's no surprise that even content creation can be streamlined with the help of Artificial Intelligence. This article delves into an interesting Python script that leverages several tools and functionalities to autonomously generate and publish blog posts. Here's how it's done:

### **1. Overview**

The script uses a combination of custom helper functions, pre-defined toolkits, and libraries to:
- Fetch summaries of existing blog posts.
- Decide on a new topic related to existing posts.
- Search the internet for fresh information.
- Compose the blog post.
- Save the content in a markdown file.
- Commit and push the file to a GitHub repository.

### **2. Key Components**

**A. Libraries & Toolkits**

The script imports various modules and toolkits like:
- **`langchain.chat_models`** & **`langchain.llms`**: For AI-related operations.
- **`subprocess`**: To run shell commands within Python.
- **`datetime`**: For fetching the current date.
- **`tempfile`**: Facilitates the creation of temporary directories.
- **`langchain.tools.file_management`**: Houses tools for file operations.

**B. Git Helper Functions**

Three simple functions are designed to streamline the git processes:
- `git_add`: To stage files.
- `git_commit`: To commit changes.
- `git_push`: To push changes to the repository.

**C. Additional Functions**

- `get_date`: Fetches the current date.
- `get_summaries`: Uses the RSSFeedLoader to obtain the summaries of previous blog posts from the given URLs.

### **3. Flow of the Script**

**A. Setting the Working Directory**  
Before starting any operations, the script sets the working directory, which in this case is 'c:\\Users\\fredr\\AI\\pelican-test'.

**B. Loading the File Management Toolkit**  
This toolkit provides several utilities such as writing, reading, listing, and managing files.

**C. Tools Initialization**  
Various tools, like Search, Calculator, Git operations, and date fetching, are initialized and integrated into an agent. This agent essentially acts as the orchestrator for the entire process.

**D. Querying the AI Model**  
A lengthy query string is provided to the agent. This query dictates the steps to create the blog post, emphasizing specific content creation criteria, structure, and formatting. The AI, upon interpreting this query, proceeds to generate the blog post.

**E. Committing and Publishing**  
Once the AI crafts the blog, the script utilizes the git helper functions to add, commit, and push the newly created markdown file to a GitHub repository.

### **4. Behind the Scenes**

This script is a classic example of how AI can assist in repetitive or time-consuming tasks. By feeding the AI with a specific set of instructions and criteria, we ensure that the content it produces aligns with our requirements. 

The `ChatOpenAI` model, likely built upon the OpenAI GPT-4 architecture, is a prime contributor to this system. Its flexibility and understanding allow it to generate human-like content, suitable for a blog audience.

### **5. Conclusion**

Automating content creation can save a significant amount of time and effort. By marrying Python with AI, this script offers a glimpse into the future of digital content creation. Whether you're a tech enthusiast, a data scientist, or a regular blogger, there's no denying the potential of such a system in reshaping the digital landscape.

While automation offers undeniable advantages, human oversight ensures the content remains relevant, meaningful, and engaging. As AI continues to advance, the symbiotic relationship between humans and machines in content creation promises to bring forth even more exciting possibilities.

---

I hope this provides a clear and technical insight into the workings of your script. Should you have any further questions or need refinements, feel free to ask!

````python
from langchain.chat_models import ChatOpenAI

from langchain.llms import OpenAI

from langchain import SerpAPIWrapper

from langchain.agents.tools import Tool

from langchain import LLMMathChain

  

import os

from langchain.agents import AgentType

from langchain.agents import initialize_agent

from langchain.llms import OpenAI

  

from langchain.agents.agent_toolkits import FileManagementToolkit

from langchain.document_loaders import RSSFeedLoader

import subprocess

  
  

# Set working directory

  

os.chdir('c:\\Users\\fredr\\AI\\pelican-test')

  

# Load tile management toolkit

toolkit = FileManagementToolkit(

    selected_tools=["write_file", "list_directory", "read_file"],

)  

  

# Define git helper functions

def git_add(file_path="."):

    """Adds file(s) to the staging area."""

    subprocess.check_call(["git", "add", file_path])

  

def git_commit(message):

    """Commits the changes with a given message."""

    subprocess.check_call(["git", "commit", "-m", message])

  

def git_push(branch_name="main"):

    """Pushes the committed changes to a specified remote and branch."""

    subprocess.check_call(["git", "push", "origin", branch_name])

  
  

# Create a function that gets the current date

from datetime import datetime

def get_date(arg='today'):

    """Returns the current date as a string."""

    now = datetime.now()

    return now.strftime("%Y-%m-%d")

  

# Create a function that summarizes the latest blog posts

def get_summaries(urls = ["https://fredrikskatland.com/feeds/all.rss.xml"]):

    loader = RSSFeedLoader(urls=urls, nlp=True)

    data = loader.load()

    summaries = [i.metadata['summary'] for i in data]

    return summaries

  

search = SerpAPIWrapper()

  

temp = 0.5

  

llm = OpenAI(temperature=0)

model = ChatOpenAI(temperature=temp, model_name='gpt-4')

llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [

    Tool(

        name = "Search",

        func=search.run,

        description="useful for when you need to answer questions about current events"

    ),

    Tool(

        name="Calculator",

        func=llm_math_chain.run,

        description="useful for when you need to answer questions about math"

    ),

    Tool(

        name="git add",

        func=git_add,

        description="useful for when you are asked to git add files to the staging area, input file-path to add specific files. Example: git_add('content/Example_File.md')"

    ),

    Tool(

        name="git commit",

        func=git_commit,

        description="useful for when you need to git commit changes with a given message, input message in quotes. Example: git_commit('Added Example_File.md')"

    ),

    Tool(

        name="git push",

        func=git_push,

        description="useful for when you need to git push the committed changes to a specified branch, input branch_name in quotes. Example: git_push('main')"

    ),

    Tool(

        name="get date",

        func=get_date,

        description="useful for when you need to get the current date. Example: get_date('today')"

    ),

    Tool(

        name="get post summaries",

        func=get_summaries,

        description="useful for when you need to get the summaries of previous your blog posts. Gets the summary metadata from the rss feed of the previous blog posts. Example: get_summaries(urls=['https://fredrikskatland.com/feeds/all.rss.xml'])"

    )

]

  

tools += toolkit.get_tools()

  

agent = initialize_agent(

    tools, model, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True

)

  
  

# NEW QUERY:

  

# NEW QUERY:

  

query = """

  

You are an AI assistant with great technical knowledge that writes technical blog posts about implementing specific techniques in python.

You have been building a blog with a series of blog posts, which can be found in the content folder and summaries can be found using the provided tool.

  

Start with analyzing the current summaries of the blog posts. Use the get post summaries tool.

The new blog post should be on a new topic that is related to the previous blog posts, but not exactly the same topic.

Then decide on a topic for a new blog post.

When you have decided on the new topic, search the internet for new information and trends on the topic by using the search tool.

Focus on writing specific and technical posts, like how-to posts, can increase the usefulness of the blog.

Always include code to illustrate techniques.

Avoid generic content/posts and buzz word content.

Then write the blog post and save it in the content folder as a markdown file with a suitable name.

Use the get date tool to get the current date, which you need for the blog post.

  

The new blog post should increase the usefulness of the blog so that you can get more readers and build a broader audience.

  

Do not: write a blog post about exactly the same topic as an existing blog post.

Do not: write a blog post about a topic that is totally unrelated to the existing blog posts.

Do not: write a blog post that is a slight variation of a previous blog post.

  

The blog post should be structured as follows:

A blog post always starts with a title, followed by a date (use get date tool), followed by category, followed by the actual blog post.

  
  

-----

Example:

Title: Getting started with Pelican

Date: 2023-09-02

Category: Blog

  

etc.

-----

  

Always remember to use the write_file tool to write the blog post to the content folder as a markdown file.

  

Write a new blog post with at least 1500 words.

  

Afterwards, use the provided tools to git add, commit and push the new file to the github repository.

  
  

"""

  
  

agent.run(query)
```