# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 22:03:24 2021

@author: boshu
"""

import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 40   # pixels
MAZE_H = 10  # grid height
MAZE_W = 10  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

    def creat_barrier(self,origin,abscissa,ordinate):
        barrier_center = origin + np.array([UNIT * abscissa,UNIT * ordinate])
        self.barrier = self.canvas.create_rectangle(
            barrier_center[0] - 15, barrier_center[1] - 15,
            barrier_center[0] + 15, barrier_center[1] + 15,
            fill='black')
        return self.barrier

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])

        # barrier
        self.barrier1 = self.creat_barrier(origin, 4, 0)
        self.barrier2 = self.creat_barrier(origin, 1, 1)
        self.barrier3 = self.creat_barrier(origin, 2, 2)
        self.barrier4 = self.creat_barrier(origin, 4, 2)
        self.barrier5 = self.creat_barrier(origin, 0, 4)
        self.barrier6 = self.creat_barrier(origin, 3, 4)
        self.barrier7 = self.creat_barrier(origin, 9, 5)
        self.barrier8 = self.creat_barrier(origin, 6, 6)
        self.barrier9 = self.creat_barrier(origin, 7, 7)
        self.barrier10 = self.creat_barrier(origin, 9, 7)
        self.barrier11 = self.creat_barrier(origin, 5, 9)
        self.barrier12 = self.creat_barrier(origin, 8, 9)
        self.barrier13 = self.creat_barrier(origin, 9, 0)
        self.barrier14 = self.creat_barrier(origin, 6, 1)
        self.barrier15 = self.creat_barrier(origin, 7, 2)
        self.barrier16 = self.creat_barrier(origin, 9, 2)
        self.barrier17 = self.creat_barrier(origin, 5, 4)
        self.barrier18 = self.creat_barrier(origin, 8, 4)
        self.barrier19 = self.creat_barrier(origin, 4, 5)
        self.barrier20 = self.creat_barrier(origin, 1, 6)
        self.barrier21 = self.creat_barrier(origin, 2, 7)
        self.barrier22 = self.creat_barrier(origin, 4, 7)
        self.barrier23 = self.creat_barrier(origin, 0, 9)
        self.barrier24 = self.creat_barrier(origin, 3, 9)

        # create red rect
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')

        # create terminus
        terminus = origin + np.array([UNIT * 9,UNIT * 9])
        self.terminus = self.canvas.create_rectangle(
            terminus[0] - 15, terminus[1] - 15,
            terminus[0] + 15, terminus[1] + 15,
            fill='green')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')
        # return observation
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect)  # next state
                # reward function
        
        if s_ in [self.canvas.coords(self.barrier1),
                    self.canvas.coords(self.barrier2),
                    self.canvas.coords(self.barrier3),
                    self.canvas.coords(self.barrier4),
                    self.canvas.coords(self.barrier5),
                    self.canvas.coords(self.barrier6),self.canvas.coords(self.barrier7),
                    self.canvas.coords(self.barrier8),
                    self.canvas.coords(self.barrier9),
                    self.canvas.coords(self.barrier10),
                    self.canvas.coords(self.barrier11),
                    self.canvas.coords(self.barrier12),self.canvas.coords(self.barrier13),
                    self.canvas.coords(self.barrier14),
                    self.canvas.coords(self.barrier15),
                    self.canvas.coords(self.barrier16),
                    self.canvas.coords(self.barrier17),
                    self.canvas.coords(self.barrier18),self.canvas.coords(self.barrier19),
                    self.canvas.coords(self.barrier20),
                    self.canvas.coords(self.barrier21),
                    self.canvas.coords(self.barrier22),
                    self.canvas.coords(self.barrier23),
                    self.canvas.coords(self.barrier24)]:
            
            done = True
            s_ = 'barrier'

        elif s_ == self.canvas.coords(self.terminus):
            done = True
            s_ = 'termimus'

        else:
            done = False


        return s_, done
    
    def observe(self, action):
        ss = 0
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT
                
        s_ = [s[0]+base_action[0],s[1]+base_action[1],s[2]+base_action[0],s[3]+base_action[1]] # next state
        
        if s_ in [self.canvas.coords(self.barrier1),
                    self.canvas.coords(self.barrier2),
                    self.canvas.coords(self.barrier3),
                    self.canvas.coords(self.barrier4),
                    self.canvas.coords(self.barrier5),
                    self.canvas.coords(self.barrier6),
                    self.canvas.coords(self.barrier7),
                    self.canvas.coords(self.barrier8),
                    self.canvas.coords(self.barrier9),
                    self.canvas.coords(self.barrier10),
                    self.canvas.coords(self.barrier11),
                    self.canvas.coords(self.barrier12),
                    self.canvas.coords(self.barrier13),
                    self.canvas.coords(self.barrier14),
                    self.canvas.coords(self.barrier15),
                    self.canvas.coords(self.barrier16),
                    self.canvas.coords(self.barrier17),
                    self.canvas.coords(self.barrier18),
                    self.canvas.coords(self.barrier19),
                    self.canvas.coords(self.barrier20),
                    self.canvas.coords(self.barrier21),
                    self.canvas.coords(self.barrier22),
                    self.canvas.coords(self.barrier23),
                    self.canvas.coords(self.barrier24)]:
            
            done = True
            ss = 1

        elif s_ == self.canvas.coords(self.terminus):
            done = True
            ss = 2

        else:
            done = False


        return s, s_, ss, done

    def render(self):
        time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 0
            s, done = env.step(a)
            if done:
                break

if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()