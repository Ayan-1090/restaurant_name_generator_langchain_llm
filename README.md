# Restaurant Name Generator

This project is a Streamlit web app that generates creative restaurant names and menu ideas based on the selected cuisine type. It uses OpenAI's language model via the LangChain framework.

## Features

- Select a cuisine type (Italian, Chinese, Mexican, Indian, French)
- Generate a fancy restaurant name
- Generate a creative menu for the restaurant

## Technologies Used

- **Streamlit** (UI)
- **LangChain** (LLM orchestration)
- **OpenAI GPT-3/4** (LLM backend)
- **Python-dotenv** (for environment variable management)

## Requirements

- Python 3.11+
- streamlit >= 1.30.0
- langchain >= 0.1.0
- langchain-openai >= 0.0.8
- openai >= 1.0.0
- python-dotenv >= 1.0.0

## Setup

1. Clone the repository and navigate to the `Restaurant_Name_Generater` directory.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the Streamlit app with:

```sh
streamlit run main.py
```

## File Structure

- `main.py` — Streamlit app entry point
- `langchain_llm_ai.py` — LLM and chain logic for generating names and menus
- `.env` — Your OpenAI API key (not included in version control)

## Example

1. Select a cuisine from the sidebar (e.g., "Italian").
2. Click on "Generate Restaurant Name and Menu".
3. The app will display a creative restaurant name and a menu.

## License

MIT
