# FPL Proxy

FPL Proxy is a lightweight Flask-based proxy for the official Fantasy Premier League (FPL) API. It enables CORS, adds simple in-memory caching, and makes it easier to consume FPL data from web apps or other services. The proxy listens on port 5050 and exposes endpoints like `/api/fpl/<path>`, forwarding requests to the official FPL API and returning JSON responses with CORS headers. Responses are cached for 10 minutes to reduce load on the FPL API. To use, clone the repository, install dependencies with `pip install flask flask-cors requests`, and run `python fpl_proxy.py`. Example usage: `GET http://localhost:5050/api/fpl/bootstrap-static/` returns the same data as the official FPL endpoint but with CORS and caching. Only GET requests are supported.

**Important:**  
This proxy can only be run and work at your home on your local WiFi network. If you deploy it on the internet (e.g., on a cloud server), it will not work because the FPL API restricts data access for requests coming from deployed/public backends. The proxy is intended for development and personal use only. If deploying publicly, consider adding authentication or rate limiting. No official affiliation with the Fantasy Premier League.

MIT License.
