# Wall Following Robot (Webots)

This project demonstrates a simple autonomous robot that follows walls using proximity sensors within a Webots simulation environment. The robot detects walls and adjusts its trajectory accordingly to maintain a consistent distance from the wall.

## Project Structure

- **controller/**
  - `wall_follower.py`: Implements the wall-following control logic.
  - `run.py`: Initializes the robot and launches the wall-follower controller.
- **worlds/**
  - `world_maze.wbt`: Webots world file where the robot operates.
- **demo/**
  - `world_maze2.mp4`: Short demonstration video of the robot in action.

## Simulation Demo

wall_follower_robot/demo/world_maze2.mp4

> 📹 Watch how the robot successfully follows walls and avoids obstacles in real-time!

## How to Run

1. Open the `world_maze.wbt` world in Webots.
2. Ensure the controller is set to `controllers/run.py`.
3. Start the simulation.

The robot will autonomously follow the left-hand wall, adjusting its path as needed.

## Requirements

- Webots R2024b or newer
- Python 3.9+
- Webots Python API installed (default with Webots installation)

