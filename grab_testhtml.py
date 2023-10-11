import os
import re
import requests

print("Script starting...")  # Debugging line

# Headers for fetching HTML
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

process_all = False  # Set to True for all, False for specific starting letters

# Allowed first letters after 'test_'
allowed_starting_letters = ['m', 'n', 'o', 'p', 'q', 'r']  # Modify as needed if process_all is False

# Absolute directory paths
test_dir = 'C:\\Users\\joeyk\\Desktop\\5\\recipe-scrapers\\tests'
test_data_dir = os.path.join(test_dir, 'test_data')

# Debugging line to check the directory listing
print(f"Files in test directory: {os.listdir(test_dir)}")

# Loop through Python files in the tests directory
for filename in os.listdir(test_dir):
    print(f"Checking file: {filename}")  # Debugging line

    if process_all or (filename.endswith('.py') and filename[5].lower() in allowed_starting_letters):
        print(f"Processing file: {filename}")  # Debugging line

        with open(os.path.join(test_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()

        # Adjusted regex to find a URL specifically in the test_canonical_url method
        match = re.search(r'def test_canonical_url\(self\):.*?"([^"]+)"', content, re.DOTALL)
        if match:
            url = match.group(1)
            print(f"Found URL: {url}")  # Debugging line

            try:
                # Fetch new HTML using the URL and headers with a 10-second timeout
                response = requests.get(url, headers=headers, timeout=10)
                print(f"HTTP Status Code: {response.status_code}")  # Debugging line

                if response.status_code == 200:
                    new_html = response.text
                    print(f"Received HTML data, length: {len(new_html)}")  # Debugging line

                    # Determine corresponding .testhtml file name
                    testhtml_filename = filename.replace('test_', '').replace('.py', '.testhtml')
                    testhtml_path = os.path.join(test_data_dir, testhtml_filename)

                    print(f"Attempting to write to: {testhtml_path}")  # Debugging line

                    # Update the HTML content
                    with open(testhtml_path, 'w', encoding='utf-8') as f:
                        f.write(new_html)
                        print(f"Updated file: {testhtml_filename}")  # Debugging line
            except requests.exceptions.Timeout:
                print(f"Request timed out for URL: {url}")  # Debugging line
        else:
            print(f"No URL found in file: {filename}")  # Debugging line
