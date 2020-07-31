import pandas as pd
from teams import Team

class Match():

    def __init__(self):
        
        self.no_of_players = int(input(' No of players for each team:'))
        self.no_of_overs = int(input(' No of overs:'))
        self.over_array_inning1=[]
        self.team1=0
        self.team2=0

    def new_teams(self,t_name1,t_name2):
        self.team1=Team(t_name1)
        self.team1.no_of_players = self.no_of_players
        self.team1.get_team_order()
        self.team2=Team(t_name2)
        self.team2.no_of_players = self.no_of_players
        self.team2.get_team_order()

    def play(self):

        #inning 1
        for team in [self.team1,self.team2]:
            (team.name)
            for over_num in range(1,(self.no_of_overs+1)):
                print('Over : ' + str(over_num))
                new_over = Over(over_num,team)
                new_over.get_play()
                self.over_array_inning1.append(new_over)


    def result(self):

        if(self.team1.team_score>self.team2.team_score):
            print(self.team1.name + ' Wins the Match')
        elif(self.team2.team_score > self.team1.team_score ):
            print(self.team2.name + ' Wins the Match')
        else:
            print('\n The Match is tie')
        
        
class Over():
    
    def __init__(self,over_num,team):
        self.columns = ['Player','Score','Fours','Sixes','Balls']
        self.Score_df = pd.DataFrame(columns=self.columns)
        self.over_number = over_num
        self.nb = 0
        self.team = team

    def scoreBoard(self):

        print('\n Scorecard for ' + self.team.name + ' :')
        for player in self.team.team_order :
            if player in self.team.player_partners:
                player_name=(player.name + '*') 
            else:
                player_name=(player.name)
            to_append = [player_name,player.score,player.fours,player.sixes,player.balls]
            player_record = pd.Series(to_append, index = self.columns)
            self.Score_df=self.Score_df.append(player_record,ignore_index = True)
        print(self.Score_df)
        print('\n Total Score :'+ str(self.team.team_score))


    def play_dict(self,x):
        if x == '0':self.team.run(0),
        elif x == '1':self.team.run(1),
        elif x == '2':self.team.run(2),
        elif x == '3':self.team.run(3),
        elif x == '4':self.team.four(),
        elif x == '6':self.team.six(),
        elif x == 'W':
            if(self.team.wicket()):
                return(1)
        elif x == 'Wd':
            self.team.run(1)
            self.nb +=1
        elif x == 'N%':
            self.nb +=1

   
    def get_play(self):

        ball_no = 1
        
        while (True) :
            if (ball_no < 7 + self.nb )and(self.team.wickets < (self.team.team_size-1)):
                ball=input()
                if(self.play_dict(ball)):
                    break
                ball_no += 1
                self.team.ball()
            else:
                break
           
        self.scoreBoard()


def main():
    
    new_match = Match()
    team1 = new_match.new_teams('CSK','MI')
    new_match.play()
    new_match.result()
    
if __name__ == "__main__":
    main()   


