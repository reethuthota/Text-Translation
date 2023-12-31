# Text Translation

This project is a text translator designed to convert between French and English while displaying the accuracy of translations. It utilizes a Streamlit frontend and Python backend, integrating GenAI, OpenAI, and Langchain.

## Features

- Translation between French and English
- Accuracy assessment of translations
- Streamlit-based user interface

## Technologies Used

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Libraries:**
  - [OpenAI](https://github.com/openai/llms): `langchain.llms`
  - [Langchain](https://github.com/langchain/langchain): `langchain`
    - langchain.prompts
    - langchain.chains

## Usage

### Prerequisites

Before running the application, ensure you have an OpenAI API key.

### Getting Started

1. Clone this repository to your local machine.
2. Create a `secret_key.py` file in the project root directory.
3. Add your OpenAI API key to the `secret_key.py` file:
   
   ```python
   # secret_key.py
   OPENAI_API_KEY = "YOUR_API_KEY_HERE"
   
4. Run the application using `streamlit run app.py`.

## How it Works

This application integrates various AI libraries, including OpenAI and Langchain. When a user selects a language for translation, the backend algorithms, powered by these libraries, collaborate to craft an accurate translated text in the specified language.
