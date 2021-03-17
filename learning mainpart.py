
from Maze import Maze
from agency import QLearningTable
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def update():
    history_rewards = []
    total_rewards = 0
    loop_c = 0
    for episode in range(200):
        # initial observation
        loop_c += 1
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)
            
        
            total_rewards += reward
            
            
            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                history_rewards.append(total_rewards)
                break
            

            
    fig, axs = plt.subplots()
    axs.set_xlabel('explore times')
    axs.set_ylabel('accumulated reward')
    plt.plot(history_rewards)
    plt.show()
    # end of game
    print('game over')
    env.destroy()
   
    return loop_c

if __name__ == "__main__":


    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    
    env.after(100, update)
    env.mainloop()

