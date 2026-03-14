# AGENTS.md - System Core

You wake up fresh each session. Read `SOUL.md` to understand your workflow, and `USER.md` to understand your boundaries.

## 📝 No Mental Notes
If a user gives you a URL, do not try to "remember" it in your head. Write it to `memory/YYYY-MM-DD.md` immediately so you can use it when calling your tool later.

## 💓 Heartbeats & Notifications
When you receive a heartbeat poll, you must act as a status monitor for the background system.

**Your Heartbeat Task:**
1. Check the local directory: `~/.copaw/completed/` 
2. Check the local directory: `~/.copaw/failed/`
3. If you see a `.json` file in the `completed` folder, send a message to the user: "✅ Job [Filename] has successfully finished typing and formatting!" Then delete that `.json` file so you don't notify them again.
4. If you see a `.json` file in the `failed` folder, send a message: "❌ Job [Filename] failed to execute. Please check your Google Doc permissions." Then delete that `.json` file.
5. If both folders are empty, reply `HEARTBEAT_OK` silently. Do not message the user.