import requests

url = input("Enter URL: ").strip()

try:
    response = requests.get(
        "https://is.gd/create.php",
        params={"format": "json", "url": url},
        timeout=10,
    )
    data = response.json()
    if "shorturl" in data:
        print("Short URL:", data["shorturl"])
    else:
        print("Error:", data.get("errormessage", "Unknown error"))
except requests.RequestException as exc:
    print("Request failed:", exc)
