rewards_Arr = [
    [0.14, -0.16, -0.12, 0.11, 0.14, -0.17, -0.2, -0.1, 0.7, -0.1],
    [0.1, 0.4, 0.5, 0.1, 0.1, -0.1, -0.3, 0.01, 0.2, -0.1],
    [0.2, -0.5, -0.2, 0.5, 0.1, 0.3, 0.3, -0.2, -0.3, -0.3],
    [0.1, -0.3, -0.1, 0.1, 0.01, -0.3, 0.2, -0.1, -0.3, 0],
    [0.1, 0.3, 0.1, 0.3, 0.7, 0.5, 0.1, -0.2, 0.1, -0.2],
    [0.6, -0.3, 0.2, -0.5, -0.1, -0.1, -0.1, -0.4, -0.2, 0.3],
    [0.4, -0.1, -0.2, 0.6, 0.1, 0.2, 0.5, -0.4, -0.2, 0.2],
    [0.08, 0, -0.06, 0.1, 0.1, 0.7, 0.1, -0.13, -0.1, -0.08],
    [0.2, -0.4, 0, 0.1, 0.1, -0.13, -0.12, -0.1, 0, 0.8],
    [-0.1, 0.4, 0.2, 0.1, 0, 0, 0.3, 0.2, 0.1, 0],
]
weights = [0.1, 0.3, 0.2, 0.25, 0.15, 0.25, 0.3, 0.1, 0.2, 0.15]


class env:
    def __init__(self, state):
        self.current_state = state

    def step(self, action):
        next_state = self.current_state.copy()
        reward = 0
        done = False
        for i in range(len(next_state)):
            # can be changed
            next_state[i] += 0.1 * rewards_Arr[action][i] * weights[i]
            reward += 0.1 * rewards_Arr[action][i] * weights[i]

        self.current_state = next_state
        return next_state, reward, done

    """
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
    """
