import unittest
from unittest.mock import MagicMock


import tkinter as tk
from dataclasses import dataclass
import random
from typing import Set, Tuple


@dataclass
class GameConfig:
    """
    Configuration object for the Game of Life simulation. Stores settings for the game window,
    grid dimensions, cell size, colors, update speed, and the number of live cells to seed initially.

    - The number of rows and columns are dynamically calculated based on the screen size and cell size.
    - The grid is finite, though the goal is to make it infinite in the future.
    """

    game_screen_width: int = 800
    game_screen_height: int = 600
    game_screen_bg_color: str = "#1F1F1F"
    game_screen_text_color: str = "#FFFFFF"
    game_screen_cell_size: int = 10
    game_screen_cell_color: str = "#E4F0FA"
    game_screen_update_speed: int = 150
    game_cells_seed_number: int = 1234

    @property
    def number_of_rows(self) -> int:
        """Calculates the number of rows based on the screen width and cell size."""
        return self.game_screen_width // self.game_screen_cell_size

    @property
    def number_of_columns(self) -> int:
        """Calculates the number of columns based on the screen height and cell size."""
        return self.game_screen_height // self.game_screen_cell_size


class GameOfLife(tk.Tk):
    """
    Main class for the Game of Life simulation. It extends `tk.Tk` to create the game window
    and controls the simulation logic, including the rules of the game and visual updates.
    """

    def __init__(self, config: GameConfig = GameConfig()):
        """
        Initializes the game with the provided configuration. Sets up the user interface,
        initializes the grid with random live cells, and starts the game loop.
        """
        super().__init__()
        self.game_config = config
        self.simulation_grid = set()  # Stores live cells as (x, y) coordinates
        self.simulation_generation = 0  # Tracks the current generation number
        self.state_paused = (
            False  # Indicates whether the simulation is paused or running
        )

        self.setup_ui()  # Initialize the user interface
        self.seed_random()  # Seed the grid with random live cells
        self.run_game()  # Start the simulation loop

    def setup_ui(self):
        """
        Creates the user interface using Tkinter components. Sets up:
        - A canvas to draw the grid and live cells.
        - Control buttons to pause, resume, or step through generations.
        """
        self.title("Game of Life")  # Set the window title
        self.canvas = tk.Canvas(
            self,
            width=self.game_config.game_screen_width,
            height=self.game_config.game_screen_height,
            bg=self.game_config.game_screen_bg_color,
        )
        self.canvas.pack()

        # Create a frame for control buttons (Quit, Pause/Resume, Step)
        controls = tk.Frame(self)
        controls.pack()

        for text, command in [
            ("Quit", self.quit),
            ("Pause/Resume", self.toggle_state),
            ("Step", self.step),
        ]:
            tk.Button(controls, text=text, command=command).pack(side="left", padx=5)

    def seed_random(self):
        """
        Randomly generates a set of live cells. The number of cells seeded is controlled by the
        `game_cells_seed_number` property from the configuration.
        """
        while len(self.simulation_grid) < self.game_config.game_cells_seed_number:
            # Select random coordinates for live cells within the grid bounds
            self.simulation_grid.add(
                (
                    random.randrange(self.game_config.number_of_rows),
                    random.randrange(self.game_config.number_of_columns),
                )
            )
        # Ensure the correct number of cells were seeded
        assert len(self.simulation_grid) == self.game_config.game_cells_seed_number

    def get_neighbors(self, x: int, y: int) -> Set[Tuple[int, int]]:
        """
        Returns a set of neighboring cell coordinates for a given cell at (x, y).
        The cell can have at most 8 neighbors, excluding itself.
        Ensures the grid is bounded (no wrapping at edges).
        """
        neighbors = {
            (x + dx, y + dy)
            for dx in (-1, 0, 1)
            for dy in (-1, 0, 1)
            if (dx, dy) != (0, 0)  # Skip the cell itself
            and 0 <= (x + dx) < self.game_config.number_of_rows  # Check x bounds
            and 0 <= (y + dy) < self.game_config.number_of_columns  # Check y bounds
        }
        return neighbors

    def update_grid(self):
        """
        Updates the grid based on the rules of Conway's Game of Life:
        - Live cells with fewer than two neighbors die (underpopulation).
        - Live cells with two or three neighbors survive.
        - Live cells with more than three neighbors die (overpopulation).
        - Dead cells with exactly three neighbors become alive (reproduction).
        """
        neighbors = {}  # Stores the count of live neighbors for each cell
        alive_cells = set()  # Set of cells that will be alive in the next generation

        # Count the number of neighbors for each live cell
        for cell in self.simulation_grid:
            for neighbor in self.get_neighbors(*cell):
                neighbors[neighbor] = neighbors.get(neighbor, 0) + 1

        # Apply the Game of Life rules to determine the next generation of cells
        alive_cells = {
            cell
            for cell, count in neighbors.items()
            if count == 3 or (count == 2 and cell in self.simulation_grid)
        }

        # Update the grid with the new set of live cells
        self.simulation_grid = alive_cells
        self.simulation_generation += 1  # Increment generation count

    def draw(self):
        """
        Redraws the grid and live cells on the canvas. Each live cell is represented as a rectangle.
        Also displays the population and the current generation count in the top-right corner.
        """
        self.canvas.delete("all")  # Clear the previous frame

        size = self.game_config.game_screen_cell_size  # Cell size for drawing
        for x, y in self.simulation_grid:
            # Draw each live cell as a filled rectangle
            self.canvas.create_rectangle(
                x * size,
                y * size,
                (x + 1) * size,
                (y + 1) * size,
                fill=self.game_config.game_screen_cell_color,
            )

        # Display population and generation count on the canvas
        self.canvas.create_text(
            self.game_config.game_screen_width - 10,
            10,
            anchor="ne",
            text=f"Population: {len(self.simulation_grid)}\nGeneration: {self.simulation_generation}",
            font=("Arial", 14, "bold"),
            fill=self.game_config.game_screen_text_color,
        )

    def toggle_state(self):
        """
        Toggles the paused state of the simulation. When paused, the grid stops updating.
        Pressing the button again resumes the game from the current generation.
        """
        self.state_paused = not self.state_paused

    def step(self):
        """
        Advances the simulation by one generation and redraws the grid. This is useful for stepping
        through the game manually, generation by generation.
        """
        self.update_grid()  # Update the grid based on the Game of Life rules
        self.draw()  # Redraw the updated grid on the canvas

    def run_game(self):
        """
        The game loop that runs continuously. If the game is not paused, it updates the grid
        to the next generation. The simulation updates at a speed determined by `game_screen_update_speed`.
        """
        if not self.state_paused:
            self.step()  # Advance the game by one step
        self.after(
            self.game_config.game_screen_update_speed, self.run_game
        )  # Continue the game loop


# Start the game if this script is executed directly
if __name__ == "__main__":
    game = GameOfLife()  # Initialize the game with default configuration
    game.mainloop()  # Start the Tkinter event loop to handle UI and game updates


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        """Set up the game with default config"""
        self.config = GameConfig()
        self.game = GameOfLife(config=self.config)
        self.game.simulation_grid = set()  # Clear the initial grid

    def test_initialization(self):
        """Test if the game initializes correctly with random cells."""
        self.game.seed_random()
        self.assertEqual(
            len(self.game.simulation_grid), self.config.game_cells_seed_number
        )

    def test_get_neighbors(self):
        """Test the neighbor calculation for grid boundaries."""
        neighbors = self.game.get_neighbors(0, 0)  # Test for top-left corner
        expected_neighbors = {(1, 0), (0, 1), (1, 1)}  # Wraps around the grid edges
        self.assertEqual(neighbors, expected_neighbors)

        neighbors = self.game.get_neighbors(
            self.config.number_of_rows - 1, self.config.number_of_columns - 1
        )  # Bottom-right corner
        expected_neighbors = {
            (self.config.number_of_rows - 2, self.config.number_of_columns - 1),
            (self.config.number_of_rows - 1, self.config.number_of_columns - 2),
            (self.config.number_of_rows - 2, self.config.number_of_columns - 2),
        }
        self.assertEqual(neighbors, expected_neighbors)

    def test_update_grid(self):
        """Test the grid update logic: cells should survive or die based on neighbors."""
        self.game.simulation_grid = {
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 2),
        }  # A 2x2 block pattern (should remain alive)
        self.game.update_grid()
        self.assertEqual(
            len(self.game.simulation_grid), 4
        )  # A 2x2 block should stay alive

        self.game.simulation_grid = {(1, 1), (2, 2)}  # Two live cells far apart
        self.game.update_grid()
        self.assertEqual(
            len(self.game.simulation_grid), 0
        )  # No neighbors, both cells should die

    def test_step_function(self):
        """Test if the step function updates and draws correctly."""
        self.game.simulation_grid = {
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 2),
        }  # 2x2 block pattern
        self.game.toggle_state()
        self.game.step()
        self.assertGreater(
            self.game.simulation_generation, 0
        )  # Generation should increment
        self.assertEqual(
            len(self.game.simulation_grid), 4
        )  # Should still have 4 cells (same block pattern)
        self.game.toggle_state()

    def test_toggle_pause(self):
        """Test the pause/resume functionality."""
        self.assertFalse(self.game.state_paused)
        self.game.toggle_state()
        self.assertTrue(self.game.state_paused)
        self.game.toggle_state()
        self.assertFalse(self.game.state_paused)

    def test_random_seed(self):
        """Test if random seed creates the correct number of initial cells."""
        self.game.seed_random()
        self.assertEqual(
            len(self.game.simulation_grid), self.config.game_cells_seed_number
        )

    def test_edge_case_cells(self):
        """Test edge case scenarios like grid wrapping."""
        self.game.simulation_grid = set([(0, 0), (0, 1), (1, 0), (1, 1)])
        self.game.update_grid()
        self.assertEqual(
            len(self.game.simulation_grid), 4
        )  # The 2x2 block remains alive

    def test_neighbors_on_large_grid(self):
        """Test if the get_neighbors function works correctly on a large grid."""
        self.game.simulation_grid = {(5, 5)}
        neighbors = self.game.get_neighbors(5, 5)
        expected_neighbors = set(
            [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]
        )
        self.assertEqual(neighbors, expected_neighbors)

    # UI-related tests can be mocked as needed.
    def test_ui_pause_button(self):
        """Test that the pause button correctly toggles the paused state."""
        mock_pause_button = MagicMock()
        self.game.toggle_state()
        mock_pause_button.configure(command=self.game.toggle_state)
        mock_pause_button.invoke()
        self.assertTrue(self.game.state_paused)

    def test_ui_step_button(self):
        """Test that the step button calls the step function."""
        mock_step_button = MagicMock()
        self.game.step()
        mock_step_button.configure(command=self.game.step)
        mock_step_button.invoke()
        self.assertGreater(
            self.game.simulation_generation, 0
        )  # Ensure generation increased


# Run the tests only if Tkinter is available and the file exists
if tk is not None:
    if __name__ == "__main__":
        unittest.main()
