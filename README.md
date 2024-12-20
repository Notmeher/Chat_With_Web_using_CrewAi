# Chat-With-Web-using-Local_LLM-llama-3.2

# GenZMarketing Chatbot Project

## Overview

The GenZMarketing Chatbot project is a sophisticated solution designed to leverage a local Large Language Model (LLM) and Crew AI to provide tailored answers based on data scraped from the GenZMarketing website. This project demonstrates the power of natural language processing, vector databases, and custom retrieval mechanisms to deliver precise and dynamic responses.

## Features

- **Website Data Scraping**: Automatically scrapes content from multiple URLs of the GenZMarketing website.
- **Vectorization**: Converts scraped data into vectorized form for efficient search and retrieval.
- **Retriever Design**: Utilizes a retriever for searching relevant content based on user queries.
- **Chatbot Integration**: Implements a chatbot using the Ollama LLM for generating user-focused responses.
- **Streamlit UI**: User-friendly interface for entering queries and viewing results.

## Technologies Used

- **Programming Languages**: Python
- **Frameworks and Libraries**:
  - [LangChain](https://github.com/hwchase17/langchain)
  - [Streamlit](https://streamlit.io/)
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
  - [ChromaDB](https://www.trychroma.com/)
  - [Ollama Embeddings and LLM](https://ollama.com/)
- **Environment Variables**: Stored securely in a `.env` file.

## File Structure

- `app.py`: Main application file for Streamlit UI.
- `crew.py`: Workflow implementation to manage the sequence of scraping, vectorization, retrieval, and chatbot integration.
- `tasks.py`: Definitions of individual tasks such as scraping, vectorization, retriever setup, and chatbot implementation.
- `tools.py`: Utility functions for scraping, saving data, vector database creation, and more.
- `agents.py`: Agent definitions for each stage of the process.
- `requirements.txt`: List of dependencies.
- `.env`: Environment configuration file (contains API keys and settings).
- `data_hash.txt`: Hash to ensure data consistency during vectorization.
- `website_data.json`: JSON file containing scraped data.
- `QA.txt`: Sample questions for testing the chatbot.

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. pip or another package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
 
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the application in your browser (usually at `http://localhost:8501`).
2. Enter a question in the input field.
3. Click **Start Analysis and Ask**.
4. View the response generated by the chatbot based on the scraped website data.

## Key Components

### Scraping
- URLs are specified in `crew.py` and processed using `BeautifulSoup`.

### Vectorization
- Scraped data is vectorized using Ollama embeddings and stored in ChromaDB.

### Retrieval
- A retriever fetches the most relevant content for a given query.

### Chatbot
- Chatbot implementation uses Ollama LLM to provide a natural conversational experience.

## Testing

Sample questions for testing can be found in `QA.txt`. These include queries about GenZMarketing's services, contact information, and blog content.


## License

This project is licensed under the MIT License. See `LICENSE` for more details.

![result](https://github.com/user-attachments/assets/0954dd5e-112e-40e9-95b8-7ae56ef56ad4)


![result5](https://github.com/user-attachments/assets/39443eba-6803-49e4-9240-fd1399e7a1ee)
![result4](https://github.com/user-attachments/assets/fed14c44-54c0-4462-b723-18c91c85b16f)
![result3](https://github.com/user-attachments/assets/f721092a-1ec3-4102-98d0-38ca6b67a2cd)
![result2](https://github.com/user-attachments/assets/fa4b9bcc-ea48-480b-a60e-888e7e1763e3)
![result1](https://github.com/user-attachments/assets/ec50acdd-8f00-4913-b14c-d7981581e930)

