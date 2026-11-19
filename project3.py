Winter_points=0
Summer_points=0
Spring_points=0
Autum_points=0
#Asks you questions  to get  results for what sesonal person you are.
answer1 = input("do you like ,A punpkin spice,B lemonade,C milkshake, D hot coco.")
if answer1 == "A" or answer1 == "a":
    Autum_points += 1
elif answer1 == "B"or  answer1 =="b":
    Summer_points += 1
elif answer1 == "C"or  answer1 =="c":
    Spring_points += 1 
elif answer1 == "D"or  answer1 =="d":
    Winter_points +=1

answer1 = input("whats your favorite holiday ,A halloween,B 4 of july ,C saint panticks day ,D christmas or Hanukkah.")
if answer1== "A"or  answer1 =="a":
    Autum_points += 1
if answer1 == "B"or  answer1 =="b":
    Summer_points += 1
if answer1 == "C"or  answer1 =="c":
    Spring_points += 1
if answer1 == "D"or  answer1 =="d":
    Winter_points += 1

answer1 = input("whats your favorite weather ,A foggy,B sunny ,C rain ,D snow.")
if answer1== "A"or  answer1 =="a":
    Autum_points += 1
if answer1== "B"or  answer1 =="b":
    Summer_points += 1
if answer1== "C"or  answer1 =="c":
    Spring_points += 1
if answer1== "D"or  answer1 =="d":
    Winter_points += 1

answer1= input("whats your favorite book out of these 4 ,A twilight,B Percy Jackson ,C Hunger games ,D Harry Potter but the author is terible i know.")
if answer1 == "A"or  answer1 =="a":
    Autum_points += 1
if answer1 == "B"or  answer1 =="b":
    Summer_points += 1
if answer1== "C"or  answer1 =="c":
    Spring_points +=1
if answer1 == "D"or  answer1 =="d":
    Winter_points +=1

answer1 = input("What is your fav percy jackson character, A Nico De Angelo,B Percy Jackson,C Annabeth Chase, D Hazel Lavesque")
if answer1=="A"or  answer1 =="a":
        Winter_points+= 10
if answer1 == "B"or  answer1 =="b":
        Summer_points+= 1
if answer1 == "C"or  answer1 =="c":
        Summer_points += 1
if answer1=="D"or  answer1 =="d":
        Summer_points+=5

answer1 = input("What is your fav Harry Potter character, A Luna lovegood,B Harry Potter,C Draco malfoy, D Snape")
if answer1=="A"or  answer1 =="a":
        Winter_points+= 1
if answer1 == "B"or  answer1 =="b":
        Winter_points+= 1
if answer1== "C"or  answer1 =="c":
        Winter_points += 1
if answer1=="D"or  answer1 =="d":
        Winter_points+=5

answer1 = input("What is your fav Hunger games character, A Katniss ,B Lucy Gray,C Haymitch Abernathy, D Peeta Mellark")
if answer1=="A"or  answer1 =="a":
        Spring_points+= 5
if answer1 == "B"or  answer1 =="b":
        Spring_points+= 1
if answer1 == "C"or  answer1 =="c":
        Spring_points += 1
if answer1=="D"or  answer1 =="d":
        Spring_points+= 5

answer1= input("What is your fav Twilight character, A Bella Swan ,B Alice Cullen ,C Jacob Black, D Edward Cullen")
if answer1=="A"or  answer1 =="a":
        Autum_points+= 1
if answer1 == "B"or  answer1 =="b":
        Autum_points+= 1
if answer1 == "C"or  answer1 =="c":
        Autum_points+= 1
if answer1=="D"or  answer1 =="d":
        Autum_points+= 1

answer1= input("whats your favorite ,A sugar glider,B sea bunny ,C bunny ,D feret.")
if answer1== "A"or  answer1 =="a":
    Autum_points += 1
if answer1 == "B"or  answer1 =="b":
    Summer_points += 1
if answer1 == "C"or  answer1 =="c":
    Spring_points +=1
if answer1== "D"or  answer1 =="d":
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
print(f"Your score is {Winter_points} winter points, {Summer_points} summer points, {Spring_points} spring points, and {Autum_points} autum or fall points!")