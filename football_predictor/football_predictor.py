import csv
import argparse
import time

desc = "To retrieve data from the CSV file"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-s', '--season', default="2019", help="Supply the season in which you wish to collect data from", type=int, required=True)
parser.add_argument('-ht', '--home-team', help="Supply the home team", type=str, required=True)
parser.add_argument('-at', '--away-team', help="Supply the away team", type=str, required=False)
args = parser.parse_args()

data = open('{season}.csv'.format(season=args.season))
csv_f = csv.reader(data)

date = []
home_team = []
away_team = []
home_goals = []
away_goals = []
full_time_result = []
half_time_result = []
home_score = []
away_score = []

for row in csv_f:
    date = row[1]
    home_team.append(row[2])
    away_team.append(row[3])
    home_goals.append(row[4])
    away_goals.append(row[5])
    full_time_result.append(row[6])
    half_time_result.append(row[9])

def check_for_home_team():
    if args.home_team in home_team:
        print("{team} is in the home team list".format(team=args.home_team))

def check_for_away_team():
    if args.away_team in away_team:
        print("{team} is in the away team list".format(team=args.away_team))

def get_home_team_index():
    home_team_index = []
    for team in home_team:
        if args.home_team == team:
            home_team_index.append(home_team.index(team))
            print(home_team_index)
            time.sleep(1)
    return home_team_index

def get_away_team_index():
    away_team_index = []
    if args.away_team in away_team:
        away_team_index.append(away_team.index(args.away_team))
    print(away_team_index)
    return away_team_index

def get_home_team_goals():
    index = get_home_team_index()
    print("Home team index is {index}".format(index=index))
    

check_for_home_team()
#check_for_away_team()
get_home_team_index()
#get_away_team_index()
#get_home_team_goals()
