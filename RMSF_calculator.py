# RMSF Calculator
# Requirements: matplotlib.pyplot, MDtraj, numpy

import mdtraj as md
import matplotlib.pyplot as plt
import numpy as np


# Load Trajectory
traj = md.load([f"/Path/to/traj/file/step7_{i}.xtc" for i in range(1, 10)], #replace range with # of .xtc files, add 1 to top range.
               top='/Path/to/input/topology/file/step5_input.psf') # .psf .pdb and other file types accepted

# Select res for RMSD Calculations
    # replace 'selection' with your res. ex. 'protein' 'POPC' 'protein or resname POPC'
sel = traj.topology.select('selection')
sel_traj = traj.atom_slice(sel)

# Calculate RMSD--using frame 0 as reference
rmsf = md.rmsf(sel_traj, sel_traj, 0)

# Calculate Time
steps = 30
time_per_step_ns = 1
frames = traj.n_frames

# Generate Time Array
time = np.linspace(0, steps * time_per_step_ns, frames)

# Plot RMSD vs. Time
plt.figure(figsize=(8, 4))
plt.plot(time, rmsf, label="Series Title", color="red")
plt.title("Graph Title")
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.legend()
plt.show()