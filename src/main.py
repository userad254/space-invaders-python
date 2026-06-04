"""
Space Invaders - Main Game Module
A classic arcade game clone using Turtle graphics.
"""

import time
from turtle import Screen
from spaceship import Spaceship
from alien import Alien
from scoreboard import Scoreboard

# Screen Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ALIEN_SPAWN_START_X = -350
ALIEN_SPAWN_END_X = 380
ALIEN_SPAWN_STEP_X = 70
ALIEN_SPAWN_START_Y = 100
ALIEN_SPAWN_END_Y = 280
ALIEN_SPAWN_STEP_Y = 30
ALIEN_MOVE_INTERVAL = 1000  # ms


class SpaceInvaders:
    """Main controller class for the Space Invaders game."""

    def __init__(self) -> None:
        """Initialize game components and screen."""
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Python Space Invaders")
        self.screen.tracer(0)

        self.player = Spaceship((0, -260))
        self.scoreboard = Scoreboard()
        self.aliens = []
        self._spawn_aliens()

        self.game_is_on = True
        self._setup_controls()

    def _spawn_aliens(self) -> None:
        """Create a grid of aliens based on spawn constants."""
        for x in range(ALIEN_SPAWN_START_X, ALIEN_SPAWN_END_X, ALIEN_SPAWN_STEP_X):
            for y in range(ALIEN_SPAWN_START_Y, ALIEN_SPAWN_END_Y, ALIEN_SPAWN_STEP_Y):
                new_alien = Alien((x, y))
                self.aliens.append(new_alien)

    def _setup_controls(self) -> None:
        """Bind keyboard events to player actions."""
        self.screen.listen()
        self.screen.onkey(self.player.go_left, "Left")
        self.screen.onkey(self.player.go_right, "Right")
        self.screen.onkey(self.player.shoot, "space")

    def move_aliens(self) -> None:
        """Advance all aliens downwards and schedule next movement."""
        if not self.game_is_on:
            return

        for alien in self.aliens:
            alien.move_down()
        
        self.screen.ontimer(self.move_aliens, ALIEN_MOVE_INTERVAL)

    def _check_collisions(self) -> None:
        """Handle collisions between bullets, aliens, and player."""
        # Bullet vs Alien
        for bullet in self.player.bullets[:]:
            for alien in self.aliens[:]:
                if bullet.distance(alien) < 20:
                    bullet.deactivate()
                    alien.hideturtle()
                    self.aliens.remove(alien)
                    self.player.bullets.remove(bullet)
                    self.scoreboard.add_point()
                    break

        # Alien vs Player / Earth
        for alien in self.aliens:
            if alien.ycor() < self.player.ycor() + 20:
                self.game_over()
                break

    def game_over(self) -> None:
        """End the game and show game over message."""
        self.game_is_on = False
        self.scoreboard.show_game_over()

    def win(self) -> None:
        """End the game and show win message."""
        self.game_is_on = False
        self.scoreboard.show_win()

    def run(self) -> None:
        """Main game loop."""
        self.move_aliens()
        
        while self.game_is_on:
            time.sleep(0.01)  # Control frame rate
            self.screen.update()
            self.player.update_bullets()
            self._check_collisions()

            # Win condition
            if not self.aliens:
                self.win()

        self.screen.exitonclick()


if __name__ == "__main__":
    game = SpaceInvaders()
    game.run()
