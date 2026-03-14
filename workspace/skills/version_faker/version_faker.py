import os
import asyncio
import random
import json
from ghostwriter.ghostwriter import ghostwriter 
from mla_formatter.mla_formatter import format_mla 

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.dirname(CURRENT_DIR)
WORKSPACE_DIR = os.path.dirname(SKILLS_DIR)
CHECKPOINT_FILE = os.path.join(WORKSPACE_DIR, "active_session.json")

def checkpoint_progress(doc_url, paragraph_index, completed_text):
    state = {"url": doc_url, "index": paragraph_index, "content": completed_text}
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(state, f)

async def version_history_faker(text: str, doc_url: str, total_duration_mins: float):
    if not text.startswith('\t'):
        text = '\t' + text.replace('\n\n', '\n\n\t')

    num_sessions = random.randint(4, 7) 
    session_duration = (total_duration_mins * 0.8) / num_sessions
    
    chunks = []
    chunk_size = len(text) // num_sessions
    start = 0
    
    for i in range(num_sessions):
        if i == num_sessions - 1:
            chunks.append(text[start:])
        else:
            end = start + chunk_size
            while end < len(text) and text[end] not in (' ', '\n', '\t'):
                end += 1
            chunks.append(text[start:end])
            start = end

    print(f"Starting Forensic Version History Simulation: {num_sessions} granular sessions planned.")

    for i, chunk in enumerate(chunks):
        if not chunk:
            continue
        
        await ghostwriter(doc_url, chunk, session_duration, is_first_session=(i == 0))
        checkpoint_progress(doc_url, i, chunk)

        if i > 0 and random.random() < 0.3:
            await simulate_revision_cycle(doc_url)

        if i < num_sessions - 1:
            break_time = (total_duration_mins * 0.2) / num_sessions
            print(f"Session {i+1} complete. Taking a {break_time:.2f} min break for forensic realism...")
            await asyncio.sleep(break_time * 60)

    print("\nAll drafting sessions complete. Triggering Final Revision: MLA Formatting...")
    await format_mla(doc_url)
    print("Forensic Simulation 100% Complete.")

    # --- THE FIX: Move these lines INSIDE the function ---
    completion_flag = os.path.join(WORKSPACE_DIR, "NOTIFY_USER.txt")
    with open(completion_flag, "w") as f:
        f.write(f"The Ghostwriter job for {doc_url} is 100% complete and formatted.")

async def simulate_revision_cycle(doc_url):
    print("Simulating a 'Self-Correction' revision cycle...")
    pass