import subprocess
import os
import rumps
import time
import threading
import json

class Pomodoro(rumps.App):
    def __init__(self):
        super(Pomodoro, self).__init__("Pomodoro")
        self.icon = "tomato.png"
        self.menu = ["Start Session", "Stop", None, "Settings"]
        self.session_duration = 25  # session duration in minutes
        self.session_break = 5  # break duration in minutes
        self.number_of_sessions = 4  # number of sessions
        self.session_active = False
        self.timer_thread = None
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()
        self.remaining_time = self.session_duration * 60

    def start_session(self):
        self.session_active = True
        self.title = "Session Active"
        self.menu["Start Session"].title = "Pause"
        self.start_timer(self.remaining_time)

    def start_timer(self, duration):
        self.stop_event.clear()
        self.pause_event.clear()
        self.timer_thread = threading.Thread(target=self.countdown, args=(duration,))
        self.timer_thread.start()

    def countdown(self, duration):
        while duration > 0 and not self.stop_event.is_set():
            if self.pause_event.is_set():
                time.sleep(1)
                continue
            mins, secs = divmod(duration, 60)
            self.title = f"{mins:02d}:{secs:02d}"
            time.sleep(1)
            duration -= 1
            self.remaining_time = duration
        if not self.stop_event.is_set() and not self.pause_event.is_set():
            self.title = "Time's Up!"
            rumps.alert(title="Pomodoro", message="Session Complete. Time for a break!")
            self.reset()

    @rumps.clicked("Start Session")
    def start_stopwatch(self, sender):
        if not self.session_active:
            self.start_session()
        elif self.pause_event.is_set():
            self.pause_event.clear()
            self.menu["Start Session"].title = "Pause"
        else:
            self.pause_event.set()
            self.menu["Start Session"].title = "Resume"

    @rumps.clicked("Stop")
    def stop_stopwatch(self, _):
        self.stop_event.set()
        self.pause_event.set()
        if self.timer_thread is not None:
            self.timer_thread.join()
        self.reset()

    @rumps.clicked("Settings")
    def open_settings(self, _):
        env = os.environ.copy()
        env["TK_SILENCE_DEPRECATION"] = "1"
        subprocess.Popen(['python3', 'settings_window.py', str(self.session_duration), str(self.session_break), str(self.number_of_sessions)], env=env)
        self.load_settings()

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                settings = json.load(f)
                self.session_duration = settings["session_duration"]
                self.session_break = settings["session_break"]
                self.number_of_sessions = settings["number_of_sessions"]
                self.remaining_time = self.session_duration * 60
        except FileNotFoundError:
            pass

    def reset(self):
        self.session_active = False
        self.title = ""
        self.menu["Start Session"].title = "Start Session"
        self.remaining_time = self.session_duration * 60

if __name__ == "__main__":
    Pomodoro().run()
