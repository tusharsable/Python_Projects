class Team():

    def __init__(self,name):
        self.team_score = 0
        self.wickets = 0
        self.strike_player = 0
        self.balls = 0
        self.wickets = 0
        self.team_order = []
        self.team_size = 0
        self.player_index = 0
        self.player_partners = []
        self.no_of_players = 0
        self.name = name
    def get_team_order(self):
        
        print(' Batting order for '+ self.name)
        self.team_order = []
        for i in range(0, self.no_of_players): 
            ele = Player(input()) 
            self.team_order.append(ele) # adding the element

        self.strike_player=self.team_order[ self.player_index ]
        self.team_size = len(self.team_order)
        self.player_partners=self.team_order[ self.player_index : self.player_index + 2 ]
        self.player_index = 1
        for player in self.player_partners:
            player.on_strike = True
    
    
    def run(self,runs):
        self.team_score += runs
        self.strike_player.run(runs)
        if runs%2 :
            self.strike_change()
        
        
    def six(self):
        self.strike_player.six()
        self.team_score += 6

    def four(self):
        self.strike_player.four()
        self.team_score += 4

    def wicket(self):
        self.wickets += 1
        self.player_index += 1
        self.strike_player.on_strike=False
        self.player_partners.remove(self.strike_player)
        try:
            self.strike_player = self.team_order[ self.player_index ]
        except: 
            return(1)
        self.strike_player.on_strike = True
        self.player_partners.append(self.strike_player)


    def strike_change(self):
        for player in self.player_partners:
            if player != self.strike_player:
                self.strike_player.on_strike = True
                self.strike_player=player
            else:
                self.strike_player.on_strike = False

    def ball(self):
        
        self.strike_player.ball()
        self.balls += 1





class Player(Team):
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.fours = 0
        self.sixes = 0
        self.balls = 0
        self.on_strike = False

    def run(self,runs):
        self.score += runs
        
    def six(self):
        self.sixes += 1
        self.score += 6

    def four(self):
        self.fours += 1
        self.score += 4

    def ball(self):
        self.balls +=1

