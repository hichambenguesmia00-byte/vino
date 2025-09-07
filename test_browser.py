import asyncio
from playwright.async_api import async_playwright

async def test_browser():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
            page = await browser.new_page()
            await page.goto("https://www.google.com")
            print("✅ Browser launched successfully!")
            print("🌍 Title:", await page.title())
            await browser.close()
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    asyncio.run(test_browser())
