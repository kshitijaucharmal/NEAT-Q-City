from collections import deque,namedtuple
import random
import numpy as np

class ExperienceReplay:
    def __init__(self,capacity,batch_size):
        self.memory=deque(maxlen=capacity)
        self.batch_size=batch_size
        self.Experience=namedtuple('Experience',['state','action','reward','next_state','done'])
    

    def add_experience(self,state,action,reward,next_state,done):
        expeirence=self.Experience(state,action,reward,next_state,done)
        self.memory.append(expeirence)

    def sample_batch(self):
        batch=random.sample(self.memory,self.batch_size)
        return batch
    
    def can_provide_sample(self):
        return len(self.memory) >= self.batch_size
    
