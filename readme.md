# Chat API Project

## Project Information

This project is a FastAPI-based backend for handling chat queries, along with a Streamlit frontend for interacting with the API.

### Features

- **Backend**: A FastAPI application that provides endpoints for health checks, project information, and chat handling.
- **Frontend**: A Streamlit application that serves as a user-friendly interface to interact with the chat API.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Steps

1. Clone the repository:

   ```
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```
     venvScriptsactivate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Configure environment variables:
   - Copy the `env.sample` file to `.env`:
     ```
     cp env.sample .env
     ```
   - Update the `.env` file with the required environment variables.

---

## Running the Project

### Backend (FastAPI)

1. Navigate to the project directory.
2. Run the FastAPI application:
   ```
   python main.py
   ```
3. The backend will be available at `http://localhost:8000`.

### Streamlit Frontend

1. Navigate to the project directory.
2. Run the Streamlit application:
   ```
   streamlit run streamlit_app.py
   ```
3. The frontend will be available in your default web browser.

---

## API Endpoints

### Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Response**: `{ "status": "healthy" }`

### Project Info

- **Endpoint**: `/`
- **Method**: `GET`
- **Response**: Project metadata (name, version, description).

### Chat API

- **Endpoint**: `/chat`
- **Method**: `GET`
- **Parameters**:
  - `chat_id`: The ID of the chat session.
  - `query`: The user's query.
- **Response**: Chat response from the backend.

---

## Notes

- Ensure the backend is running before using the Streamlit frontend.
- The backend and frontend communicate via `http://localhost:8000`. Update the URL in `streamlit_app.py` if the backend runs on a different host or port.
