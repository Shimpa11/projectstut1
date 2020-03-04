import pandas as pd

Teams=["Rajasthan Royals","Kings XI Punjab","Chennai Super Kings","Delhi Capitals",
       "Mumbai Indians","Kolkata Knight Riders", "Royal Challengers Banglore","Deccan Chargers","Mumbai Indians","Kings XI Punjab"]
Years=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
Ranks=[2,3,4,1,3,4,1,2,5,4]
print(len(Teams))
print(len(Years))
print(len(Ranks))

iplData={
    "Team":Teams,
     "Rank":Ranks,
    "Year":Years
}
table=pd.DataFrame(iplData)
print(table)

print("Group by Teams")
groupTeam=table.groupby("Team")
print(groupTeam)
print(groupTeam.groups)

print("Group by Rank")
groupRank=table.groupby("Rank")
print(groupRank)
print(groupRank.groups)

print("Group by Team and Rank")
groupTeamRank=table.groupby(["Team","Rank"])
print(groupTeamRank)
print(groupTeamRank.groups)
print()

print("===Iterate in Group====")
for teamName,grp in groupTeam:
    print(grp)
    print()
    # print(teamName)
print("!!!!!!!!!!!!!!!!")

print()
print("Fetch a single group from groups")
print(groupTeam.get_group("Delhi Capitals"))

print("!!!!!!!!!!!!!!!!")
for teamName,grp in groupRank:
    print(grp)
    print()


anotherIplData={
    "Teams":
    ["Sunrisers Hyderabad","Mimbai Indians","Pune Warriors"],
    "Rank":[8,9,5]

}

table1=pd.DataFrame(iplData)
table2=pd.DataFrame(anotherIplData)

print("Table1")
print(table1)

print("Table2")
print(table2)
table3=pd.concat([table1,table2])
print("Table3")
print(table3)









