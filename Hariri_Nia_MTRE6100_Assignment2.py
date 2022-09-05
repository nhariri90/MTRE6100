#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import random

ENV_ALL_POSITIONS=[0,1,2,3] #The potential positons of robot
ENV_TRUTH_MEASUREMENT=["wall","door","wall","door"] #the ground truth of measurement at each position
MAX_STEP =  4

def trasition_probability(control = None,current_state = None, previous_state = None ): #_Complete inputs 
        #10% robot travels 2 states
        #20% Robot stays
        #70% Robot travels to next state
        #robot will not move backwards
        if (control is None or current_state is None or previous_state is None):
            return 0
        if control != 1:
            return (0)
        diff_states = current_state - previous_state
        if diff_states == 1:
            return .7
        elif diff_states == 2:
            return .1
        else:
            return 0

def measurement_probabiliy(sensor_measurement, current_state ):
    # the observation state / measurement state depends only on the current state.
    # 20% robot sees wall infront of door
    # 80% robot sees door infront of door
    # 30% robot sees door infront of wall
    # 70% robot sees wall infront of wall
    truth_measurement = ENV_TRUTH_MEASUREMENT[current_state]

    if sensor_measurement == truth_measurement:
        if sensor_measurement == 'wall':
            return .7
        elif sensor_measurement == 'door':
            return .8
        else:
            return 0
    elif sensor_measurement !=truth_measurement:
        if sensor_measurement == 'wall':
            return .2
        elif sensor_measurement == 'door':
            return .8
        else:
            return 0
    else:
        return 0

def get_real_measurement(current_state = None):
    if (current_state is None):
        user_input = input( "Please enter either Wall or Door" )
        if (user_input == 'Wall' or user_input == 'wall'):
            return 'wall'
        elif (user_input == 'Door' or user_input == 'door'):
            return 'door'
    else:
        truth_measurement = ENV_TRUTH_MEASUREMENT[current_state]
        random_number = random.random()
        if (truth_measurement == 'wall'):
            if(random_number < .3):
                return 'door'
            else:
                return 'wall'
        
        elif (truth_measurement == 'door'):
            if(random_number < .2):
                return 'wall'
            else:
                return 'door'
def normalize(R):
    s=sum(R)
    for i in range (len( R ) ):
        R[i] = R[i] / s
        
def main():
        belief = [.25,.25,.25,.25]
        belief_star=[0,0,0,0]
        for step in range(0, MAX_STEP):
            #first step of bayes filter is to get belief_star
            # discrete value = sum (Prob of ccurrent state from all states given the control = 1)
            # transition / control update state of bayes filter updating belief_sar
            for state in range( len(ENV_ALL_POSITIONS ) ):
                for previous_state in range( len(ENV_ALL_POSITIONS ) ):
                    temp_array = []
                    temp_array.append(trasition_probability(control = 1, current_state=state, previous_state = previous_state)*belief[previous_state])
                         

            #----------------------------------------------------------------------------------------------------
            # measurement stage of bayes
            temp_belief_array = []
            for state in range( len( ENV_ALL_POSITIONS ) ):
                for current_state in range( len( ENV_ALL_POSITIONS ) ):
                    temp_belief_array.append(measurement_probabiliy ( sensor_measurement = get_real_measurement, current_state = current_state) * belief_star[state] )
                
#pos = temp_array*temp_belief_array
#plt.hist(pos)
#plt.show

    
if __name__ == '__main__': #dunder or magic methods
    '''main'''
    main()
   
    
