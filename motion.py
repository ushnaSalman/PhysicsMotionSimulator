import numpy as np

class Body:
    def __init__(self,name,mass,u,a,t):
        self.name = name 
        self.u = u
        self.mass = mass
        self.a = a
        self.t = t

    def finalvelocity(self):
        return self.u + self.a * self.t

    def distanceCovered(self):
        return self.u * self.t + 0.5 * self.a * self.t**2

    def motion_arrays(self, step=0.1):
        time = np.arange(0, self.t + step, step)
        velocity = self.u + self.a * time
        position = self.u * time + 0.5 * self.a * time**2
        return time, velocity, position 


