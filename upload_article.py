from pathlib import Path
from helpers import (
    BASE_URL,
    TIMEOUT,
    check_response,
    load_config,
    retrieve_access_token,
)
import requests

def upload_article(token, title, body, topic_id):
    response = requests.post(
        f"{BASE_URL}/knowledgebase",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "type": "article",
            "title": title,
            "body": body,
            "parent_topic_id": topic_id,
        },
        timeout=TIMEOUT,
    )
    check_response(response)
    return response.json()

def main():
    config = load_config()
    token = retrieve_access_token(config["login"], config["secKey"])
    markdown = Path(config["mdFileName"]).read_text(encoding="utf-8")
    result = upload_article(token, config["titleForArticle"], markdown, config["topicId"])
    print(result)

if __name__ == "__main__":
    main()