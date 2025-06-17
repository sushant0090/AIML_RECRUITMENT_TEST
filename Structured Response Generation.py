import json

def check_json_response(text):
    try:
        return json.loads(text)
    except:
        return {"error": "Not valid JSON"}

reply =
{
    "benefits": [
        "Simple syntax",
        "Powerful libraries",
        "Strong community"
    ]
}


print(check_json_response(reply))
