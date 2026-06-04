"""
Module for the Alien class in Space Invaders.
"""

from turtle import Turtle
from typing import Tuple

# Constants
ALIEN_MOVE_DISTANCE = 5


class Alien(Turtle):
    """A class representing an enemy alien."""

    def __init__(self, position: Tuple[float, float]) -> None:
        """
        Initialize an alien at a given position.

        Args:
            position: Initial (x, y) coordinates of the alien.
        """
        super().__init__()
        self.shape("triangle")
        self.color("blue")
        self.penup()
        self.goto(position)
        self.setheading(270)  # Face downwards

    def move_down(self) -> None:
        """Move the alien downwards by a fixed distance."""
        new_y = self.ycor() - ALIEN_MOVE_DISTANCE
        self.sety(new_y)
