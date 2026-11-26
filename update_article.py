from pathlib import Path
from helpers import (
    BASE_URL,
    TIMEOUT,
    check_response,
    load_config,
    retrieve_access_token,
)
import requests

def update_article(token, body, article_id):
    response = requests.put(
        f"{BASE_URL}/knowledgebase/{article_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"body": body},
        timeout=TIMEOUT,
    )
    check_response(response)
    return response.json()

def main():
    config = load_config()
    token = retrieve_access_token(config["login"], config["secKey"])
    markdown = Path(config["mdFileName"]).read_text(encoding="utf-8")
    result = update_article(token, markdown, config["articleId"])
    print(result)

if __name__ == "__main__":
    main()