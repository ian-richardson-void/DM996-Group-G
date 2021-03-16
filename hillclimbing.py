# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 22:05:44 2021

@author: boshu
"""
from HillMaze import Maze
import matplotlib.pyplot as plt
import numpy as np
import random

def update():
    gradient_history = []
    for i in range(30):
        gradients = []
        
        for observe in range(4):
            a, s ,ss, done = env.observe(observe)
            if ss == 1:
                gradient = 100000000
                gradients.append(gradient)
            
            else:
                gradient = -(s[0]+15)-(s[1]+15)
                gradients.append(gradient)
                
        gradient_history.append(min(gradients)) 
        action = [i for i in range(len(gradients)) if gradients[i] == min(gradients)]
        print(gradients)
        
        env.render()
        s_, done_ = env.step(random.choice(action))
        if s_ == 'termimus':
                    print('game over')
                    break

    fig, axs = plt.subplots()
    axs.set_xlabel('steps')
    axs.set_ylabel('gradient')
    axs.set_xticks(range(0,len(gradient_history),1))
    axs.set_title('steps vs gradient')      
    plt.plot(gradient_history)   
        

if __name__ == "__main__":

    env = Maze()
    env.after(100, update)
    env.mainloop()

