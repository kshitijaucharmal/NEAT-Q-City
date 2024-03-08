from keras.layers import InputLayer,Dense
from keras import Sequential
from keras.optimizers import Adam,SGD
from keras.losses import mean_squared_error
import numpy as np
from collections import deque
import tensorflow as tf


memory_size=5000
batch_size=3


#OBSERVATIONS

input_values = [12,4,10,6,1,40,9,4,8,3]
observations_parm = ['Population density', 'Pollution', 'Recreation', 'Literacy rate',
                'Crime rate', 'Household income', 'Green space', 'Healthcare',
                'Employment rate', 'Internet coverage']
state =np.array(input_values)
num_states = len(observations_parm)


#  ACTIONS
actions_parm = ['Building hospital', 'Building park', 'Building factory', 'Expand roads',
           'Building education institutes', 'Residential building', 'Building Offices',
           'Building Police station', 'Building Communication tower', 'Building Farms']
num_actions = len(actions_parm)

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

rewards_Arr=[[5, -4, 5, 5, -4, 5, 4, 5, 5, 4],
             [4, -4, 5, 5, 4, 4, 5, 4, 4, 4],
             [-5, 5, -5, -4, 5, 5, -4, -5, 5, 5],
             [3, -3, 3, 3, -3, 3, 3, 3, 3, 3],
             [4, -4, 5, 5, -4, 5, 4, 5, 5, 5],
             [4, -3, 4, 4, -3, 4, 4, 4, 4, 4],
             [5, -4, 5, 5, -4, 5, 4, 5, 5, 5],
             [5, 4, 5, 5, 4, 5, 4, 5, 5, 5],
             [4, 4, 4, 5, 4, 4, 4, 5, 5, 4],
             [4, -3, 4, 4, -3, 4, 4, 4, 4, 4]]

class DQNagent:
    def __init__(self,num_states,num_actions):
        self.replay_memory=deque(maxlen=memory_size)
        self.q_values=np.ones(shape=num_actions)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.batch_size = 3
        self.num_episodes = 1000
        self.num_actions=num_actions
        self.num_states=num_states
        self.model = self.create_model(num_states, num_actions)
        self.target_model = self.create_model(num_states, num_actions)
        self.target_model.set_weights(self.model.get_weights())

    def create_model(self,num_states, num_actions):
        model=Sequential()
        model.add(InputLayer(input_shape=num_states))
        model.add(Dense(32,activation='tanh'))
        model.add(Dense(64,activation='relu'))
        model.add(Dense(64,activation='relu'))
        model.add(Dense(units=num_actions,activation='relu'))
        model.compile(optimizer=Adam(),metrics=['accuracy'],loss=mean_squared_error)
        return model

    def update_q_values(self):
        if len(self.replay_memory) < batch_size:
            return
        else:
            batch = np.array(self.replay_memory)[np.random.choice(len(self.replay_memory), batch_size, replace=False)]
            states, actions, rewards, next_states, dones = zip(*batch)

            updated_q_values = []
            for state, action, reward, next_state, done in zip(states, actions, rewards, next_states, dones):
                if done:
                    target_q_value = reward
                else:
                    next_q_values = self.target_model.predict(np.array([next_state]))[0]
                    target_q_value = reward + self.gamma * np.max(next_q_values)
                q_values = self.model.predict(np.array([state]))[0]
                q_values[action] = target_q_value
                updated_q_values.append(q_values)
            updated_q_values = np.array(updated_q_values)
            self.model.fit(np.array(states), updated_q_values, epochs=1, verbose=0)

    def select_action(self,state):
        state=state
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.num_actions)
        else:
            q_values = self.model.predict(np.array([state]))[0]
            return np.array(q_values)

    def store_experience(self,state, action, reward, next_state, done):
        self.replay_memory.append((state, action, reward, next_state, done))

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def predict(self,stats):
        self.stats=stats
        self.prediction=self.model.predict(stats)
        print(self.prediction)

class env:
    def __init__(self,state):
        self.current_state=state
    def step(self,action):
        next_state = [0] * 10  # Initialize next_state with 10 elements
        reward = 0  # Initialize reward
        done=False
        for i in range(10):
            for j in range(10):
                next_state[i] += self.current_state[j] - 10 * action * rewards_Arr[i][j]
                reward += 10 * action * rewards_Arr[i][j]

        return next_state, reward,done

def train(agent, num_episodes, stats, env):
    for epoch in range(num_episodes):
        total_reward = 0
        done = False
        state = env.current_state
        print("Epoch:", epoch)
        i=10
        while (i):
            action = agent.select_action(stats)
            next_state, reward, done = env.step(action)
            agent.store_experience(state, action, reward, next_state, done)
            agent.update_q_values()
            state = next_state
            total_reward += reward
            print("Action:", action, "Reward:", reward, "Total Reward:", total_reward)
            i-=1



agent=DQNagent(num_states=num_states, num_actions=num_actions)
environment=env(state)
train(agent,num_episodes=1,stats=state,env=environment)

'''
input_values.append(float(input("Enter population density: ")))
input_values.append(float(input("Enter pollution: ")))
input_values.append(float(input("Enter entertainment: ")))
input_values.append(float(input("Enter literacy rate: ")))
input_values.append(float(input("Enter crime rate: ")))
input_values.append(float(input("Enter household income: ")))
input_values.append(float(input("Enter green space: ")))
input_values.append(float(input("Enter healthcare: ")))
input_values.append(float(input("Enter employment rate: ")))
input_values.append(float(input("Enter internet range: ")))
'''
new_states=np.array([[0,0,1,0,0,0,0,0,0,0]])
pred=agent.predict(new_states)
print(pred)