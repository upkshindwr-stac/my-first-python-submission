race_results = {}
positions = ["Winner","Runner Up","Third Place"]
for position in positions:
    print(f"\nEnter details for the {position}")
    athlete_name = input("Athlete Name:")
    athlete_timing = input("Race Timing:")
    athlete_country = input("athlete_country:")

    race_results[position] = {
        "Name" : athlete_name,
        "Timing" : athlete_timing,
        "Country" : athlete_country
     }
print("\n===== Asian Games Men's 100m Results =====")

for position, details in race_results.items():
    print(f"\n{position}")
    print(f"Name    : {details['Name']}")
    print(f"Timing  : {details['Timing']}")
    print(f"Country : {details['Country']}")

view_position = input (
     "\nEnter the position you want to view "
    "(Winner / Runner Up / Third Place): "
)

if view_position in race_results:

    print(f"\nDetails of the {view_position}")
    print(f"Name    : {race_results[view_position]['Name']}")
    print(f"Timing  : {race_results[view_position]['Timing']}")
    print(f"Country : {race_results[view_position]['Country']}")

else:
    print("Sorry, invalid position entered.")