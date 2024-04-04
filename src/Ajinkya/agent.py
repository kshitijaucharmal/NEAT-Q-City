from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import mean_squared_error
import numpy as np

memory_size = 5000
batch_size = 3

class DQNagent:
    def __init__(self, num_states, num_actions):
        self.replay_memory = deque(maxlen=memory_size)
        self.q_values = np.ones(shape=num_actions)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.batch_size = batch_size
        self.num_episodes = 1000
        self.num_actions = num_actions
        self.num_states = num_states
        self.model = self.create_model(num_states, num_actions)
        self.target_model = self.create_model(num_states, num_actions)
        self.target_model.set_weights(self.model.get_weights())

    def create_model(self, num_states, num_actions):
        model = Sequential()
        model.add(InputLayer(input_shape=num_states))
        model.add(Dense(32, activation='tanh'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(units=num_actions, activation='relu'))
        model.compile(optimizer=Adam(), metrics=['accuracy'], loss=mean_squared_error)
        return model

    def update_q_values(self):
      if len(self.replay_memory) < self.batch_size:
          return
      else:
          batch_indices = np.random.choice(len(self.replay_memory), self.batch_size, replace=False)
          batch = [self.replay_memory[i] for i in batch_indices]
          states, actions, rewards, next_states, dones = zip(*batch)

          updated_q_values = np.zeros((self.batch_size, self.num_actions))
          for i, (state, action, reward, next_state, done) in enumerate(zip(states, actions, rewards, next_states, dones)):
              target_q_value = reward
              if not done:
                  print(f"next_state:",np.array([next_state]))
                  next_q_values = self.target_model.predict(np.array([next_state]))[0]
                  target_q_value += self.gamma * np.max(next_q_values)

              q_values = self.model.predict(np.array([state]))[0]
              print(f"q_values",q_values)
              print(f"action:",action)
              q_values[action] = target_q_value
              updated_q_values[i] = q_values

          print(f"states:",np.array(states))
          print(f"updated_q_values",updated_q_values)
          self.model.fit(np.array(states), updated_q_values, epochs=1, verbose=0)


    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.num_actions)
        else:
            q_values = self.model.predict(np.array([state]))[0]
            return np.argmax(q_values)

    def store_experience(self, state, action, reward, next_state, done):
        self.replay_memory.append((state, action, reward, next_state, done))

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def predict(self):
        return self.model.predict(self.num_states)