\# The Ghostwriter Engine (by The Audit Engine)



\*\*The open-source core of the most advanced local academic writing suite.\*\* Most "AI Humanizers" are simple cloud wrappers that charge students $30/month for a prompt that still gets flagged by Turnitin and GPTZero. I built the \*\*Ghostwriter Engine\*\* to end the subscription scam. This is a local-first, privacy-shielded behavioral engine that doesn't just "rewrite" text—it simulates the actual human writing process.



\---



\## Why This is Different



\### 1. Forensic Behavior Simulation

Standard tools require you to copy-paste your entire essay into google docs instantly. Which creates an awfully suspicious looking version history in your google docs. This engine uses \*\*Playwright\*\* to physically type your essay into Google Docs for you, providing you with a real looking version history. 

\* \*\*Variable Pacing:\*\* Mimics human typing speeds with randomized "jitter."

\* \*\*Self-Correction:\*\* Randomly types typos and backspaces them, just like a human brain working through a sentence.

\* \*\*Session Interruption:\*\* Simulates a "forensic version history" by breaking the writing task into 4-7 separate sessions over several hours.



\### 2. The Humanizer Skill (24-Point Logic)

The engine integrates the \*\*Humanizer\*\* skill by \[BioStar Technology](https://clawhub.ai/biostartechnology/humanizer). It proactively scans and removes 24 distinct AI patterns, including:

\* \*\*Significance Inflation:\*\* No more "pivotal moments" or "testaments to."

\* \*\*AI Vocabulary:\*\* Automatically replaces words like "Moreover," "Tapestry," and "Underscore."

\* \*\*Rule of Three:\*\* Breaks up algorithmic list structures into natural prose.



\### 3. Privacy Shield

Because this runs locally, your data never leaves your machine. Your essays are never stored on a cloud server or used to train future models.



\---



\## 💻 System Requirements



This engine runs locally using the \*\*Qwen 3.5:9b\*\* model. 



\* \*\*GPU (Recommended):\*\* 8GB VRAM (NVIDIA RTX 3060/4060 or better) for high-speed "soulful" writing.

\* \*\*CPU/RAM (Minimum):\*\* 8GB System RAM. 

&#x20; \* \*Note: Running on System RAM alone will be significantly slower, but it works perfectly for "set-it-and-forget-it" jobs while you sleep.\*



\---



\##  Installation (The "Hard" Way)



This repository contains the raw Python scripts for developers and tech-savvy students.



1\. \*\*Clone the repo:\*\*

&#x20;  ```bash

&#x20;  git clone git@github.com:TheAuditEngine/ghostwriter-engine.git



2\. \*\*Install Dependecies:\*\*

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  playwright install chromium



3\. \*\*Configure Environment:\*\* Create a .env file with your Telegram Token and Google User Profile paths.



4\. Run the Daemon and the Gateway: 

&#x20;  ```bash

&#x20;  python daemon.py



\---



\##  How to Use (1st Time Setup)



If you are using the raw repository, you must manually pair your messaging channel and dashboard. Follow these steps exactly:



\### 1. Start the Services

Open two terminal windows:

\* \*\*Terminal 1 (Gateway):\*\* Run `openclaw gateway` to start the communication bridge.

\* \*\*Terminal 2 (Execution):\*\* Run `python daemon.py` to start the background typing engine.



\### 2. The Security Handshake (Crucial)

OpenClaw requires explicit approval for any device or channel trying to talk to your local model.



\*\*A. Pair your Browser Dashboard:\*\*

1\. Run `openclaw dashboard`. You will see a message saying your device is not paired.

2\. Run `openclaw gateway requests`. Look for the \*\*Request ID\*\* for your browser.

3\. Run `openclaw gateway approve \[ID]` to authorize your dashboard.



\*\*B. Pair your Telegram Bot:\*\*

1\. Message your Telegram bot (e.g., "Hello").

2\. Copy the approval code it replies with.

3\. Run `openclaw pairing approve telegram \[Pairing Code]`



\### 3. Google Docs Authentication

The very first time the Ghostwriter opens a Google Doc, Playwright will pause and prompt you to log in. 

\* \*\*Action:\*\* Log in manually in the automated window. 

\* \*\*Persistence:\*\* The engine saves this session to the `sessions/google\_user\_session` folder, so you won't have to log in again for future essays.



\---



\##  Typical Workflow



Once setup is complete, your daily workflow looks like this:



1\. \*\*Prompt the Agent:\*\* Message your Telegram bot: 

&#x20;  \*"Write an essay on \[Topic]. Here is the link: \[Google Doc URL]. I want it done over 180 minutes."\*

2\. \*\*Review the Draft:\*\* The agent will generate a "Humanized" draft in the chat.

3\. \*\*Approve:\*\* Type `Approve` in Telegram.

4\. \*\*Execution:\*\* The agent creates a job file, and the background `daemon.py` will begin the forensic typing session. 

&#x20;  \* \*Tip: You can now close the chat and go about your day. The Ghostwriter is now "working" in the background.\*



\---



\## 📦 The "One-Click" Ghostwriter Suite



While I provide the core engine for free to support transparency, I also offer a \*\*Professional Installer\*\* for students who don't want to deal with a multi step complicated install. The student tier gets you set up without the technical headache. The pro tier allows you to avoid the terminal entirely and control everything by clicking buttons instead of having to type "open claw gateway run" to start the agent up for example. 



&#x20;  -Student Tier ($29.99): The full One-Click Docker Installer. Lifetime access. No subscriptions.



&#x20;  -Pro Tier ($49.99): Includes a "Controller" GUI to manage your AI ghostwriter agent without ever touching a terminal.



> 🔗 \*\*Download Link:\*\* You can find the latest stable installer link in the \*\*"About"\*\* section (right-hand sidebar) of this GitHub repository.



\---



Security 



Pro-Tip: To minimize security risks, if you are using the Docker version, we recommend turning the container off when it is not actively performing a writing task.



\---



Credits



&#x20;  -Humanizer Skill: BioStar Technology



&#x20;  -LLM: Qwen 3.5:9b



&#x20;  -Framework: OpenClaw Agent Framework

