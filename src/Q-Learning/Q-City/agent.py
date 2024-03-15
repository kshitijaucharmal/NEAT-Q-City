from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model

import numpy as np

class Agent:
    def __init__(self):
        self.no_of_states=10
        self.no_of_actions=10
        self.gamma=0.99
        self.epsilon=1
        self.epsilon_decay=0.998
        self.epsilon_end=0.1
        self.model=self.build_model()


    def build_model(self):
        model=Sequential([
            Dense(128,activation='relu',input_shape=[self.no_of_states]),
            Dense(64,activation='relu'),
            Dense(32,activation='relu'),
            Dense(10,activation='linear')
        ])

        model.compile(optimizer='adam',loss='mse')

        return model
    
    def get_action(self):

        if np.random.rand() <= self.eplison:
            #Exploration
            action = np.random.randint(0,10)
        else:
            #Exploitation
            # Add an extra dimension to the state to create a batch with one instance
            state=np.expand_dims(state,axis=0)

            #prdicting the q_values from the model
            #q_values=self.model.predict(state,verbose=0)
            q_values=self.model.predict(state)
            # Select and return the action with the highest Q-value
            action=np.argmax(q_values[0])

            # Decay the epsilon value to reduce the exploration over time
            if self.epsilon > self.epsilon_end:
                self.epsilon *= self.epsilon_decay
            
            return action
        
        def learn(self,experiences):
            states = np.array([experience.state for experience in experiences])
            actions = np.array([experience.state for experience in experiences])
            rewards = np.array([experience.state for experience in experiences])
            next_states = np.array([experience.state for experience in experiences])
            dones = np.array([experience.state for experience in experiences])

            current_q_value=self.model.predict(states,verbose=0)
            next_q_values=self.model.predict(next_states,verbose=0)

            target_q_values=current_q_value.copy()

            for i in range(len(experiences)):
                if dones[i]:
                    # If the episode is done, there is no next Q-value
                    # [i, actions[i]] is the numpy equivalent of [i][actions[i]]
                    target_q_values[i, actions[i]] = rewards[i]
                else:
                    # The updated Q-value is the reward plus the discounted max Q-value for the next state
                    # [i, actions[i]] is the numpy equivalent of [i][actions[i]]
                    target_q_values[i, actions[i]] = rewards[i] + self.gamma * np.max(next_q_values[i])

            current_q_value=self.model.predict(states,verbose=0)
            next_q_values=self.model.predict(next_states,verbose=0)

            self.model.fit(states,target_q_values,epochs=1,verbose=0)

        def load(self,file_path):
            self.model=load_model(file_path)

        def save(self,file_path):
            self.model.save(file_path)







