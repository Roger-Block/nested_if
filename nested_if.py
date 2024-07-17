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