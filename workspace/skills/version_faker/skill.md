---
name: version_faker
description: "Advanced forensic tool that orchestrates multiple writing sessions. It simulates deep revisions to ensure the Google Docs Version History appears authentic and non-automated."
---

# Version History Faker Skill

This skill handles the session structure for high-level forensic realism. It creates multiple 'timestamp' entries in the Google Docs history to prove a student worked on the file over several hours.

## When to Use
- When a student needs proof of a long-term drafting process.
- MUST have an approved draft ready before starting.

## Input Parameters
- text (string): The full approved essay text.
- doc_url (string): URL of the Google Doc.
- total_duration_mins (float): Total time for the simulated multi-session process.