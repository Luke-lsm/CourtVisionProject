class Player:
    def __init__(self, name, jersey_num, position, salary):
        self.name = name
        self.jersey_num = jersey_num
        self.position = position
        self.salary = salary
        
        # Stats initialization
        self.points = 0
        self.steals = 0
        self.blocks = 0
        self.games_played = 0

    def edit_player_info(self, name=None, jersey_num=None, position=None, salary=None):
        # TODO: Update the player's information based on the provided parameters.
        # Only update the attributes that are not None.

        pass

    def add_game_stats(self, pts, stl, blk):
        # TODO: Update the player's stats.
        pass

    def calculate_efficiency(self):
        # TODO: Implement the formula: (Points + Steals + Blocks) / Games Played
        return 0.0
    
    def format_player_info(self):
        # TODO: Return a formatted string with the player's information and stats.
        """
        Example format:
        Player: John Doe
        Jersey Number: 23
        Position: Guard
        Salary: $5,000,000
        Points: 1500
        Steals: 200
        Blocks: 100
        Games Played: 82
        """
        pass