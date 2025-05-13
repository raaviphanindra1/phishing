from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils.check_url import analyze_url


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')  # ✅ This serves the frontend page

@app.route('/api/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    result = analyze_url(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
