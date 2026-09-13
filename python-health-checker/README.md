# API & Website Health Checker

## Overview

This Python script checks website and API URLs whenever the program is run. Users can enter multiple URLs, and the script sends an HTTP request to each target.

For each URL, the tool reports the response URL, HTTP status code, and a simple status classification. Timeouts, connection failures, and other request errors are handled without crashing the program, allowing the remaining URLs to continue being checked.

Results are displayed in the terminal and saved to a CSV file.

## Features

- Accepts multiple comma-separated website or API URLs
- Sends an HTTP GET request to each URL
- Records HTTP status codes
- Classifies HTTP responses as `OK` or `NOT OK`
- Handles request timeouts without stopping the script
- Handles connection failures without stopping the script
- Handles other Requests errors with a general fallback
- Displays a readable terminal summary
- Saves results to `results.csv`

## Requirements

- Python 3
- Python `requests` library

Install Requests if needed:

```bash
python -m pip install requests
```

## How to Run

1. Run the Python script:

```bash
python health_checker.py
```

2. Enter one or more URLs separated by commas:

```text
https://jsonplaceholder.typicode.com/users/1, https://httpbin.org/status/404
```

3. View the health-check summary in the terminal.

4. Open `results.csv` to view the saved results.

## Example Output

```text
=== HEALTH CHECK SUMMARY ===

URL: https://jsonplaceholder.typicode.com/users/1
Status Code: 200
Status: OK

URL: https://httpbin.org/status/404
Status Code: 404
Status: NOT OK

URL: http://this-domain-should-not-exist-928374.invalid
Status Code: N/A
Status: CONNECTION FAILED
```

## Error Handling

The script handles request failures independently so that one failed URL does not stop the remaining checks.

- Timeout → `TIMEOUT`
- Connection failure → `CONNECTION FAILED`
- Other Requests errors → `REQUEST FAILED`

When no HTTP response is received, no HTTP status code is stored. The terminal displays this as `N/A`.

## Testing

The tool was tested with several different scenarios:

- Valid endpoint returning HTTP `200` → classified as `OK`
- Endpoint returning HTTP `404` → classified as `NOT OK`
- Invalid/unreachable hostname → classified as `CONNECTION FAILED`
- Delayed endpoint with a short timeout → classified as `TIMEOUT`
- Multiple URLs in a single run → each URL was checked independently
- Failed requests did not prevent subsequent URLs from being checked
- Results were successfully exported to CSV

## Limitations

This is a simple on-demand health-checking tool.

- It does not run continuously or provide 24/7 monitoring.
- It does not send email or other notifications.
- The current version checks user-supplied URLs using HTTP GET requests.
- It does not save or analyze response bodies.
- It does not perform authenticated API monitoring.