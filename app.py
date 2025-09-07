from flask import Flask
import asyncio
import nest_asyncio

# حل مشكلة event loop مع Flask
nest_asyncio.apply()

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Server is running!"

@app.route("/check")
def check():
    async def run():
        from pyppeteer import launch
        browser = await launch(headless=True, args=['--no-sandbox'])
        page = await browser.newPage()
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
