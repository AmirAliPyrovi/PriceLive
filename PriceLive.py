#AmirAli Pyrovi
import random
import time
teamlist=[]
for i in range(1,7):
    team=input("Enter Your Team Name = ")
    teamlist.append(team)
    teamrandom=random.choice(teamlist)
print("Team Sherkat Konanede ->",teamlist)
time.sleep(2)
plalistyer=[]
for i in range(1,6):
    player=input("Enter Your Player Name = ")
    plalistyer.append(player)
print("Player Sherkat Konanede ->",plalistyer)
time.sleep(2)
# ساخت برنامه مسابقات به صورت هفته بندی
teams_schedule = teamlist.copy()
random.shuffle(teams_schedule)
baziha = []
tedad_team = len(teams_schedule)
for week in range(tedad_team - 1):
    week_games = []
    for j in range(tedad_team // 2):
        team1 = teams_schedule[j]
        team2 = teams_schedule[tedad_team - 1 - j]
        week_games.append((team1, team2))
    baziha.append(week_games)
    teams_schedule = (
        [teams_schedule[0]]
        + [teams_schedule[-1]]
        + teams_schedule[1:-1]
    )
for i in range(len(baziha)):
    print("\n========== WEEK", i + 1, "==========")
    for team1, team2 in baziha[i]:
        print(team1, " VS ", team2)
    time.sleep(2)
#استارت هفته
time.sleep(2)
#مشخص کردن هفته و بازي
for i in range(1, 6):
    teams = {
        "Team 1":random.randint(0, 5),
        "Team 2":random.randint(0, 5)
    }
    if teams["Team 1"] > teams["Team 2"]:
        s = teams["Team 1"] - teams["Team 2"]
        m = 1
    elif teams["Team 1"] < teams["Team 2"]:
        s = teams["Team 2"] - teams["Team 1"]
        m = 2
    else:
        s = teams["Team 2"] - teams["Team 1"]
        m = 0
    time.sleep(2)
    pointp = []
    for i in plalistyer:
        point=0
        print("Pish bini natayeje", "Name ->",i)
        w = int(input("Gol-Team 1= "))
        e = int(input("Gol-Team 2 = "))
        if (w == teams["Team 1"] and e == teams["Team 2"]):
            point+=10
        else:
            point-=2
        print("Ekhtelaf Gol Do Team ", "Name ->", i)
        q = int(input("Ekhtelaf = "))
        if (q == s ):
            point+=7
        else:
            point-=2
        z = int(input("Bord ya bakht( 1=Team 1___2=Team 2 ) = "))
        if (z == m):
            point += 5
        else:
            point -= 2
        pointp.append([i, point])
        print("Your Points =", point)
        time.sleep(2)
    toppoint = 0
    topname = 0
    for i in pointp:
        if (i[1] > toppoint):
            toppoint = i[1]
            topname = i[0]
    print("\n---TOP SHERKAT KONNADE IN WEEK---")
    time.sleep(1)
    print("Winner =", topname)
    time.sleep(1)
    print("Top Point =", toppoint)
    #نتيجه بازي اين هفته 
    print("\n Natije Bazi In Hafte")
    print("Team 1 = ", teams["Team 1"])
    print("Team 2 = ", teams["Team 2"])
    print("Ekhtelaf =", s)
    time.sleep(2)
    print("")
    print("New Week")
