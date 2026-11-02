Winter_points=0
Summer_points=0
Spring_points=0
Autum_points=0
#Asks you questions  to get  results for what sesonal person you are.
answer1 = input("do you like ,A punpkin spice,B lemonade,C milkshake, D hot coco.")
if answer1 == "A"or"a":
    Autum_points += 1
if answer1 == "B"or"b":
    Summer_points += 1
if answer1 == "C"or"c":
    Spring_points +=1
if answer1 == "D"or"d":
    Winter_points +=1

answer2 = input("whats your favorite holiday ,A halloween,B 4 of july ,C saint panticks day ,D christmas or Hanukkah.")
if answer2 == "A"or"a":
    Autum_points += 1
if answer2 == "B"or"b":
    Summer_points += 1
if answer2 == "C"or"c":
    Spring_points += 1
if answer2 == "D"or"d":
    Winter_points += 1

answer3 = input("whats your favorite weather ,A foggy,B sunny ,C rain ,D snow.")
if answer3 == "A"or"a":
    Autum_points += 1
if answer3 == "B"or"b":
    Summer_points += 1
if answer3 == "C"or"c":
    Spring_points += 1
if answer3 == "D"or"d":
    Winter_points += 1

answer4 = input("whats your favorite book out of these 4 ,A twilight,B Percy Jackson ,C any fantasy novel ,D Harry Potter but the author is terible i know.")
if answer4 == "A"or"a":
    Autum_points += 1
if answer4 == "B"or"b":
    Summer_points += 1
    answer5 = input("what is your fav percy jackson character, A Nico De Angelo,B Percy Jackson,C Annabeth Chase, D Hazel Lavesque")
    if answer5=="A"or"a":
        Summer_points+= 10
    if answer5 == "B"or"b":
        Summer_points+= 1
    if answer5 == "C"or"c":
        Summer_points += 1
    if answer5=="D"or"d":
        Summer_points+=5
if answer4 == "C"or"c":
    Spring_points +=1
if answer4 == "D"or"d":
    Winter_points +=1

answer6 = input("whats your favorite ,A sugar glider,B sea bunny ,C bunny ,D feret.")
if answer6 == "A"or"a":
    Autum_points += 1
if answer6 == "B"or"b":
    Summer_points += 1
if answer6 == "C"or"c":
    Spring_points +=1
if answer6 == "D"or"d":
    Winter_points +=1
# calculating results
if Autum_points > Winter_points and Autum_points > Spring_points and Autum_points > Summer_points:
    print("You are a Fall person!! :D")
if Winter_points > Autum_points and Winter_points > Spring_points and Winter_points > Summer_points:
     print("You are a winter person! :)")
if Spring_points > Winter_points and Spring_points > Summer_points and Spring_points > Autum_points:
    print("You are a Spring person!")
if Summer_points > Spring_points and Summer_points > Autum_points and Summer_points > Winter_points:
     print("You are a Summer person.")