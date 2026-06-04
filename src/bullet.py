"""
Module for the Bullet class in Space Invaders.
"""

from turtle import Turtle
from typing import Tuple

# Constants
BULLET_SPEED = 10
OFF_SCREEN_Y = 300


class Bullet(Turtle):
    """A class representing a bullet fired by the player."""

    def __init__(self, position: Tuple[float, float]) -> None:
        """
        Initialize the bullet at a given position.

        Args:
            position: Initial (x, y) coordinates of the bullet.
        """
        super().__init__()
        self.shape("arrow")
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.is_active = True

    def move(self) -> None:
        """Move the bullet upwards and deactivate if it goes off-screen."""
        if not self.is_active:
            return

        new_y = self.ycor() + BULLET_SPEED
        self.sety(new_y)

        if new_y > OFF_SCREEN_Y:
            self.deactivate()

    def deactivate(self) -> None:
        """Deactivate the bullet and hide it from the screen."""
        self.is_active = False
        self.hideturtle()
