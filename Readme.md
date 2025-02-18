# GreenLife Foods Order Chatbot

This project is a chatbot built using Streamlit and powered by the Llama-3.1 model to capture orders for GreenLife Foods. The chatbot helps users browse a product catalog, place orders, and interact with the assistant.

## Prerequisites

Before running the application, ensure you have the following prerequisites:

- **Llama-3.1-8b Model** (from Ollama)
- **Python 3.7+**
- **Streamlit**

### Install Llama Model

1. **Install Ollama** (for macOS):
   If you are on macOS, you can install Ollama via Homebrew:

   ```bash
   brew install ollama
   ```
2. **Start Ollama**:

   ```
    brew services start ollama
   ```

3. **Run Llama-3.1 Model**:
   After installing Ollama, run the following command to make sure the Llama-3.1 model is available:

   ```bash
   ollama run llama3.1
   ```

   This will use the `llama3.1-8b` variant of the model, which is the one used in this application. For more details on the Llama-3.1 model, visit the [Llama 3.1 documentation](https://ollama.com/library/llama3.1).

---

## Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

---

## Install Dependencies

1. Install the required Python dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

Once all dependencies are installed, run the Streamlit app:

```bash
streamlit run app.py
```

This will start a local Streamlit server, and you can access the chatbot through your browser at `http://localhost:8501`.

---

## Features

- **Product Catalog**: A list of GreenLife Foods products, including name, description, and price.
- **Order Placement**: Place orders by selecting products and specifying quantities. The order summary is displayed in the sidebar.
- **Conversation History**: View the conversation history, which includes details of the placed orders.
- **Inventory Check**: Ensure that users can only order products if sufficient stock is available.
  
---