lambda/index.py
import json
import urllib.request
import urllib.parse

def handler(event, context):
    body = json.loads(event["body"])
    message = body["message"]

    base_url = "https://983e-35-225-109-230.ngrok-free.app"

    params = urllib.parse.urlencode({"text": message})
    full_url = f"{base_url}/predict?{params}"

    try:
        with urllib.request.urlopen(full_url) as response:
            result = json.loads(response.read().decode())
            answer = result.get("response", "No response")
    except Exception as e:
        answer = f"Error: {e}"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"response": answer})
    }
