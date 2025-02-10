# Your colleagues have been looking over your shoulder. When you should have been doing your 
# boring real job, you've been using the work computers to smash in endless hours of codewars.

# In a team meeting, a terrible, awful person declares to the group that you aren't working. 
# You're in trouble. You quickly have to gauge the feeling in the room to decide whether or not 
# you should gather your things and leave.

# Given an object ( meet ) containing team member names as keys, and their happiness rating out 
# of 10 as the value, you need to assess the overall happiness rating of the group. If <= 5, return 
# 'Get Out Now!'. Else return 'Nice Work Champ!'.

# Happiness rating will be total score / number of people in the room.

# Note that your boss is in the room ( boss ). Their score is worth double its face value (but they 
# are still just one person!).

def outed(meet, boss):
    """
    Assesses average rating of team meeting.

    Args:
        meet: A dictionary where keys are team member names (strings) and
              values are their happiness ratings (integers).
        boss: The name (key) of the boss in the meet dictionary, whose score is doubled.

    Returns:
        'Get Out Now!' if the average happiness rating is <= 5,
        otherwise 'Nice Work Champ!'.
    """
    total_score = 0
    number_of_people = len(meet)

    for person, score in meet.items():
        if person == boss:
            score *= 2  # Double the boss's score
        total_score += score

    average_happiness = total_score / number_of_people
    return 'Get Out Now!' if average_happiness <= 5 else 'Nice Work Champ!'
