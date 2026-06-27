# NGL-Spammer

## 📖 Overview
**NGL-Spammer** is a Python-based command-line tool designed to automate message submissions to NGL through its web API. It allows users to configure the target username, number of messages, message source, delay intervals, and sending mode before execution.

## ✨ Features
- Target NGL username input.
- Configurable number of messages.
- Supports custom message files (`messages.txt`).
- Adjustable random delay between requests.
- Sequential (single-thread) mode.
- Parallel (multi-thread) mode.
- Automatically creates `messages.txt` if it does not exist.
- Random message selection.
- Random Device ID and User-Agent generation.
- Real-time progress tracking and final statistics.

## 📂 Project Structure
- **bcolors** — Handles colored terminal output.
- **NGLSpammer** — Main class responsible for:
  - User input.
  - Loading messages.
  - Sending HTTP requests.
  - Sequential and parallel execution.
  - Progress tracking and result statistics.

## 📦 Dependencies
- requests
- random
- time
- os
- sys
- json
- datetime
- concurrent.futures

## 📲 Support
- Termux
- pydroid 3

## ⚠️ Disclaimer
This project is intended for **educational and research purposes only**. Any automated interaction with third-party services should comply with their Terms of Service and applicable laws. The author is not responsible for any misuse of this software.

## 👨‍💻 Author
**OhangExpoilt**
