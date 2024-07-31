# Chat Application with Flask and Generative AI

This README file provides an overview of the Flask-based web application that leverages Google's Generative AI model. The application serves as a simple chat interface, where users can interact with a sophisticated AI model trained on a diverse dataset, with a focus on ancient Egyptian history and archaeology.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Endpoints](#endpoints)
6. [Configuration](#configuration)
7. [License](#license)

## Introduction

This project demonstrates how to integrate Google's Generative AI model with a Flask web application. The AI model is customized to act as a knowledgeable archaeologist and historian with a focus on ancient Egypt. The web application allows users to interact with this model via a chat interface.

## Requirements

To run this application, you need:

- Python 3.x
- Flask
- Google Generative AI SDK

You can install the required Python packages using pip:

```bash
pip install flask google-generativeai
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Make sure you have the required Python packages installed:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key:**

   Replace `"AIzaSyADKNOhNpVUvCSquyYNAMfvWZxrEg35rlI"` in the `init_model` function with your own Google API key.

4. **Create Static Directory:**

   Ensure you have a `static` directory for serving static files like CSS and JavaScript.

## Usage

1. **Start the Flask Application:**

   Run the application with:

   ```bash
   python app.py
   ```

2. **Access the Application:**

   Open your web browser and navigate to `http://localhost:5000` to see the chat interface.

## Endpoints

- **GET /**

  Serves the main HTML page (`index.html`).

- **POST /chat**

  Receives a JSON payload with a user message and returns a response from the AI model.

  **Request Format:**

  ```json
  {
    "message": "Your question or message here"
  }
  ```

  **Response Format:**

  ```json
  {
    "messages": [
      {"role": "user", "parts": ["Your question or message here"]},
      {"role": "model", "parts": ["Response from the AI model"]}
    ]
  }
  ```

## Configuration

The AI model is configured with the following settings:

- **Generation Configuration:**
  - `temperature`: 1
  - `top_p`: 0.95
  - `top_k`: 0
  - `max_output_tokens`: 8192

- **Safety Settings:**
  - Harassment
  - Hate Speech
  - Sexually Explicit
  - Dangerous Content

- **System Instruction:**
  The AI model is instructed to act as a knowledgeable archaeologist and historian, with a special emphasis on ancient Egypt.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify and extend this application as needed. Enjoy building with Flask and Google's Generative AI!
