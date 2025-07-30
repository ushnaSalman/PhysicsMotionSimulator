import streamlit as st
import matplotlib.pyplot as plt
from simulator import run_Simulation

st.set_page_config(page_title="Motion Simulator")

st.title("Physics Motion Simulator (1D Kinematics)")

name = st.text_input("Object name" , "Body A")
mass = st.number_input("Mass (kg)", value=1.0)
u = st.number_input("Initial Velocity (u in m/s)", value=0.0)
a = st.number_input("Acceleration in m/s2: ", value=1.0)
t = st.number_input("Time (t in Seconds): ", value=10.0)

if st.button("Run Simulation"):
    obj, final_v, distance, time, velocity, position = run_Simulation(name,mass,u,a,t)

    st.success(f"Final Velocity: {final_v: .2f} m/s")
    st.success(f"Distance: {distance: .2f} m")

    st.subheader("Motion Data Table")
    st.dataframe({"Time (s)" : time, "Velocity (m/s)" : velocity, "Position (m)" : position})

    st.subheader("Velocity vs Time")
    plt.figure()
    plt.plot(time, velocity, label="Velocity", color="purple")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.grid(True)
    st.pyplot(plt)


    st.subheader("Position vs Time")
    plt.figure()
    plt.plot(time, position, label="Position" , color="pink")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.grid(False)
    st.pyplot(plt)


