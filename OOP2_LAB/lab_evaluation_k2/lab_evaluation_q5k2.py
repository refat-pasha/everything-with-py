"""
5. A fitness center wants to track the progress of its
members based on the number of workouts they
complete each week. You are asked to create a
Python program that takes a list of members
and their weekly workout counts over several weeks
and calculates the total number of workouts for each member.
• It takes a list of tuples,
where each tuple contains the member's name
and a list of their weekly workout counts.
• It uses a loop to calculate the total workouts
 for each member.
• Returns a dictionary with each member's
 name as the key and their total number of
 workouts as the value.
Sample Input: members_workouts = [ ('John', [3, 4, 2, 5]), ('Emily', [5, 3, 4, 4]), ('Sam', [2, 2, 3, 3]) ]
Output: { 'John': 14, 'Emily': 16, 'Sam': 10 }
"""

def cal_total_time(members_workouts):
    total_workouts = {}
    for member, workouts in members_workouts:
        total_workouts[member] = sum(workouts)
    return total_workouts
members_workouts = [ ('John', [3, 4, 2, 5]),
                     ('Emily', [5, 3, 4, 4]),
                     ('Sam', [2, 2, 3, 3]) ]

"""
jodi sorted caw taile emon
result = dict(cal_total_time(members_workouts))
result = sorted(result.items())

"""

#as required
result = cal_total_time(members_workouts)

print(result)







