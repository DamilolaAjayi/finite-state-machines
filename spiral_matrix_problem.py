from enum import Enum, auto

class States(Enum):
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()
    UP = auto()

def spiral_matrix(arr):
    min_col, max_col = 0, len(arr[0]) - 1
    min_row, max_row = 0, len(arr) - 1

    i, j = 0, 0 # starting point

    current_state = States.RIGHT
    output = []

    total_elements = len(arr) * len(arr[0])

    while len(output) < total_elements:
        output.append(arr[i][j])
        if current_state == States.RIGHT:
            if j < max_col:
                j += 1
            else:
                current_state = States.DOWN
                min_row += 1
                i += 1
        elif current_state == States.DOWN:
            if i < max_row:
                i += 1
            else:
                current_state = States.LEFT
                max_col -= 1
                j -= 1
        elif current_state == States.LEFT:
            if j > min_col:
                j -= 1
            else:
                current_state = States.UP
                max_row -= 1
                i -= 1
        elif current_state == States.UP:
            if i > min_row:
                i -= 1
            else:
                current_state = States.RIGHT
                min_col += 1
                j += 1

    return output

arr = [[1,2,3], [4, 5, 6], [7, 8, 9]]

print(spiral_matrix(arr))