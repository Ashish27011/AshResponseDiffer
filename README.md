# AshResponseDiffer

AshResponseDiffer is a Python-based HTTP response comparison tool designed to analyze and identify differences between two web responses.

## Features

- Compare two URLs
- Validate HTTP/HTTPS URLs
- Capture HTTP response information
- Compare status codes
- Compare response lengths
- Compare final URLs
- Compare response times
- Detect header differences
- Compare response bodies
- Generate unified body differences
- Store detailed body differences in a separate file
- Generate a structured report

## Project Structure

AshResponseDiffer/
│
├── banners/
│   └── banner.py
│
├── core/
│   ├── request_handler.py
│   ├── response_parser.py
│   ├── comparator.py
│   ├── body_diff.py
│   ├── analyzer.py
│   └── reporter.py
│
├── outputs/
│   ├── writeup.py
│   └── change_content.txt
│
├── reports/
│   └── report.txt
│
├── main.py
└── README.md

## How It Works

The program follows this workflow:

User Input
    ↓
URL Validation
    ↓
HTTP Request
    ↓
Response Parsing
    ↓
Response Comparison
    ↓
Difference Analysis
    ↓
Body Difference Detection
    ↓
Report Generation

## Example

The tool can compare two responses such as:

Request A:
https://example.com/page

Request B:
https://example.com/page

It then analyzes differences such as:

- Status Code
- Response Length
- Response Time
- Final URL
- Headers
- Response Body

## Body Difference

The body comparison uses Python's `difflib` module to generate unified differences.

Example:

--- a
+++ b
@@ -40,7 +40,7 @@
-Original content
+Modified content

Large body differences are stored separately in:

outputs/change_content.txt

while the main report provides a concise indication that body differences were detected.

## Technologies

- Python
- Requests
- urllib.parse
- difflib
- File Handling

## Purpose

This project was built as a practical cybersecurity/Python project to understand how HTTP responses can be programmatically collected, compared, analyzed, and reported.

## Future Improvements

- HTML normalization
- Ignore dynamic values such as timestamps and tokens
- More precise changed-content extraction
- Header-by-header comparison
- JSON response comparison
- Improved CLI arguments
- More advanced reporting

## Disclaimer

This tool should only be used against systems and applications that you own or have explicit permission to test.
