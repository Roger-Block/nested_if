#========== 1. Nested Decisions: The Adventure Game ==========

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print ("You awoken the bear!!! RUN!!!")
    elif action == "proceed in the dark":
        print ("You fell down a deep hole!")
    else:
        pass


#======= 2. Quick Decisions: The Event Planner ================


attendees = int(input("Enter number of attendees:"))
if attendees > 100:
    venue = "large hall"
else:
    venue = "conference room"
print(venue)


  
#=============== Task 2: Catering Choices =======================



vegetarian = input("Do you want vegetarian food? Yes or No?")
if vegetarian == "Yes":
    print("We recommend Veggie Delight Caterers for vegetarian food.")
elif vegetarian == "No":
    print("We recommend Gourmet Meals Caterers for non-vegetarian food.")
else:
    pass