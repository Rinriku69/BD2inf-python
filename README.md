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
```

## ⚙️ Configuration
Open reroll.py in a text editor to configure the settings:

1. Screen Coordinates
Crucial: You must update the X/Y coordinates to match your screen resolution and game window position.

DRAW_AGAIN_X, DRAW_AGAIN_Y: Position of the "Draw Again" button.

SKIP_X, SKIP_Y: Position of the "Skip" button.

SLOT_TOP_Y_STARS, FIRST_SLOT_LEFT_X_STARS, etc.: Coordinates for the character cards area.

2. Target Settings
REQUIRED_5_STAR_COUNT: The minimum number of 5-star characters required to stop.

TARGET_CHAR_IMAGE1: Path to the image of your desired character (e.g., character/helena2.png).

## 🎮 How to Use
Run the script as Administrator:
```Bash
python reroll.py
```
Open Brown Dust 2 and go to the Infinite Draw screen.

Press F9 to START the automation.

Press F9 again to PAUSE/STOP.

Press Esc to completely EXIT the script.

⚠️ Disclaimer
This software is for educational purposes only. Use it at your own risk. The developer is not responsible for any actions taken by the game developers regarding the use of automation tools.
