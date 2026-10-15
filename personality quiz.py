winter_points=0
summer_points=0
spring_points=0
fall_points=0

answer1 = input("do you like ,A punpkin spice,B lemonade,C milkshake, D hot coco.")
if answer1 == "A"or"a":
    fall_points += 1
elif answer1 == "B""b":
    summer_points += 1
elif answer1 == "C"or"c":
    spring_points +=1
elif answer1 == "D"or"d":
    winter_points +=1

answer2 = input("whats your favorite holiday ,A halloween,B 4 of july ,C saint panticks day ,D christmas or Hanukkah.")
if answer2 == "A"or"a":
    fall_points += 1
elif answer2 == "B""b":
    summer_points += 1
elif answer2 == "C"or"c":
    spring_points +=1
elif answer2 == "D"or"d":
    winter_points +=1

answer3 = input("whats your favorite weather ,A foggy,B sunny ,C rain ,D snow.")
if answer3 == "A"or"a":
    fall_points += 1
elif answer3 == "B"or"b":
    summer_points += 1
elif answer3 == "C"or"c":
    spring_points +=1
elif answer3 == "D"or"d":
    winter_points +=1

answer4 = input("whats your favorite book out of these 4 ,A twilight,B Percy Jackson ,C any fantasy novel ,D Harry Potter but the author is terible i know.")
if answer4 == "A"or"a":
    fall_points += 1
elif answer4 == "B"or"b":
    summer_points += 1
    answer5 = input("what is your fav percy jackson character, A Nico De Angelo,B Percy Jackson,C Annabeth Chase, D Hazel Lavesque")
    if answer5=="A"or"a":
        fall_points+= 10
    elif answer5 == "B"or"b":
        summer_points+= 1
    elif answer5 == "C"or"c":
        summer_points += 1
    elif answer5=="D"or"d":
        summer_points+=5
elif answer4 == "C"or"c":
    spring_points +=1
elif answer4 == "D"or"d":
    winter_points +=1

answer6 = input("whats your favorite ,A sugar glider,B sea bunny ,C bunny ,D feret.")
if answer6 == "A"or"a":
    fall_points += 1
elif answer6 == "B"or"b":
    summer_points += 1
elif answer6 == "C"or"c":
    spring_points +=1
elif answer6 == "D"or"d":
    
    winter_points +=1
if fall_points > winter_points and fall_points > spring_points and fall_points > summer_points:
    print("You are a Fall person!! :D")
elif winter_points > fall_points and winter_points > spring_points and winter_points > summer_points:
     print("You are a winter person! :)")
elif spring_points > winter_points and spring_points > summer_points and spring_points > fall_points:
    print("You are a Spring person!")
elif summer_points > spring_points and summer_points > fall_points and summer_points > winter_points:
     print("You are a Summer person.")