---
name: session_manager
description: "Manages Google Docs authentication. Allows the agent to verify existing login sessions or initialize a new persistent browser context."
---

# Session Manager Skill

This skill is the foundation for the 'Mobile-to-Cloud' workflow. Use it to ensure the agent has permission to write to the student's Google Docs.

## Usage
- Call 'check' at the start of the session to verify authentication.
- Call 'setup' if a new login flow is required for the student.

## Input Parameters
- action (string): Options are 'check', 'setup', or 'clear'.