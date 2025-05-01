# Semantic Kernel Space Information Agent

This Python project, managed with Poetry, serves as a basic agent that can inform users about space. Currently, it fetches the APOD ([Astronomy Picture of the Day](https://api.nasa.gov/planetary/apod)) from NASA and fun facts about space and presents it to the user. It also allows for basic questions about space and relies on a large language model (LLM) for the answers. 

## Technologies Used

- Python
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) - Microsoft's lightweight SDK for AI services integration
- [Streamlit](https://streamlit.io/) - Web app framework for machine learning and data science
- [Poetry](https://python-poetry.org/) - Python dependency management
- NASA APOD API

## Features

- 🌌 Web-based interface with Streamlit
- 🛰️ Automatic function calling for plugin operations
- 📸 Astronomy Picture of the Day with image display
- 💡 Random space facts from curated collection
- 🤖 AI-powered space Q&A using OpenAI models
- 📚 Conversation history preservation

## Setup

1.  Clone this repository.
2.  Navigate to the project directory.
3.  Install the project dependencies using Poetry:
    ```bash
    poetry install
    ```
4.  Create a `.env` file in the project root and add your NASA API key:
    ```
    .env
    NASA_API_KEY=your_key_here
    OPENAI_API_KEY=sk-your-key-here
    OPENAI_CHAT_MODEL_ID=gpt-4o-mini
    ```

## Usage

1.  Activate the Poetry shell (optional, but recommended for isolated environment):
    ```bash
        poetry shell
    ```
2.  Run the agent:
    ```bash
        poetry run streamlit run src/space_bot/main.py
    ```
3.  After launching the app:
    1. Type general space questions to chat with the AI
    2. Use special commands:
       - `apod`: Show today's astronomy picture
       - `fact`: Get a random space fact
    3. Interactive chat maintains conversation context

🔧 **Architecture**
- Plugins system for extendable functionality
- Semantic Kernel for AI orchestration
- Streamlit for web interface
