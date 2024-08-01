import numpy as np

def calculate(list):
    # Check if list has 9 elements, if not then raise ValueError
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3*3 matrix 
    arr = np.array(list).reshape((3,3))
    
    # Initialize calculations dictionary
    calculations = dict()

    # Calculate mean - axis 0, axis 1 and flattened
    calculations["mean"] = [
        np.mean(arr, axis=0).tolist(), 
        np.mean(arr, axis=1).tolist(), 
        np.mean(arr)
    ]
    
    # Calculate variance - axis 0, axis 1 and flattened
    calculations["variance"] = [
        np.var(arr, axis=0).tolist(), 
        np.var(arr, axis=1).tolist(), 
        np.var(arr)
    ]

    # Calculate standard deviation - axis 0, axis 1 and flattened
    calculations["standard deviation"] = [
        np.std(arr, axis=0).tolist(), 
        np.std(arr, axis=1).tolist(), 
        np.std(arr)
    ]
    
    # Calculate max - axis 0, axis 1 and flattened
    calculations["max"] = [
        np.max(arr, axis=0).tolist(), 
        np.max(arr, axis=1).tolist(), 
        np.max(arr)
    ]

    # Calculate min - axis 0, axis 1 and flattened
    calculations["min"] = [
        np.min(arr, axis=0).tolist(), 
        np.min(arr, axis=1).tolist(), 
        np.min(arr)
    ]

    # Calculate sum - axis 0, axis 1 and flattened
    calculations["sum"] = [
        np.sum(arr, axis=0).tolist(), 
        np.sum(arr, axis=1).tolist(), 
        np.sum(arr)
    ]

    return calculations