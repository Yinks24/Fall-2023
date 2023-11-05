# Solomon Falode 2154980
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

    def print_standing(self):
        percentage = self.get_win_percentage()

        if percentage > 0.5:
            print('Congratulations, Team', self.team_name, 'has a winning average!')
        else:
            print('Team', self.team_name, 'has a losing average.')

if __name__ == '__main__':
    team = Team()
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())
    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses
    team.print_standing()