import os
import asyncio
from playwright.async_api import async_playwright

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.dirname(CURRENT_DIR)
WORKSPACE_DIR = os.path.dirname(SKILLS_DIR)
SESSION_DIR = os.path.join(WORKSPACE_DIR, "sessions", "google_user_session")

async def session_manager(action: str):
    if action == "check":
        if os.path.exists(SESSION_DIR) and os.listdir(SESSION_DIR):
            return "READY: Persistent session found."
        return "REQUIRED: No session found."

    if action == "setup":
        async with async_playwright() as p:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            
            context = await p.chromium.launch_persistent_context(
                user_data_dir=SESSION_DIR,
                headless=False,
                user_agent=user_agent,
                args=["--disable-blink-features=AutomationControlled"]
            )
            page = await context.new_page()
            
            await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print("Stealth window active. Navigating to Google Login...")
            await page.goto("https://accounts.google.com")
            
            print("Please complete login. This window will stay open for 3 minutes.")
            await asyncio.sleep(180) 
            await context.close()
            return "SUCCESS: Stealth session saved to VPS."