"""
Module for the Scoreboard class in Space Invaders.
"""

from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")
SCORE_POS = (300, 260)
MESSAGE_POS = (0, 0)


class Scoreboard(Turtle):
    """A class to handle scoring and game messages."""

    def __init__(self) -> None:
        """Initialize the scoreboard."""
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.update_display()

    def update_display(self) -> None:
        """Clear the current display and show the updated score."""
        self.clear()
        self.goto(SCORE_POS)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self) -> None:
        """Increase the score by one and update the display."""
        self.score += 1
        self.update_display()

    def show_game_over(self) -> None:
        """Display the 'GAME OVER' message."""
        self.goto(MESSAGE_POS)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def show_win(self) -> None:
        """Display the 'YOU WIN' message."""
        self.goto(MESSAGE_POS)
        self.write("MISSION ACCOMPLISHED - YOU WIN!", align=ALIGNMENT, font=FONT)
