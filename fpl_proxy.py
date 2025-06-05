from flask import Flask, request, jsonify
import requests
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CACHE = {}
CACHE_TTL = 60 * 10  # 10 minutes

def get_from_cache_or_fetch(url):
    now = time.time()
    if url in CACHE and now - CACHE[url]['time'] < CACHE_TTL:
        return CACHE[url]['data']
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        CACHE[url] = {'data': data, 'time': now}
        return data
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

@app.route('/api/fpl/<path:subpath>')
def proxy_fpl(subpath):
    fpl_url = f"https://fantasy.premierleague.com/api/{subpath}"
    if request.query_string:
        fpl_url += '?' + request.query_string.decode()
    data = get_from_cache_or_fetch(fpl_url)
    if data is not None:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch FPL data"}), 502

@app.route('/')
def index():
    return "FPL Proxy is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)