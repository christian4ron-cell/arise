# Gamified Fitness Tracker (Arise Clone)

A lightweight, self-hosted web app built with Python and Flask that gamifies your daily workout routine. It features RPG elements like leveling up, XP scaling, daily quests, and streak tracking.

## Features
* **Daily Quests:** Randomly assigns a workout routine from a customizable quest bank.
* **RPG Leveling:** Earn XP for completing workouts. The XP required to level up scales automatically (1.5x per level).
* **Streak Tracking:** Keep your streak alive by working out daily.
* **Mobile-Friendly UI:** Designed to look and feel like a native mobile app in dark mode.
* **Local Save Data:** Automatically saves progress to a local JSON file.

## How to Run locally
1. Clone this repository.
2. Install the requirements:
   `pip install -r requirements.txt`
3. Run the app:
   `python app.py`
4. Access the app on your mobile device by typing `http://[YOUR-COMPUTER-IP]:5000` into your phone's browser (ensure both devices are on the same Wi-Fi).

## Customization
You can easily add new workouts by editing the `QUEST_BANK` array inside `app.py`.
