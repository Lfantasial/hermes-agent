import requests
import json
from datetime import datetime, timedelta, timezone

def fetch_daily_notion_tasks(token, database_id):
    # Set timezone to Asia/Seoul (UTC+9)
    KST = timezone(timedelta(hours=9))
    now = datetime.now(KST)
    
    # Calculate range: Yesterday 07:00 KST to Today 07:00 KST
    # If currently it's 08:00 KST, "Today 07:00" is 1 hour ago.
    # "Yesterday 07:00" is 25 hours ago.
    today_07 = now.replace(hour=7, minute=0, second=0, microsecond=0)
    if now < today_07:
        # If run before 07:00 (unlikely for an 08:00 cron), adjust
        today_07 -= timedelta(days=1)
    
    yesterday_07 = today_07 - timedelta(days=1)
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    
    # Query database with filter on created_time
    # Notion created_time is in ISO 8601 UTC.
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    
    filter_data = {
        "filter": {
            "and": [
                {
                    "timestamp": "created_time",
                    "created_time": {
                        "on_or_after": yesterday_07.isoformat()
                    }
                },
                {
                    "timestamp": "created_time",
                    "created_time": {
                        "before": today_07.isoformat()
                    }
                }
            ]
        }
    }
    
    response = requests.post(url, headers=headers, json=filter_data)
    if response.status_code != 200:
        return f"Error: {response.text}"
    
    results = response.json().get("results", [])
    if not results:
        return "전날 07시부터 당일 07시 사이에 새로 등록된 항목이 없습니다. 🌌"
    
    report = f"📅 **{yesterday_07.strftime('%m/%d %H:%M')} ~ {today_07.strftime('%m/%d %H:%M')} 노션 업무 요약**\n\n"
    
    for i, page in enumerate(results, 1):
        props = page.get("properties", {})
        
        # Extract fields
        category = props.get("Category", {}).get("select", {}).get("name", "N/A")
        
        task_list = props.get("Task", {}).get("title", [])
        task = task_list[0].get("plain_text", "N/A") if task_list else "N/A"
        
        from_list = props.get("From", {}).get("rich_text", [])
        sender = from_list[0].get("plain_text", "N/A") if from_list else "N/A"
        
        summary_list = props.get("Summary", {}).get("rich_text", [])
        summary = summary_list[0].get("plain_text", "N/A") if summary_list else "N/A"
        
        report += f"{i}. **[{category}]** {task}\n"
        report += f"   - **발신**: {sender}\n"
        report += f"   - **요약**: {summary}\n\n"
        
    return report

if __name__ == "__main__":
    TOKEN = "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"
    DB_ID = "00807fb0163d406c969699eb61a2e761"
    print(fetch_daily_notion_tasks(TOKEN, DB_ID))
