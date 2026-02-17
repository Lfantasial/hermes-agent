import requests
import json
import sys

def get_notion_data(token, object_id):
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    
    # Try fetching as a page first
    url = f"https://api.notion.com/v1/pages/{object_id}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        page_data = response.json()
        blocks_url = f"https://api.notion.com/v1/blocks/{object_id}/children"
        blocks_response = requests.get(blocks_url, headers=headers)
        return json.dumps({
            "type": "page",
            "properties": page_data.get("properties", {}),
            "blocks": blocks_response.json().get("results", []) if blocks_response.status_code == 200 else []
        }, indent=2, ensure_ascii=False)
    
    # Try fetching as a database
    db_url = f"https://api.notion.com/v1/databases/{object_id}/query"
    db_response = requests.post(db_url, headers=headers)
    
    if db_response.status_code == 200:
        return json.dumps({
            "type": "database",
            "results": db_response.json().get("results", [])
        }, indent=2, ensure_ascii=False)
    
    return f"Error fetching Notion data: {db_response.text}"

if __name__ == "__main__":
    token = "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"
    object_id = "00807fb0163d406c969699eb61a2e761"
    print(get_notion_data(token, object_id))
