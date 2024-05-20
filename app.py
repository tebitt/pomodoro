import rumps
import time

class Pomodoro(rumps.App):
    def __init__(self):
        super(Pomodoro, self).__init__("Pomodoro")
        self.icon = "tomato.png"
        self.menu = ["Start Pomodoro", "Start Short Break", "Start Long Break", "Stop Timer"]

    @rumps.clicked("Start Pomodoro")
    def start_pomodoro(self, _):
        rumps.notification(title="Pomodoro", subtitle="25 minutes starts now!", message="Focus on your work!")
        time.sleep(25*60)
        rumps.notification(title="Pomodoro", message="Time's up! Take a break!")

    
    @rumps.clicked("Start Short Break")
    def start_short_break(self, _):
        rumps.notification(title="Short Break", subtitle="5 minutes starts now!", message="Take a break!")
    
    @rumps.clicked("Start Long Break")
    def start_long_break(self, _):
        rumps.notification(title="Long Break", subtitle="15 minutes starts now!", message="Take a break!")

    @rumps.clicked("Stop Timer")
    def stop_timer(self, _):
        rumps.notification(title="Timer Stopped", message="You can start a new timer now!")

if __name__ == "__main__":
    Pomodoro().run()
