# import ollama

# response = ollama.chat(
#     model='deepseek-r1:1.5b',
#     messages=[{'role': 'user', 'content': 'Tell me about machine learning.'}]
# )

# print(response['message']['content'])


from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ollama():
    data = request.json
    model = data.get('model', 'llama3.2:1b')  # Default model
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    response = requests.post(OLLAMA_URL, json={
        'model': model,
        'prompt': prompt,
        'stream': False
    })

    if response.status_code != 200:
        return jsonify({'error': 'Ollama API error'}), 500

    return jsonify({'response': response.json().get('response')})

if __name__ == '__main__':
    app.run(debug=True)
