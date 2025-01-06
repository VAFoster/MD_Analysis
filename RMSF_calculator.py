# RMSF Calculator
# Requirements: matplotlib.pyplot, MDtraj, numpy

import mdtraj as md
import matplotlib.pyplot as plt
import numpy as np


# Load Trajectory
traj = md.load([f"/Path/to/traj/file/step7_{i}.xtc" for i in range(1, 10)], #replace range with # of .xtc files, add 1 to top range.
               top='/Path/to/input/topology/file/step5_input.psf') # .psf .pdb and other file types accepted

# Select res for RMSF Calculations
    # replace 'selection' with your res. ex. 'protein' 'POPC' 'protein or resname POPC'
sel = traj.topology.select('selection')
sel_traj = traj.atom_slice(sel)

# Calculate RMSF
rmsf = md.rmsf(sel_traj, sel_traj)

# Generate indicies
residue_indices = [traj.topology.atom(i).residue.index for i in sel_traj]

# Plot RMSF vs. Index
plt.figure(figsize=(8, 4))
plt.plot(residue_indices, rmsf, label="Series Title", color="red")
plt.title("Graph Title")
plt.xlabel("Residue Index")
plt.ylabel("RMSD (nm)")
plt.legend()
plt.show()