from flask import Flask
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask with Playwright is running!"

@app.route("/check")
def check():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com")
        title = page.title()
        browser.close()
        return f"🌍 Title: {title}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
