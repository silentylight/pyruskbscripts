from helpers import (
    BASE_URL,
    TIMEOUT,
    check_response,
    load_config,
    retrieve_access_token,
    safe_filename,
)
import requests

def fetch_article(token, article_id):
    response = requests.get(
        f"{BASE_URL}/knowledgebase/{article_id}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=TIMEOUT,
    )
    check_response(response)
    data = response.json()
    return data["title"], data["body"]

def write_markdown(file_name, markdown):
    with open(file_name + ".md", "w", encoding="utf-8") as file:
        file.write(markdown)

def main():
    config = load_config()
    token = retrieve_access_token(config["login"], config["secKey"])
    title, body = fetch_article(token, config["articleId"])
    write_markdown(safe_filename(title), body)

if __name__ == "__main__":
    main()
