# Court Vision - Project Brief

*This is a .md file, which stands for markdown. Press `ctrl + shift + v` on VSCode to view a nicely formatted version of this file*

The Flying Foxes Basketball Club needs a digital solution to track their player’s performance during the season. The head coach wants to move away from the paper spreadsheets they’ve been using to a system that can calculate “Efficiency Ratings” and visualise scoring trends to help with team selection.

This project is part-scaffolded for you, but you will need to fill in the blanks and add additional functionality to meet the requirements outlined below.

## Functional Requirements

1. **Player Management**
    - Player Details: The system should allow the coach to input, edit and manage their players' details. This includes: 
        - Name 
        - Jersey Number
        - Position
        - Salary

    - Player Performance: The system should allow the coach to input and manage player performance data for each game, including:
        - Points
        - Steals
        - Blocks

2. **Efficiency Rating Calculation**
    - The system should calculate an Efficiency Rating for each player based on their performance data. The formula for Efficiency Rating is
    
    ```
    Efficiency Rating = (Points + Steals + Blocks) / Games Played
    ```

3. **Data Visualization**
- The program must be "user-friendly" and provide a clear menu interface. The user should be able to:
    - Add new players and their performance data.
    - View a list of all players and their details.
    - View the Efficiency Ratings of all players.
    - View a specific player's performance data and Efficiency Rating.
    - Exit the program.


## Player Details
Each player should have the following details:
- Name: A string representing the player's name.
- Jersey Number: An integer representing the player's jersey number.
- Position: A string representing the player's position on the team (e.g., Guard, Forward, Center) 'g' | 'f' | 'c'.
- Salary: A float representing the player's salary.

## Performance Data
For each game, the coach should be able to input the following performance data for each player:
- Points: An integer representing the number of points scored by the player in a game.
- Steals: An integer representing the number of steals made by the player in a game.
- Blocks: An integer representing the number of blocks made by the player in a game.


## Technical Constraints
To achieve the highest marks, remember that your program must demonstate the following technical skills:
- Use of functions to modularise code and avoid repetition.
- Use of classes to represent players and their performance data.
- Use of file handling to store and retrieve player data persistently.
- Use of error handling to manage invalid inputs and ensure the program runs smoothly.
- Use of validation to ensure that the data entered by the user is correct and meaningful (e.g., no negative points, valid jersey numbers, etc.).
- No spaghetti code! Your code should be well-structured and easy to read.

## Extended Challenge

### 1 - Starter
Record if a player is injured. If a player reaches 3 injuries, they must be automatically flagged with a "Medical Intervention Required" warning when displayed in the player list.

### 2 - Medium
Add a feature that allows the coach to select 5 specific players for an "Upcoming Match Roster."

### 3 - Hard
Move away from the temporary txt file storage and implement a more permanent solution using a database of your choice.

# Evaluation Criteria
Upon Completion, you must be prepared to discuss: 
- How you structured your code and why.
- The challenges you faced and how you overcame them.
- What data structures you used, and why
- How you implemented error handling and validation.
- How the system could be improved in the future (e.g., additional features, performance optimizations, etc.).

___
Note: This project is a chance to showcase your coding skills and creativity. Don't be afraid to go beyond the requirements. Additionally, you should not use AI tools to generate code for this project.