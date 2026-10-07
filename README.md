# 📰 News Search Agent

A beginner-friendly Python Agentic AI project that searches latest news by topic using the News API.

## Project Goal

Create an agent that searches latest news by topic.

## Workflow

User enters topic  
↓  
News Agent receives topic  
↓  
Agent calls News API  
↓  
API sends news articles  
↓  
Agent displays title, source, date, and link

## Tools Required

- Python
- VS Code
- Internet
- News API
- requests library
- python-dotenv

## Project Structure

```text
News-Search-Agent/
├── news_search_agent.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Install Libraries

```bash
pip install requests python-dotenv
```

## Create Free News API Key

Go to:

https://newsapi.org

Create a free account and copy your API key.

## Configure .env

Open `.env` and replace `YOUR_API_KEY` with your real News API key:

```env
NEWS_API_KEY=YOUR_API_KEY
```

Do NOT upload `.env` to GitHub. It is already included in `.gitignore`.

## Run the Project

```bash
python news_search_agent.py
```

## Example

```text
Welcome to News Search Agent
Type exit to stop

Enter news topic: Artificial Intelligence

Top 5 News:

Title: New AI tools changing education
Source: Tech News
Published: 2026-01-01T10:00:00Z
Link: https://example.com/news1
--------------------------------------------------
```

## Explanation

### import requests

Used to connect Python with the News API.

### API Key

The API key is used like a password to use News API. In this project it is safely loaded from `.env`.

### input()

```python
topic = input("\nEnter news topic: ")
```

Takes the topic from the user.

### requests.get()

```python
response = requests.get(url)
```

Sends the request to the news website/API.

### response.json()

```python
data = response.json()
```

Converts the API result into a Python dictionary.

### for loop

```python
for article in articles[:5]:
```

Shows only the first 5 news articles.

## Improved Version

The project uses the PDF's improved loop-based version:

- Welcome message
- `exit` option
- Topic input
- News API request
- No-news handling
- Top 5 results
- Title
- Source
- Published date
- Link
- API error message

The only change from the PDF code is that the API key is loaded securely from `.env` instead of being written directly in the Python file.

## Agentic AI Thinking

### User Goal

```text
Search latest news about Agentic AI
```

### Agent Steps

1. Understand topic = Agentic AI
2. Call news API
3. Collect articles
4. Select top 5 results
5. Display title, source, date, and link

## Project Extensions

1. Add category search
2. Add country-wise news
3. Add Streamlit interface
4. Add voice search
5. Add email news summary
6. Add WhatsApp news bot
7. Add AI summary of each article
8. Add daily news automation

## Concepts Learned

- Python
- API
- API Key
- requests
- JSON
- loops
- input
- conditional statements
- News API
- Agentic AI workflow
- Environment variables
