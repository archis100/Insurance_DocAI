# InsuranceDoc-AI

An AI-powered application designed to process insurance policy documents and answer user questions using a Retrieval-Augmented Generation (RAG) pipeline. This project consists of a FastAPI backend and a React frontend.

-----

### Key Features

  * **Document Processing:** Takes a public PDF URL, extracts text, and processes it for AI querying.
  * **Vector Database:** Embeds document text chunks and stores them in a Pinecone vector index.
  * **Intelligent Q\&A:** Uses the Gemini AI model to answer questions based **only** on the content of the provided document.
  * **Efficient Lookups:** Utilizes a consistent document ID to check if a document has already been processed, skipping redundant work.
  * **Responsive Frontend:** A simple, clean chat interface built with React to interact with the API.

-----

### Tech Stack

**Backend:**

  * **Python:** The core language for the API.
  * **FastAPI:** A modern, fast web framework for building the API endpoints.
  * **Google Gemini API:** The Large Language Model (LLM) used for generating answers.
  * **Pinecone:** A serverless vector database used for storing document embeddings.
  * **`requests` & `fitz`:** Libraries for downloading and parsing PDF files.

**Frontend:**

  * **Streamlit:** An interactive Streamlit UI interface

-----

### Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

  * [Python 3.9+](https://www.python.org/downloads/)
  * A **Google API Key** for Gemini AI
  * A **Pinecone API Key** and a Pinecone Index


### Local Setup

The project is structured with a `rag-chatbot` folder for the `backend` folder and  `frontend` folder.

#### 1\. Backend Setup

1.  Navigate to the root folder directory.
    ```bash
    cd rag-chatbot
    ```
2.  Create a Python virtual environment and activate it.
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  Install the required Python packages.
    ```bash
    pip install -r requirements.txt
    ```
4.  Create a **`.env`** file in the `rag-chatbot` directory and add your API keys.
    ```
    HACKATHON_API_KEY="your-secret-api-key"
    GOOGLE_API_KEY="your-google-api-key"
    PINECONE_API_KEY="your-pinecone-api-key"
    ```
5.  Start the FastAPI server.
    ```bash
    uvicorn backend.main:app --reload
    ```
    The backend will run on `http://127.0.0.1:8000`.

#### 2\. Frontend Setup

1.  Open a new terminal and navigate to the `frontend` directory.
    ```bash
    cd frontend
    ```
2.  Create a **`.env`** file in the `frontend` directory and add the following variables, pointing to your local backend.
    ```
    FRONTEND_API_URL=http://localhost:8000
    HACKATHON_API_KEY="your-secret-api-key"
    ```
3.  Navigate back to the root directory `rag-chatbot`
    ```bash
    cd ..
    ```
4.  Start the Streamlit server.
    ```bash
    streamlit run frontend/streamlit_app.py
    ```
    The frontend will run on `http://localhost:8501`.

-----

### API Endpoint

The primary backend endpoint for interaction is:

  * **POST** `/hackrx/run`
      * **Description:** Processes a document from a URL and answers a list of questions.
      * **Request Body (JSON):**
        ```json
        {
          "documents": "string_url_to_pdf",
          "questions": ["What is the policy period?", "What is the premium?"]
        }
        ```
      * **Headers:**
          * `Authorization: Bearer YOUR_HACKATHON_API_KEY`
      * **Response (JSON):**
        ```json
        {
          "answers": ["Answer to question 1.", "Answer to question 2."]
        }
        ```

-----

## 🚀 Deployment on Hugging Face

This project is configured for deployment on **Hugging Face Spaces** using **FastAPI** for the backend and **Streamlit** for the frontend, all within the `rag-chatbot` root directory.

- **Backend (FastAPI):**  
  - Provides API endpoints (`/hackrx/run`) for document processing and question answering.  
  - Runs inside the Hugging Face container and listens on port **7860**.  

- **Frontend (Streamlit):**  
  - User interface defined in `streamlit_app.py`.  
  - Sends requests directly to the FastAPI backend in the same Space.  

## 🧪 Example Usage

**Sample Policy Document:**  
[RBC Insurance — Term 100 Policy (PDF)](https://www.rbcinsurance.com/samplepolicy/pdf/t100-policy.pdf)

**Sample Question:**
What are the benefits provided by this policy ?
What are the terms used in this policy ?

**Sample Output (screenshot):**
![RAG Chatbot Demo](assets/demo_screenshot.jpg)





