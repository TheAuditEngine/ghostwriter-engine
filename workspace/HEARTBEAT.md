\# HEARTBEAT.md


_This logic runs every 60 seconds while you are idle._

## Task 1: Check for Ghostwriter Completion
1. Check for a file named `NOTIFY_USER.txt` in the workspace root.
2. **If found**:
    - Read the file content.
    - Send a Telegram message to the user confirming the job is done.
    - Delete the file immediately using `exec: rm NOTIFY_USER.txt`.
3. **If not found**: Continue your cycle.

## Task 2: Maintain Focus
- Review any pending queue items.
- Ensure the background daemon is still running by checking for active Playwright processes if requested.