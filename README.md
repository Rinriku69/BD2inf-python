# Brown Dust 2 Infinite Reroll - Python Automation 🐍

A Python-based automation script designed for **Brown Dust 2's Infinite Draw Banner**. This tool automatically rerolls (draws, skips, and scans) until your desired conditions (specific characters or a number of 5-star units) are met.

## 🚀 Features
- **Auto Reroll:** Automatically clicks "Draw Again" and skips the animation.
- **Image Recognition:** Scans the results screen for 5-star indicators and specific target character portraits.
- **Customizable Targets:** Set specific characters you are hunting for.
- **Audio Alert:** Plays a "Tuturu" sound (or system beep) when the target is found.
- **Safety Switch:** Dedicated Hotkeys to Start/Stop or Quit the script immediately.

## 🛠️ Prerequisites
- Python 3.x
- **Administrator Privileges** (Required for `pydirectinput` to interact with the game window).

## 📦 Installation

1. Clone this repository or download the source code.
2. Install the required Python libraries:

```bash
pip install pyautogui pydirectinput keyboard pywin32
