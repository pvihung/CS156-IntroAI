import math
import random

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv("Data.csv")

# Self note: Create a plot having states and their rewards, similar to the lecture example.
# Move the csv file to the same directory as A3_LocalSearch folder

# A figure with axes
fig, ax = plt.subplots()
# the axes limits xmin, x max, y min, y max
ax.axis([0,100,0,10000])
# create a point in the axes, we are plotting the data from CSV file "Data.csv" . 
# Assume that, there are 100 possible sates Si where i = (1...100) 
# Each state (except state 1 and 100) have exactly 2 neighbours. Si has neighbors Si-1 and Si+1
# Data.csv directly provides the reward/utility of every state (1 to 100). Column named "State" corresponds to state number and its respective row " Reward" corresponds to utility of the state.
ax.plot(df['State'],df['Reward'])
# An animated point used to show the current state on the plot.
point, = ax.plot(0,1, marker="o")

# we will randomly use a state as the initial state. Indexing starts from 0, therefore, we are ommiting that first and last row
start_state=random.randint(1,98)
#Initially current state = start state.
cur_state=start_state

#Temperature = 4000, use this for Section 2, Q2
T = 4000

#A simple hillclimbing method, without sideway moves,  is implemented as an example
def HillClimbNoSideways(time):
    global cur_state #access the curstate as global variable

    #checks neighbors and move only if utility is strictly greater than current state.
    #The point is returned to the animating function which displays it on the plot.
    #Use this code an as example to complete the other two functions.
    if(df["Reward"][cur_state+1] >df["Reward"][cur_state]):
        cur_state=min(cur_state+1,98)
        point.set_data([cur_state], [df['Reward'][cur_state]])
        return point
    elif ( df["Reward"][cur_state - 1]>df["Reward"][cur_state] ):
        cur_state = max(cur_state - 1,1)
        point.set_data([cur_state], [df['Reward'][cur_state]])
        return point
    return point

""" DO NOT MAKE MODIFICATIONS ABOVE THIS LINE"""
#______________________________________________
def HillClimbWithSideways(time):
    global cur_state
    # Complete the code in this function to implement a better hillclimbing
    # method which allows sideways moves with 0.5 probability
    
    cur_destination = df["Reward"][cur_state]
    cur_right = df['Reward'][cur_state + 1]
    cur_left = df['Reward'][cur_state - 1]
    
    # Try to move to the maximum neighbor 
    # But this might have a problem if the neighbor is only a local maximum
    if cur_right > cur_destination:
        cur_state = min(cur_state + 1, 98)
    elif cur_left > cur_destination:
        cur_state = max(cur_state - 1, 1)
    elif (cur_right == cur_destination or cur_left == cur_destination):
        # Check if the probability meets the condition to allow the sideways move
        # random.random() will return a float between 0.0 and 1.0
        # So we can use it to decide to move or not, here, I choose to move if the random number is less than 0.5, which can work similarly in the oposite way
        if random.random() < 0.5:
            if cur_right == cur_destination:
                cur_state = min(cur_state + 1, 98)
            elif cur_left == cur_destination:
                cur_state = max(cur_state - 1, 1)
    # Set data like the previous function example          
    point.set_data([cur_state], [df['Reward'][cur_state]])       
    return point

def SimulatedAnnealing(time):
    global cur_state, T
#     # Complete the code in this function to implement a Simulated annealing method
#     # which allows all upward moves and
#     # which allows downward  moves with  probability  p = e^(delta/T) . delta stands for the differnce in state utility.
#     #Use a linearly decreasing T , that is, T=T-1 every iteration.
#     # The Algorithm must randomly select a neighbor with probability 0.5,
#     # then allow downward moves with probability p

    cur_destination = df["Reward"][cur_state]
    # Randomly select where to move, left or right
    # The concept of this is to choose where to move, then check if the move is valid or not
    # I will move 'crazily' to the point when it can not move to that one side anymore and have to move to the correct one
    
    direction = random.choice([-1, 1])
    if direction == 1:
        next_state = min(cur_state + 1, 98)
    else:
        next_state = max(cur_state - 1, 1)
    next_destination = df["Reward"][next_state]
    # Delta in Simulated Annealing is the difference in reawards (between current and next state)
    # T is the temperature
    # Usually, we might need to find it, but in this case, we already have it defined 
    delta = next_destination - cur_destination
    if delta > 0:
        cur_state = next_state
    elif delta <=0: 
        p = math.exp(delta / T)
        if random.random() < p:
            cur_state = next_state 
    # The linearly decreasing temperature mentioned in the question   
    T = T -1 
    # Since we dont want the temperature to drop to 0 or negative (since T is in the denominator of the probability p)
    # We need to set a boundary condition
    T = max(T, 1)
    point.set_data([cur_state], [df['Reward'][cur_state]])
    return point

# Self note: There might be a problem with this algorithm, for example, there might be a case where we unluckily choose the wrong direction 
# all over again, which make the temperature drop, and when start to move to the correct direction, the temperature is already too low to allow it


""" DO NOT MAKE MODIFICATIONS BELOW THIS LINE, Except for the second parameter in FuncAnimation call"""
#______________________________________________

# This  animation with 50ms interval, which is repeated,
# The second parameter, the function name, is the function that is called
# repeatedly for "frames" (sixth parameter) number of times.
# ani = FuncAnimation(fig,HillClimbNoSideways, interval=50, blit=False, repeat=False, frames=5000)

# Question 1: HiilClimbWithSideways
# ani = FuncAnimation(fig, HillClimbWithSideways, interval=50, blit=False, repeat=False, frames=5000)

# Question 2: SimulatedAnnealing
ani = FuncAnimation(fig, SimulatedAnnealing, interval=50, blit=False, repeat=False, frames=5000)

plt.show()
