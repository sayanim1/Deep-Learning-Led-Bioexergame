import numpy as np
from utils import generate_transition_linear, generate_transition_cub

# Test Linear Transition (Root)
start_pos = np.array([0, 0, 0])
end_pos = np.array([10, 5, 2])
root_trans = generate_transition_linear(start_pos, end_pos, n_frames=5)
print("Root Transition (Linear):\n", root_trans)

# Test Rotation Transition (Joints)
start_rot = np.array([0.1, 0.2, 0.3])
end_rot = np.array([0.5, 0.6, 0.7])
rot_trans = generate_transition_cub(start_rot, end_rot, n_frames=5)
print("\nJoint Transition (Log-space):\n", rot_trans)
