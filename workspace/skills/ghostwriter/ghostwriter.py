import os
import random
import asyncio
from playwright.async_api import async_playwright

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.dirname(CURRENT_DIR)
WORKSPACE_DIR = os.path.dirname(SKILLS_DIR)
SESSION_DIR = os.path.join(WORKSPACE_DIR, "sessions", "google_user_session")

async def ghostwriter(target_url: str, content: str, duration_minutes: float = 5.0, is_first_session: bool = True):
    total_seconds = duration_minutes * 60
    char_count = len(content)
    base_delay = max(0.01, (total_seconds - 10) / char_count)
    
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=SESSION_DIR,
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        page = context.pages[0] if context.pages else await context.new_page()
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        await page.goto(target_url)
        
        try:
            editor = await page.wait_for_selector('[aria-label="Document content"]', timeout=20000)
            await editor.click()
            await asyncio.sleep(2)
        except:
            await page.mouse.click(600, 400)
            await asyncio.sleep(2)

        if not is_first_session:
            await page.keyboard.press('Control+End')
            await asyncio.sleep(0.5)

        print(f"🕒 Pacing initiated. Target: {duration_minutes} mins. Calculated Delay: {base_delay:.3f}s/char")

        burst_chars_left = 0
        current_multiplier = 1.0

        for i, char in enumerate(content):
            if burst_chars_left > 0:
                burst_chars_left -= 1
            else:
                if random.random() < 0.15: 
                    burst_chars_left = random.randint(15, 60) 
                    current_multiplier = random.uniform(0.3, 0.6) 
                else:
                    current_multiplier = random.uniform(0.9, 1.6) 

            jitter = base_delay * current_multiplier * random.uniform(0.8, 1.2)
            
            if char in ['.', '?', '!', ',', ';']:
                if random.random() < 0.45: 
                    pause_length = random.uniform(1.0, 3.5) 
                    await asyncio.sleep(pause_length)
                    
            elif random.random() < 0.004: 
                pause_length = random.uniform(2.5, 7.0)
                await asyncio.sleep(pause_length)

            if char == '\n':
                await page.keyboard.press('Enter')
                await asyncio.sleep(jitter + random.uniform(0.8, 2.5))
            elif char == '\t':
                await page.keyboard.press('Tab')
                await asyncio.sleep(jitter)
            else:
                if random.random() < 0.005:
                    await page.keyboard.type(random.choice("asdfghjkl"))
                    await asyncio.sleep(jitter * 2.5) 
                    await page.keyboard.press("Backspace")
                    await asyncio.sleep(jitter * 1.5) 

                await page.keyboard.type(char)
                await asyncio.sleep(jitter)

        print(f"✅ Drafting session complete.")
