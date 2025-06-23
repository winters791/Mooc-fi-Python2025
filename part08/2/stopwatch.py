'''class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    def __str__(self):
        return(f"{self.minutes}:{self.seconds}")
    def tick(self):
        if self.seconds >= 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1'''
class Clock:
    def __init__(self,hr: int, min: int,sec: int):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def tick(self):
        while True:
            self.sec += 1
            if self.sec > 59:
                self.min += 1
                if self.min > 59:
                    self.min = 0
                    self.sec = 0
                    self.hr += 1
                    if self.hr > 23:
                        self.hr = 0
                        self.min = 0
                        self.sec = 0
            break
    def set(self, hr:int,min:int):
        self.hr = hr
        self.min = min
        self.sec = 0

clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)