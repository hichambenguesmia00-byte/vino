from flask import Flask
import asyncio
from pyppeteer import launch

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ السيرفر يخدم"

@app.route("/check")
def check():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(run_browser())
        return f"🌍 النتيجة: {result}"
    except Exception as e:
        # هنا يرجع الخطأ الحقيقي في الصفحة
        return f"❌ Error: {str(e)}"

async def run_browser():
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto("https://www.google.com", timeout=20000)
    title = await page.title()
    await browser.close()
    return title
