#!/usr/bin/env python3

import json
import random

votes = json.load(open("votes.json", "r"))

# Assemble a list of choices, where games with more votes show up more times
choices = []
for game in votes:
    for i in range(votes[game]):
        choices.append(game)

# Choose randomly from the choices list and append to schedule
schedule = []
while len(schedule) < len(votes):
    choice = random.choice(choices)
    if choice not in schedule: # Don't play the same game twice
        schedule.append(choice)

# Print the game schedule
for game in schedule:
    print(f"{game} - {votes[game]}")
