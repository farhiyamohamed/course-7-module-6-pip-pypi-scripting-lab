# lib/generate_log.py

from datetime import datetime
import requests

def generate_log(log_data):
    """Writes log_data (list) to a timestamped file."""
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename  # Return filename for testing

def fetch_post_title():
    """Fetches a post title from a public API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json().get("title", "No title found")
    return "No title found"

# Optional: allow CLI execution
if __name__ == "__main__":
    logs = ["User logged in", "User updated profile", "Report exported"]
    generate_log(logs)
    title = fetch_post_title()
    print("Fetched Post Title:", title)