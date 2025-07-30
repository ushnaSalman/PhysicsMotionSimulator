from motion import Body

def run_Simulation(name,mass,u,a,t):
    obj = Body(name,mass,u,a,t)
    final_v = obj.finalvelocity()
    distance = obj.distanceCovered()
    time,velocity,position = obj.motion_arrays()
    return obj,final_v,distance,time,velocity,position


