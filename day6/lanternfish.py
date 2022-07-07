"""Lanternfish-class."""


__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


class Lanternfish:
    """A Lanternfish

    This class represents a fish with a reproductioncycle (timer)
    
    Attributes:
        int
    """
    def __init__(self, timer):
        """inits the Lanternfish class.
        """
        self.timer = timer


    def reduce_timer(self):
        """Reduces the timer by one. If it's 0 it creates a new Lanternfish
        """
        if self.timer == 0:
            self.timer = 6
        else:
            self.timer -= 1