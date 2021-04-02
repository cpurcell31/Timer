import tkinter as tk
import math

class Timer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(width=False, height=False)
        self.hours = tk.StringVar()
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()

        self.input_hours = 0
        self.input_minutes = 0
        self.input_seconds = 0
        self.memory_hours = 0
        self.memory_minutes = 0
        self.memory_seconds = 0

        self.timer_running = False
        self._task = None

        self.timer_hours_entry = tk.Entry(
            master=self.window,
            textvariable=self.hours,
            width=2,
            font="Helvetica 44 bold"
        )
        self.timer_minutes_entry = tk.Entry(
            master=self.window,
            textvariable=self.minutes,
            width=2,
            font="Helvetica 44 bold"
        )
        self.timer_seconds_entry = tk.Entry(
            master=self.window,
            textvariable=self.seconds,
            width=2,
            font="Helvetica 44 bold"
        )

        self.hours.set("00")
        self.minutes.set("00")
        self.seconds.set("00")

        self.button_pause = tk.Button(
            master=self.window,
            text="Pause",
            command=self.pause_timer,
            height=2,
            width=15
        )

        self.button_start = tk.Button(
            master=self.window,
            text="Start",
            command=self.start_timer,
            height=2,
            width=15
        )

        self.button_reset = tk.Button(
            master=self.window,
            text="Reset Timer",
            command=self.reset_timer,
            height=2,
            width=15
        )

        self.timer_hours_entry.pack(side=tk.LEFT)
        self.timer_minutes_entry.pack(side=tk.LEFT)
        self.timer_seconds_entry.pack(side=tk.LEFT)
        self.button_start.pack()
        self.button_reset.pack()
        self.button_pause.pack()
        self.window.mainloop()

    def update_time(self):
        """
        Updates timer_hours_entry, timer_minutes_entry, timer_seconds_entry
        decrementing every 1 second unless paused with pause_timer()
        """
        if self.timer_running:
            self.input_seconds -= 1

            if self.input_hours <= 0 and self.input_minutes <= 0 and self.input_seconds <= 0:
                self.hours.set("00")
                self.minutes.set("00")
                self.seconds.set("00")
                self.timer_running = False
                self.window.update()
                # play sound?
            else:
                if self.input_seconds <= 0 < self.input_minutes:
                    self.input_minutes -= 1
                    input_seconds = 59
                if self.input_minutes <= 0 < self.input_hours:
                    self.input_hours -= 1
                    self.input_minutes = 59

                self.hours.set(self.input_hours)
                self.minutes.set(self.input_minutes)
                self.seconds.set(self.input_seconds)
                self.window.update()
                self._task = self.window.after(1000, self.update_time)

    def start_timer(self):
        """
        Starts the timer after a 1 second delay with the user supplied values
        """
        try:
            self.input_hours = int(self.hours.get())
            self.input_minutes = int(self.minutes.get())
            self.input_seconds = int(self.seconds.get())
        except:
            print("Invalid Input: Unable to Convert to INT")

        if self.input_minutes >= 60:
            temp = math.floor(self.input_minutes / 60)
            self.input_hours += temp
            self.input_minutes -= 60 * temp
        if self.input_seconds >= 60:
            temp = math.floor(self.input_seconds / 60)
            self.input_minutes += temp
            self.input_seconds -= 60 * temp

        self.hours.set(self.input_hours)
        self.minutes.set(self.input_minutes)
        self.seconds.set(self.input_seconds)
        self.timer_running = True
        self._task = self.window.after(1000, self.update_time)

    def pause_timer(self):
        """
        Pauses the timer at the current time remaining
        NOTE: Currently this will pause at the current second, meaning,
        the timer has no memory of any time value smaller than a second
        """
        self.cancel_task()
        self.timer_running = False

    def reset_timer(self):
        """
        Resets the timer to the original user input values for
        hours, minutes, and seconds
        """
        pass

    def play_alarm(self):
        """
        Plays an alarm sound when called
        """
        pass

    def cancel_task(self):
        """
        A utility method used by pause_timer() to prevent updates from occurring
        in intervals faster than 1 second
        """
        if self._task is not None:
            self.window.after_cancel(self._task)
            self._task = None


def init():
    clock = Timer()


if __name__ == '__main__':
    init()

