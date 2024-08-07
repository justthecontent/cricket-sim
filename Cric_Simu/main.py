import random as rand
import pandas as pd


class MatchDay:
    # def __init__(self, team_A, team_B, overs):
    #     self.team_a = team_A
    #     self.team_b = team_B
    #     self.overs = overs

    def toss(self):
        return rand.choice([1, 2]) # 1 -> team_A; 2 -> team_B;

    def choice(self):
        return rand.choice([0, 1]) # 0 -> Bat; 1 -> ball;
    
    def innings(self, batting_team, balling_team, overs, target = 0):

        batting_lineup = list(batting_team.keys())
        #print("Batting lineup: ", batting_lineup)

        balling_lineup = [key for key in balling_team.keys() if balling_team[key] == 'Ball' or balling_team[key] == 'All']
        #print("Balling lineup: ", balling_lineup)

        # key -> bat's_man ; value -> [Run -> 0; Ball_faced -> 0]
        batting_team_timeline = {i: [0, 0] for i in batting_lineup}

        # key -> Boller ; value -> [over -> 0; wicket_taken-> 0]
        balling_team_timeline = {i: [0, 0] for i in balling_lineup}

        extra_runs = 0
        total_runs = 0 

        strike = batting_lineup[0]
        non_strike = batting_lineup[1]
        up_coming_batsman = 2

        prev_baller = None
        prev_delivery = None

        #iterating over overs
        over = 0
        while over < overs and up_coming_batsman < len(batting_lineup): # Tracking Overs and up_coming_batsman

            if prev_baller is None:
                baller = rand.choice(balling_lineup)
            else:
                pid = balling_lineup.index(prev_baller) # prev_baller index
                baller = rand.choice(balling_lineup[:pid] + balling_lineup[pid+1:]) # removing prev_baller since baller can't ball 2 consecutive overs
            j = 1
        
            while j < 7: # j -> every ball

                if prev_delivery is None:
                    delivery = rand.choice([0, 1, 2, 3, 4, 5, 6, 'WD', 'NB', 'WKT']) # WD -> wide delivery; NB -> no ball; WKT -> wicket
                
                elif prev_delivery == 'NB':  # if prev_delivery is no ball then next delivery must be Free hit;
                    delivery = rand.choice([0, 1, 2, 3, 4, 5, 6, 'WD', 'NB'])
                    if delivery != 'NB' or delivery != 'WD':
                        prev_delivery = None

                print(f"Over {over}.{j}: {strike} faces {baller} - {delivery}")

                if delivery == 'WD':  # wide delivery
                    j -= 1
                    extra_runs += 1
                    total_runs += 1

                elif delivery == 'NB':  # no ball
                    j -= 1
                    extra_runs += 1
                    total_runs += 1
                    prev_delivery = 'NB'

                elif delivery == 'WKT':  # Wicket
                    print(f"{strike} is out!")
                    balling_team_timeline[baller][1] += 1
                    batting_team_timeline[strike][1] += 1
                    if up_coming_batsman < len(batting_lineup):
                        strike = batting_lineup[up_coming_batsman]
                        up_coming_batsman += 1
                    else:
                        return batting_team_timeline, balling_team_timeline, extra_runs, total_runs

                elif delivery % 2 != 0 and delivery != 5:  # odd runs
                    print(f"{strike} scores {delivery} run(s)")
                    batting_team_timeline[strike][0] += delivery
                    batting_team_timeline[strike][1] += 1
                    strike, non_strike = non_strike, strike
                    total_runs += delivery

                else:
                    batting_team_timeline[strike][0] += delivery
                    batting_team_timeline[strike][1] += 1
                    total_runs += delivery
                
                if target != 0 and total_runs >= target:  # checking if target is achieved
                    print(f"Target of {target} achieved by {batting_team}")
                    return batting_team_timeline, balling_team_timeline, extra_runs, total_runs

                j += 1 # next ball


            strike, non_strike = non_strike, strike  # changing strike after every over
            print(f"End of over {over}: {batting_team} - {total_runs}/{up_coming_batsman-2}")
            balling_team_timeline[baller][0] += 1
            prev_baller = baller
            over += 1

        return batting_team_timeline, balling_team_timeline, extra_runs, total_runs


    def result(self, team_A, team_B, overs, tname): # Showcase 1st innings and 2nd innings Timeline
        toss = self.toss()
        choice = self.choice()

        team_a_total_runs = 0
        team_b_total_runs = 0

        print(f"{tname[toss-1]} won the toss and elected to {['bat', 'ball'][choice]} first")

        if (toss == 1 and choice == 0) or (toss == 2 and choice == 1):  # team_A bat first

            team_a_batting_timeline, team_b_balling_timeline, team_a_extra_runs, team_a_total_runs = self.innings(team_A, team_B, overs)
            team_a_batting_showcase = pd.DataFrame(team_a_batting_timeline, index=['Runs', 'Balls'])

            print(f"After {overs} overs, {tname[0]} scored {team_a_total_runs} (Extras: {team_a_extra_runs})")
            print()
            print(f"{tname[0]} batting Timeline: ")
            print(team_a_batting_showcase.transpose())
            print()
            print(f"{tname[1]} bowling Timeline: ")
            print(pd.DataFrame(team_b_balling_timeline, index=['Overs', 'Wickets']))
            target = team_a_total_runs + 1
            print(f"Now {tname[1]} needs {target} runs to win")
            print()
            team_b_batting_timeline, team_a_balling_timeline, team_b_extra_runs, team_b_total_runs = self.innings(team_B, team_A, overs, target)
            #team_b_balling_showcase = pd.DataFrame(team_b_balling_timeline, index=['Overs', 'Wickets'])
            team_b_batting_showcase = pd.DataFrame(team_b_batting_timeline, index=['Runs', 'Balls'])
            print(f"After {overs} overs, {tname[1]} scored {team_b_total_runs} (Extras: {team_b_extra_runs})")
            print()
            print(f"{tname[1]} batting Timeline: ")
            print(team_b_batting_showcase.transpose())
            print()
            print(f"{tname[0]} bowling Timeline: ")
            print(pd.DataFrame(team_a_balling_timeline, index=['Overs', 'Wickets']))

        else:     # team_B bat first

            team_b_batting_timeline, team_a_balling_timeline, team_b_extra_runs, team_b_total_runs = self.innings(team_B, team_A, overs)
            team_b_batting_showcase = pd.DataFrame(team_b_batting_timeline, index=['Runs', 'Balls'])
            print(f"After {overs} overs, {tname[1]} scored {team_b_total_runs} (Extras: {team_b_extra_runs})")
            print()
            print(f"{tname[1]} batting Timeline: ")
            print(team_b_batting_showcase.transpose())
            print()
            print(f"{tname[0]} bowling Timeline: ")
            print(pd.DataFrame(team_a_balling_timeline, index=['Overs', 'Wickets']))


            target = team_b_total_runs + 1
            print(f"Now {tname[0]} needs {target} runs to win")
            print()
            team_a_batting_timeline, team_b_balling_timeline, team_a_extra_runs, team_a_total_runs = self.innings(team_A, team_B, overs, target)
            team_a_batting_showcase = pd.DataFrame(team_a_batting_timeline, index=['Runs', 'Balls'])
            print(f"After {overs} overs, {tname[0]} scored {team_a_total_runs} (Extras: {team_a_extra_runs})")
            print()
            print(f"{tname[0]} batting Timeline: ")
            print(team_a_batting_showcase.transpose())
            print()
            print(f"{tname[1]} bowling Timeline: ")
            print(pd.DataFrame(team_b_balling_timeline, index=['Overs', 'Wickets']))

        print()
        print(f"# {'-'*20} {tname[0]} VS {tname[1]} {'-'*20} #")
        print()

        # Final Verdict

        if team_a_total_runs > team_b_total_runs:
            print(f"{tname[0]} won")
        elif team_a_total_runs < team_b_total_runs:
            print(f"{tname[1]} won")
        else:
            print(f"Match tied between {tname[0]} and {tname[1]}")
        print()


if __name__ == '__main__': # main function
    
    team_A = {'A1':"Bat", 'A2':"Bat", 'A3':"Bat", 'A4':"Bat", 'A5':"Bat", 'A6':"All", 'A7':"Ball", 'A8':"Ball", 'A9':"Ball", 'A10':"Ball", 'A11':"Ball"}
    team_B = {'B1':"Bat", 'B2':"Bat", 'B3':"Bat", 'B4':"Bat", 'B5':"Bat", 'B6':"All", 'B7':"Ball", 'B8':"Ball", 'B9':"Ball", 'B10':"Ball", 'B11':"Ball"}
    teams = ["Afghanistan", "Australia", "Bangladesh", "England", "India", "Netherlands", "New Zealand", "Pakistan", "South Africa", "Sri Lanka", "West Indies"]
    
    fst_team = rand.choice(teams)
    snd_team = rand.choice(teams[:teams.index(fst_team)]+teams[teams.index(fst_team)+1:])
    overs = 5
    match = MatchDay() # object creation
    match.result(team_A, team_B, overs, [fst_team, snd_team]) # calling result method


                    
                    
