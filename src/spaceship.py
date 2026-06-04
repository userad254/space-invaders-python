"""
Module for the Spaceship class in Space Invaders.
"""

from turtle import Turtle
from typing import Tuple, List
from bullet import Bullet

# Constants
MOVE_DISTANCE = 20
SCREEN_BOUNDARY = 380


class Spaceship(Turtle):
    """A class representing the player's spaceship."""

    def __init__(self, position: Tuple[float, float]) -> None:
        """
        Initialize the spaceship at a given position.

        Args:
            position: Initial (x, y) coordinates of the spaceship.
        """
        super().__init__()
        self.shape("triangle")
        self.color("green")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.bullets: List[Bullet] = []

    def go_right(self) -> None:
        """Move the spaceship to the right if within boundaries."""
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < SCREEN_BOUNDARY:
            self.setx(new_x)

    def go_left(self) -> None:
        """Move the spaceship to the left if within boundaries."""
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > -SCREEN_BOUNDARY:
            self.setx(new_x)

    def shoot(self) -> None:
        """Fire a bullet from the current position."""
        bullet_pos = (self.xcor(), self.ycor())
        new_bullet = Bullet(bullet_pos)
        self.bullets.append(new_bullet)

    def update_bullets(self) -> None:
        """Move all active bullets and remove inactive ones."""
        for bullet in self.bullets[:]:
            bullet.move()
            if not bullet.is_active:
                self.bullets.remove(bullet)
