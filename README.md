# Pomodoro Timer

A simple Pomodoro Timer built with Python and Kivy to help improve focus and productivity by following the Pomodoro Technique.

## Features
- **Pomodoro Timer (25 minutes)**
- **Short Break (5 minutes)**
- **Long Break (15 minutes)**
- **Start, Stop, and Reset functionality**
- **Progress Indicator for session tracking**
- **Audio Alerts for session transitions**
- **Auto-transition from Pomodoro to Breaks**

## Installation

### Prerequisites
Ensure you have Python installed on your system. Install the required dependencies using:

```sh
pip install kivy
```

## How to Run
Clone the repository and navigate to the project folder:

```sh
git clone https://github.com/yourusername/pomotimer.git
cd pomotimer
python main.py
```

## Usage
- Click `Start` to begin the timer.
- Click `Stop` to pause the timer.
- Click `Reset` to restart the current session.
- Use the `Break`, `Long Break`, and `Pomo` buttons to switch modes.

## Project Structure
```
├── main.py          # Python script for Pomodoro Timer logic
├── pomotimer.kv     # Kivy layout file
├── alarm.wav        # Alarm sound for timer completion
├── start.wav        # Sound when starting the timer
```

## Screenshots
![Pomodoro Timer UI](pomo timer screenshot.png)

## Future Improvements
- Customizable work and break durations
- UI enhancements
- Dark mode support

## License
This project is licensed under the MIT License.

---

Feel free to modify and improve the project as needed!

