rewards_Arr = [[0.5, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.4],
               [0.4, -0.4, 0.5, 0.5, 0.4, 0.4, 0.5, 0.4, 0.4, 0.4],
               [-0.5, 0.5, -0.5, -0.4, 0.5, 0.5, -0.4, -0.5, 0.5, 0.5],
               [0.3, -0.3, 0.3, 0.3, -0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
               [0.4, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
               [0.4, -0.3, 0.4, 0.4, -0.3, 0.4, 0.4, 0.4, 0.4, 0.4],
               [0.5, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
               [0.5, 0.4, 0.5, 0.5, 0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
               [0.4, 0.4, 0.4, 0.5, 0.4, 0.4, 0.4, 0.5, 0.5, 0.4],
               [0.4, -0.3, 0.4, 0.4, -0.3, 0.4, 0.4, 0.4, 0.4, 0.4]]

class env:
    def __init__(self, state):
        self.current_state = state

    def step(self, action):
        next_state = self.current_state.copy()
        reward = 0
        done = False
        for i in range(len(self.current_state)):
            # can be changed
            next_state[i] -= 0.1 * rewards_Arr[action][i]# *weights[i]
            reward += 0.1 * rewards_Arr[action][i]# *weights[i]

        # self.current_state = next_state
        return next_state, reward, done

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