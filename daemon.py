import os
import json
import asyncio
import sys

# --- DYNAMIC PATH CONFIGURATION ---
# This automatically uses the exact folder the daemon.py file is sitting in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Point to OpenClaw's workspace folder
WORKSPACE_DIR = os.path.join(BASE_DIR, "workspace")
BASE_SKILLS = os.path.join(WORKSPACE_DIR, "skills")
VERSION_FAKER_DIR = os.path.join(BASE_SKILLS, "version_faker")

# --- AUTO-LINKING ---
# Dynamically add the skill directories to the system path
for p in [BASE_SKILLS, VERSION_FAKER_DIR]:
    if os.path.exists(p) and p not in sys.path:
        sys.path.append(p)

try:
    from version_faker import version_history_faker
    print(f"✅ Ghostwriter Engine linked successfully for user: {os.getlogin()}")
except ImportError as e:
    print(f"❌ Linkage Failure: {e}")
    sys.exit(1)

# --- JOB DIRECTORIES ---
# Keeping the queue at the root of .openclaw for easy access
QUEUE_DIR = os.path.join(BASE_DIR, "queue")
FAILED_DIR = os.path.join(BASE_DIR, "failed")
COMPLETED_DIR = os.path.join(BASE_DIR, "completed")

# Ensure all necessary folders exist immediately
for folder in [QUEUE_DIR, FAILED_DIR, COMPLETED_DIR]:
    os.makedirs(folder, exist_ok=True)

async def process_queue():
    print(f" Daemon started. Monitoring {QUEUE_DIR}...")
    while True:
        files = [f for f in os.listdir(QUEUE_DIR) if f.endswith(".json")]
        
        for file in files:
            file_path = os.path.join(QUEUE_DIR, file)
            print(f"📦 Found task: {file}")
            
            await asyncio.sleep(0.5) 
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    raw_content = f.read().strip()
                
                if not raw_content:
                    continue
                
                task = json.loads(raw_content)
                print(f"⏳ Triggering Forensic Typewriter for: {task.get('doc_url')}")
                
                # Execute the typing engine
                await version_history_faker(
                    task['draft_text'], 
                    task['doc_url'], 
                    task.get('duration', 18.0)
                )
                
                # SUCCESS: Move file to /completed
                completed_path = os.path.join(COMPLETED_DIR, file)
                if os.path.exists(completed_path):
                    os.remove(completed_path)
                os.rename(file_path, completed_path)
                
                print(f"✅ Task {file} successfully moved to /completed.")

            except Exception as e:
                print(f"❌ Execution Error: {e}")
                
                # FAILURE: Move file to /failed
                if os.path.exists(file_path):
                    failed_path = os.path.join(FAILED_DIR, file)
                    if os.path.exists(failed_path):
                        os.remove(failed_path)
                    os.rename(file_path, failed_path)
                    print(f"⚠️ Task {file} moved to /failed.")
            
        await asyncio.sleep(5) 

if __name__ == "__main__":
    try:
        asyncio.run(process_queue())
    except KeyboardInterrupt:
        print("\n Daemon shutting down.")