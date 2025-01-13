#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A code that appreciates every member of group-23

Parameters:
    - group_23: Takes an array of string input names of group members.
    - codes: Takes an array of unique code numbers corresponding to each name in group_23.

@author: Novel Yonas

Idea enriched from the book 'PYTHON CRUSH COURSE' by Eric Matthes.
"""

group_23 = [
    "Bhang",
    "Ava",
    "Ibrahim",
    "Sadam",
    "Saeed",
    "Hasan",
    "Anyak",
    "Cynthia",
    "Nahom",
]
codes = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Unique codes for each member

# Create a dictionary to map names to codes
name_code_mapping = dict(zip(group_23, codes))

# Request user input for the code
code_input = int(input("Please enter your number: "))

# Check if the code exists and print the corresponding message
for name, code in name_code_mapping.items():
    if code == code_input:
        print(name.title() + ", that was a great time working with you!")
        print(
            "I can't wait to communicate with you in the future, "
            + name.title()
            + ".\n"
        )
        break
else:
    print("The code entered does not match any member of the group.")
