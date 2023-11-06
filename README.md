# Turtle Crossing Game 🐢

Welcome to the Turtle Crossing Game, a Python game created using Python's Turtle module. The player's objective is to guide their turtle through the busy road, crossing from one end to the other while avoiding oncoming traffic. The player can only move forward.

## Project Structure

The Turtle Crossing Game is organized into several essential components:

### 1. **player.py**

In this module, you'll find the `Player` class, which models the player's character. It includes methods such as:

- `move`: Controls the player's movement across the screen (up).
- `reset_position`: Handles the player's position reset if they reach the finish line.

### 2. **scoreboard.py**

The `Scoreboard` class is responsible for managing and displaying the game's scoreboard. It includes methods like:

- `update_scoreboard`: Updates the game level when the player successfully crosses the finish line.
- `game_over`: Updates the scoreboard to display "GAME OVER" at the center of the screen when the player collides with a car.

### 3. **car_manager.py**

The `CarManager` class, defined in this module, handles the oncoming traffic in the game. It includes attributes like `cars` (an empty list) and `car_speed` (the distance at which the cars move). It also offers methods such as:

- `create_car`: Randomly creates cars based on a predefined chance and appends them to the `cars` list.
- `move_car`: Moves the cars across the screen.
- `increase_speed`: Increases the cars' speed by adjusting the movement distance.

### 4. **main.py**

This is the main program file where the game's logic comes together. It models the game screen, creates the player, scoreboard, and car manager objects, and initiates the game. The `car_manager` object creates and moves the cars, while a for loop within the main while loop continuously checks if the player collides with any cars. If a collision occurs, the game is over. However, if the player successfully crosses the finish line, the scoreboard updates, the player's position resets, and the speed of the cars increases.

## How to Play

- Use the arrow keys (up) to move your turtle player and navigate through the oncoming traffic.
- Your objective is to safely cross the road from one side to the other without colliding with any cars.
- Be cautious, as the cars' speed will increase as the game progresses, making it more challenging.

## Purpose

**Learning Python**: game development, object-oriented programming (OOP), and working with Python's Turtle module.

Get ready to test your reflexes and guide your turtle to victory in the Turtle Crossing Game! 🚗🏁
