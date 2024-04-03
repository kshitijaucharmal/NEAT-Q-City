from neat.genome import Genome
from neat.geneh import GeneHistory
import numpy as np

class Agent:
    def __init__(self):
        self.no_of_states=10
        self.no_of_actions=10
        self.gamma=0.99
        self.epsilon=1
        self.epsilon_decay=0.998
        self.epsilon_end=0.1
        #self.model=self.build_model()
        self.gh=GeneHistory(self.no_of_states,self.no_of_actions)

    def model(self):
        self.g = Genome(self.gh)
        for i in range(50):
            self.g.mutate()
        pass

    def predict(self,inputs):
        return self.g.feed_forward(inputs)
    
    def fit(self,inputs,targets,epochs):
        for _ in range(epochs):
            self.g.backpropogate(inputs, targets)

        mse=self.g.mean_squared_error(targets,self.predict(inputs))
        print("Mean squared error:", mse)
    
    def get_action(self,state):

        if np.random.rand() <= self.epsilon:
            #Exploration
            action = np.random.randint(0,10)
        else:
            #Exploitation
            # Add an extra dimension to the state to create a batch with one instance
            state=np.expand_dims(state,axis=0)

            #prdicting the q_values from the model
            q_values=self.predict(state)
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

            current_q_value=self.predict(states)
            next_q_values=self.predict(next_states)

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

            current_q_value=self.predict(states)
            next_q_values=self.predict(next_states)

            self.fit(states,target_q_values,epochs=10)

        # def load(self,file_path):
        #     self.model=load_model(file_path)

        # def save(self,file_path):
        #     self.model.save(file_path)







