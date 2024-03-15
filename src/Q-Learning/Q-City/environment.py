import numpy as np
import random


states = ['Population density', 'Pollution', 'Recreation', 'Literacy rate',
        'Crime rate', 'Household income', 'Green space', 'Healthcare',
        'Employment rate', 'Internet coverage']
# example: [5,3,2,1,4,5,2,4,1,5] 

actions = ['Building hospital', 'Building park', 'Building factory', 'Expand roads',
          'Building education institutes', 'Residential building', 'Building Offices',
          'Building Police station', 'Building Communication tower', 'Building Farms']

rewards = {
    'Building hospital': [5, -4, 5, 5, -4, 5, 4, 5, 5, 4],
    'Building park': [4, -4, 5, 5, 4, 4, 5, 4, 4, 4],
    'Building factory': [-5, 5, -5, -4, 5, 5, -4, -5, 5, 5],
    'Expand roads': [3, -3, 3, 3, -3, 3, 3, 3, 3, 3],
    'Building education institutes': [4, -4, 5, 5, -4, 5, 4, 5, 5, 5],
    'Residential building': [4, -3, 4, 4, -3, 4, 4, 4, 4, 4],
    'Building Offices': [5, -4, 5, 5, -4, 5, 4, 5, 5, 5],
    'Building Police station': [5, 4, 5, 5, 4, 5, 4, 5, 5, 5],
    'Building Communication tower': [4, 4, 4, 5, 4, 4, 4, 5, 5, 4],
    'Building Farms': [4, -3, 4, 4, -3, 4, 4, 4, 4, 4],
}


reward_arr = [[5, -4, 5, 5, -4, 5, 4, 5, 5, 4],
               [4, -4, 5, 5, 4, 4, 5, 4, 4, 4],
               [-5, 5, -5, -4, 5, 5, -4, -5, 5, 5],
               [3, -3, 3, 3, -3, 3, 3, 3, 3, 3],
               [4, -4, 5, 5, -4, 5, 4, 5, 5, 5],
               [4, -3, 4, 4, -3, 4, 4, 4, 4, 4],
               [5, -4, 5, 5, -4, 5, 4, 5, 5, 5],
               [5, 4, 5, 5, 4, 5, 4, 5, 5, 5],
               [4, 4, 4, 5, 4, 4, 4, 5, 5, 4],
               [4, -3, 4, 4, -3, 4, 4, 4, 4, 4]]

state_arr = [12, 4, 10, 6, 1, 40, 9, 4, 8, 3]

class Environment:
    def __init__(self,no_of_states=10):
        self.no_of_states=no_of_states
        #self.state = state

    def reset(self):
        # once an episode is done the environment gets reset to an random state
        for i in range(self.no_of_states):
            self.state[i]=random.randint(1,10)

        return (self.get_state())
    
    def move_by_agent(self,action):
        done = False  # The episode is not done by default
        reward = [0,0,0,0,0,0,0,0,0,0]   # Initialize reward

        # A lot of refinement/Optimization is required in reward structure
        self.state[action]+=1
        # There needs to be certain goal in terms of state of an
        # city (optimal parameters) where the agent will be aiming.
        for i in range(self.no_of_states):
            reward[i] += reward_arr[action][i]

        
            
        return reward,done
    #def is valid_location(self,location);

    
    def get_state(self):
        state = np.array(self.state)
        return state 
    
    def step(self,action):
        
        reward,done = self.move_agent(action)
        next_state=self.get_state()
        
        return reward, next_state,done



env = Environment()
print(env.reset())

