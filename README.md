# Ollama Web Interface

A simple web interface for interacting with Ollama models using Flask. This project provides a user-friendly way to interact with various Ollama models through a web browser.

## Prerequisites

- Python 3.7 or higher
- Ollama installed and running locally
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ganessa037/Ollama.git
cd ollama
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install flask requests
```

4. Make sure Ollama is running locally:
- Download and install Ollama from [ollama.ai](https://ollama.ai)
- Start the Ollama service
- The service should be running on `http://localhost:11434`

## Running the Application

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Features

- Simple web interface for interacting with Ollama models
- Support for different Ollama models
- Real-time responses from the AI model
- Default model: llama3.2:1b

## Project Structure

```
ollama-web-interface/
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── index.html     # Main web interface
└── README.md          # This file
```

## Usage

1. Open the web interface in your browser
2. Select your preferred Ollama model
3. Enter your prompt in the text area
4. Click "Ask" to get a response from the model

## Screenshots

[Add screenshots of your application here]

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Ollama](https://ollama.ai) for providing the AI models
- [Flask](https://flask.palletsprojects.com/) for the web framework 