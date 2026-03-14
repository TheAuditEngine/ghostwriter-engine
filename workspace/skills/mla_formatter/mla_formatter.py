import os
import asyncio
from playwright.async_api import async_playwright

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.dirname(CURRENT_DIR)
WORKSPACE_DIR = os.path.dirname(SKILLS_DIR)
SESSION_DIR = os.path.join(WORKSPACE_DIR, "sessions", "google_user_session")

async def format_mla(target_url: str):
    """
    Automates Google Docs UI to apply standard MLA formatting dynamically.
    """
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=SESSION_DIR,
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        page = context.pages[0] if context.pages else await context.new_page()
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        print(f"Opening document for MLA Formatting: {target_url}")
        
        try:
            await page.goto(target_url, wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(5) 
        except Exception as e:
            print(f"Navigation warning: {e}. Attempting to proceed...")

        try:
            print("Acquiring focus...")
            await page.mouse.click(500, 400)
            await asyncio.sleep(1)
            
            await page.keyboard.press('Control+A')
            await asyncio.sleep(1)

            await page.keyboard.press('Alt+/')
            await asyncio.sleep(0.5)
            await page.keyboard.type('Times New Roman')
            await asyncio.sleep(0.5)
            await page.keyboard.press('Enter')
            await asyncio.sleep(1)

            await page.keyboard.press('Alt+/')
            await asyncio.sleep(0.5)
            await page.keyboard.type('Font size 12')
            await asyncio.sleep(0.5)
            await page.keyboard.press('Enter')
            await asyncio.sleep(1)

            await page.keyboard.press('Alt+/')
            await asyncio.sleep(0.5)
            await page.keyboard.type('Double space')
            await asyncio.sleep(0.5)
            await page.keyboard.press('Enter')
            await asyncio.sleep(1)

            await page.keyboard.press('ArrowRight')
            await asyncio.sleep(1)
            
            print("MLA Formatting successfully applied.")

        except Exception as e:
            print(f"Formatting sequence error: {e}")

        await context.close()