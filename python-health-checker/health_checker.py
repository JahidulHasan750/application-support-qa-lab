import csv
import requests

raw_urls = input("Enter URLs separated by commas: ")
urls = []

for url in raw_urls.split(","):
    url = url.strip()
    if url:
        urls.append(url)

results = []

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        result = {
            "url": response.url,
            "status_code": response.status_code,
            "status": "OK" if response.ok else "NOT OK"
        }
        results.append(result)

    except requests.exceptions.Timeout:
        result = {
            "url": url,
            "status_code": None,
            "status": "TIMEOUT"
        }
        results.append(result)

    except requests.exceptions.ConnectionError:
        result = {
            "url": url,
            "status_code": None,
            "status": "CONNECTION FAILED"
        }
        results.append(result)

    except requests.exceptions.RequestException:
        result = {
            "url": url,
            "status_code": None,
            "status": "REQUEST FAILED"
        }
        results.append(result)

fieldnames = ["url", "status_code", "status"]

with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("=== HEALTH CHECK SUMMARY ===\n")

for result in results:
    status_code = "N/A" if result["status_code"] is None else result["status_code"]

    print(f'URL: {result["url"]}')
    print(f"Status Code: {status_code}")
    print(f'Status: {result["status"]}\n')