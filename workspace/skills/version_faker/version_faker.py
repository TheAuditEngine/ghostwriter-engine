import os
import asyncio
import random
import json
from playwright.async_api import async_playwright
from ghostwriter.ghostwriter import ghostwriter 
from mla_formatter.mla_formatter import format_mla 

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.dirname(CURRENT_DIR)
WORKSPACE_DIR = os.path.dirname(SKILLS_DIR)
CHECKPOINT_FILE = os.path.join(WORKSPACE_DIR, "active_session.json")
SESSION_DIR = os.path.join(WORKSPACE_DIR, "sessions", "google_user_session")

def checkpoint_progress(doc_url, paragraph_index, completed_text):
    state = {"url": doc_url, "index": paragraph_index, "content": completed_text}
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(state, f)

async def simulate_revision_cycle(doc_url):
    print("🔄 Simulating a 'Self-Correction' revision cycle (Scrapping a drafted thought)...")
    
    dummy_thoughts = [
        "Need to remember to expand on the introduction here. ",
        "Maybe I should move the second paragraph down? No, that doesn't make sense. ",
        "Note to self: check the citation for this next part. ",
        "I think the transition here is a bit weak, let me try rewriting it. "
    ]
    
    scrapped_text = "".join(random.choices(dummy_thoughts, k=random.randint(2, 3)))
    
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=SESSION_DIR,
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        page = context.pages[0] if context.pages else await context.new_page()
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await page.goto(doc_url)
        
        try:
            editor = await page.wait_for_selector('[aria-label="Document content"]', timeout=20000)
            await editor.click()
            await asyncio.sleep(2)
        except:
            await page.mouse.click(600, 400)
            await asyncio.sleep(2)

        await page.keyboard.press('Control+End')
        await asyncio.sleep(1)
        await page.keyboard.press('Enter')
        await page.keyboard.press('Enter')
        
        for char in scrapped_text:
            await page.keyboard.type(char)
            await asyncio.sleep(random.uniform(0.05, 0.15))
            
        print("   -> Typed a messy thought. Pausing to 'read' it...")
        await asyncio.sleep(random.uniform(5.0, 15.0))
        
        print("   -> Scrapping the thought (Deleting)...")
        await page.keyboard.press('Shift+Home')
        await asyncio.sleep(0.5)
        await page.keyboard.press('Backspace')
        await asyncio.sleep(1)
        
        await page.keyboard.press('Backspace')
        await page.keyboard.press('Backspace')

        print("✅ Revision cycle complete. Context saved.")
        await context.close()


async def version_history_faker(text: str, doc_url: str, total_duration_mins: float):
    if not text.startswith('\t'):
        text = '\t' + text.replace('\n\n', '\n\n\t')

    num_sessions = random.randint(4, 7) 
    session_duration = (total_duration_mins * 0.8) / num_sessions
    
    chunks = []
    start = 0
    remaining_length = len(text)
    
    for i in range(num_sessions):
        if i == num_sessions - 1:
            chunks.append(text[start:])
        else:
            percent_to_take = random.uniform(0.10, 0.40)
            chunk_size = int(len(text) * percent_to_take)
            
            chunk_size = min(chunk_size, remaining_length - 50) 
            
            end = start + chunk_size
            while end < len(text) and text[end] not in (' ', '\n', '\t'):
                end += 1
                
            chunks.append(text[start:end])
            start = end
            remaining_length = len(text) - start

    print(f"Starting Forensic Version History Simulation: {num_sessions} granular sessions planned.")

    for i, chunk in enumerate(chunks):
        if not chunk:
            continue
        
        await ghostwriter(doc_url, chunk, session_duration, is_first_session=(i == 0))
        checkpoint_progress(doc_url, i, chunk)

        if i > 0 and random.random() < 0.3:
            await simulate_revision_cycle(doc_url)

        if i < num_sessions - 1:
            base_break_time = (total_duration_mins * 0.2) / num_sessions
            actual_break_time = base_break_time * random.uniform(0.2, 2.5) 
            
            print(f"⏸️ Session {i+1} complete.")
            print(f"   Agent is taking a {actual_break_time:.2f} minute break to simulate human downtime.")
            print(f"   DO NOT CLOSE THIS WINDOW. Resuming at {actual_break_time:.2f} mins...")
            
            await asyncio.sleep(actual_break_time * 60)

    print("\nAll drafting sessions complete. Triggering Final Revision: MLA Formatting...")
    await format_mla(doc_url)
    print("Forensic Simulation 100% Complete.")

    completion_flag = os.path.join(WORKSPACE_DIR, "NOTIFY_USER.txt")
    with open(completion_flag, "w") as f:
        f.write(f"The Ghostwriter job for {doc_url} is 100% complete and formatted.")
