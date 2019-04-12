import numpy as np

def load_data():
    x_data = np.array(
        [[ 0, 0 ],
        [ 1, 0 ],
        [ 1, 1 ],
        [ 0, 0 ],
        [ 0, 0 ],
        [ 0, 1 ]])
    y_data = np.array(
        [[ 1, 0, 0 ],
        [ 0, 1, 0 ],
        [ 0, 0, 1 ],
        [ 1, 0, 0 ],
        [ 1, 0, 0 ],
        [ 0, 0, 1 ]])
    return x_data, y_data