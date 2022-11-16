from player import Player
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader 
    
    def top_scorers_by_nationality(self, nationality):
        print(f'Players from {nationality}')

        def filter_by_nationality(player):
            if player.nationality == nationality:
                return True
            else:
                return False
        
        return sorted(filter(filter_by_nationality,self.reader.get_players()), key=lambda p: p.assists+p.goals, reverse=True)

    

