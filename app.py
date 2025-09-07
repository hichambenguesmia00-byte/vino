from flask import Flask
import asyncio
from pyppeteer import launch

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask + Pyppeteer running!"

@app.route("/check")
def check():
    async def run():
        # تشغيل المتصفح بدون sandbox (إلزامي في Render)
        browser = await launch(headless=True, args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto("https://www.google.com", timeout=30000)
        title = await page.title()
        await browser.close()
        return title

    loop = asyncio.get_event_loop()
    title = loop.run_until_complete(run())
    return f"🌍 Title: {title}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
