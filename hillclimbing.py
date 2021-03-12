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
      
    for i in range(30):
        gradients = []
        
        for observe in range(4):
            a, s ,ss, done = env.observe(observe)
            if ss == 1:
                gradient = 100000000
                gradients.append(gradient)
            
            else:
                gradient = -s[0]-s[1]-s[2]-s[3]
                gradients.append(gradient)
                
        print(gradients)      
        action = gradients.index(min(gradients))
        
        print(action)
        if isinstance(action,list):
            env.render()
            s_, done_ = env.step(random.choice(action))
            if s_ == 'termimus':
                    print('game over')
                    break

        else:
            env.render()
            s_, done_ = env.step(action)  
            if s_ == 'termimus':
                    print('game over')
                    break
            
            
        

if __name__ == "__main__":

    env = Maze()
    env.after(100, update)
    env.mainloop()

