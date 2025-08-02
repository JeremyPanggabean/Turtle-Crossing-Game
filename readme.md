# 🐢 Turtle Crossing Game

A classic arcade-style game built with Python's Turtle graphics library where you help a turtle safely cross a busy road filled with moving cars.

### Game Screenshot
![Game Screenshot](https://chatgpt.com/backend-api/estuary/content?id=file-GfwyKV29Wb4badY2b3Mqhf&ts=487255&p=fsns&cid=1&sig=5d3d18f8a0ae747ad875bfdd4deb898d99ca7998bc6a9763afb14cca129e337e)

## 🎮 Game Description

In this exciting game, you control a green turtle that needs to cross from the bottom of the screen to the top while avoiding colorful cars moving from right to left. Each successful crossing increases your level and makes the game more challenging!

## 🎯 Objective

- Move the turtle from the starting position at the bottom to the finish line at the top
- Avoid colliding with the moving cars
- Reach higher levels by successfully crossing multiple times
- Challenge yourself to achieve the highest level possible!

## 🕹️ How to Play

- **Controls**: Use the **Up Arrow Key** to move the turtle forward
- **Goal**: Reach the top of the screen without hitting any cars
- **Progression**: Each successful crossing increases the level and car speed
- **Game Over**: The game ends when the turtle collides with a car

## 🚀 Features

- **Progressive Difficulty**: Cars move faster as you advance through levels
- **Colorful Graphics**: Randomly colored cars for visual variety
- **Level Tracking**: Real-time level display in the top-left corner
- **Collision Detection**: Precise collision detection between turtle and cars
- **Smooth Animation**: Fluid movement and responsive controls

## 📁 Project Structure

```
turtle-crossing-game/
│
├── main.py           # Main game loop and setup
├── player.py         # Player (turtle) class and movement logic
├── car_manager.py    # Car generation and movement system
├── scoreboard.py     # Level display and game over screen
└── README.md         # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Turtle graphics library (included with Python)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/JeremyPanggabean/Turtle-Crossing-Game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Turtle-Crossing-Game
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 📋 File Descriptions

### `main.py`
The main game file that:
- Sets up the game screen (600x600 pixels)
- Initializes all game objects (player, cars, scoreboard)
- Contains the main game loop
- Handles collision detection and game over conditions

### `player.py`
Contains the `Player` class that:
- Creates and manages the turtle player
- Handles upward movement with the Up arrow key
- Manages starting position and finish line detection
- Provides methods for resetting position after level completion

### `car_manager.py`
Contains the `CarManager` class that:
- Generates random cars at different y-positions
- Manages car movement from right to left
- Increases car speed when leveling up
- Maintains a list of all active cars on screen

### `scoreboard.py`
Contains the `Scoreboard` class that:
- Displays the current level in the top-left corner
- Updates the level counter when player advances
- Shows "GAME OVER" message when collision occurs
- Uses Courier font for retro arcade aesthetics

## ⚙️ Game Mechanics

### Difficulty Progression
- **Starting Speed**: Cars move at 5 pixels per frame
- **Speed Increase**: +4 pixels per frame for each level
- **Car Generation**: 1/6 chance of creating a new car each frame

### Collision System
- Collision detection uses distance calculation
- Collision occurs when turtle is within 20 pixels of any car
- Game immediately ends upon collision

### Level System
- Level increases each time turtle reaches the top
- Car speed increases with each level
- Level is displayed in real-time during gameplay

## 🎨 Customization

You can easily customize the game by modifying:

- **Colors**: Edit the `COLORS` list in `car_manager.py`
- **Speed**: Adjust `STARTING_MOVE_DISTANCE` and `MOVE_INCREMENT`
- **Difficulty**: Change car generation probability in `create_car()`
- **Screen Size**: Modify screen dimensions in `main.py`


---


Enjoy playing the Turtle Crossing Game! 🐢🚗💨

