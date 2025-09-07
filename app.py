from flask import Flask
import asyncio
from playwright.async_api import async_playwright

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Server is running!"

@app.route("/check")
def check():
    async def run():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
            page = await browser.new_page()
            await page.goto("https://www.google.com", timeout=20000)
            title = await page.title()
            await browser.close()
            return title

    try:
        title = asyncio.run(run())
        return f"🌍 Page title: {title}"
    except Exception as e:
        return f"❌ Error in /check: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
