```python
from flask import Flask, request
from LangChain_app.api import handle_request

app = Flask(__name__)
api_endpoint = "/api/v1/langchain"

@app.route(api_endpoint, methods=['POST'])
def api():
    data = request.get_json()
    return handle_request(data)

if __name__ == "__main__":
    app.run(debug=True)
```