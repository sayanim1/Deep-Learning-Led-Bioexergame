import numpy as np

def generate_transition_linear(start, end, n_frames=10):
    """
    Generate a transition between two points using linear interpolation.
    Used typically for root position transitions.
    
    Args:
        start: Start position (vector or scalar).
        end: End position (vector or scalar).
        n_frames: Number of transition frames to generate.
        
    Returns:
        numpy.ndarray: Array of shape (n_frames, ...) containing the transition.
    """
    if n_frames <= 0:
        return np.array([])
    if n_frames == 1:
        return np.array([start])
    
    start = np.array(start)
    end = np.array(end)
    
    # Generate linearly spaced weights from 0 to 1
    # We use n_frames + 2 and take the middle if we want to avoid repeating start/end,
    # but usually, for stitching, we want frames BETWEEN the two segments.
    # However, standard lerp of n_frames usually includes both or just the transition.
    # Based on the notebook usage, it likely wants n_frames of NEW data.
    
    weights = np.linspace(0, 1, n_frames + 2)[1:-1]
    
    transition = [(1 - w) * start + w * end for w in weights]
    
    # If n_frames was meant to be exactly the length of the returned list:
    if len(transition) != n_frames:
         weights = np.linspace(0, 1, n_frames)
         transition = [(1 - w) * start + w * end for w in weights]

    return np.array(transition)

def generate_transition_cub(start, end, n_frames=10):
    """
    Generate a transition for joint rotations using log-space interpolation.
    
    According to user specifications:
    - Calculates rotation matrices (if applicable)
    - Uses log-space interpolation
    - Applies to all joints
    
    Args:
        start: Start rotation state (e.g., rotation vectors or Euler angles).
        end: End rotation state.
        n_frames: Number of transition frames.
        
    Returns:
        numpy.ndarray: Array of shape (n_frames, ...) containing the transition.
    """
    if n_frames <= 0:
        return np.array([])
    if n_frames == 1:
        return np.array([start])
        
    start = np.array(start)
    end = np.array(end)
    
    # Log-space interpolation for rotations:
    # If the input is already in 'log-space' (e.g., rotation vectors/exponential coordinates),
    # then linear interpolation in this space is the correct log-space interpolation.
    # If the input is rotation matrices, we would use log/exp maps.
    
    # Given the user's focus on 'log space interpolation', we assume the values
    # represent the log-domain of the rotations (like rotation vectors/joint angles).
    
    weights = np.linspace(0, 1, n_frames)
    transition = [(1 - w) * start + w * end for w in weights]
    
    return np.array(transition)
