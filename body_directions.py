def head_direction(positions_x, positions_y):
    x_old = positions_x[len(positions_x)-2]; x_new = positions_x[len(positions_x)-1]
    y_old = positions_y[len(positions_y)-2]; y_new = positions_y[len(positions_y)-1]

    if x_old - x_new < 0:
        return 270
    if x_old - x_new > 0:
        return 90
    if y_old - y_new > 0:
        return 0
    if y_old - y_new < 0:
        return 180

    print('to se nemělo stát')

def tail_direction(positions_x, positions_y, last_position_x, last_position_y):
    x_new = positions_x[0]
    y_new = positions_y[0]

    if last_position_x - x_new < 0:
        return 270
    if last_position_x - x_new > 0:
        return 90
    if last_position_y - y_new > 0:
        return 0
    if last_position_y - y_new < 0:
        return 180

    print('to se nemělo stát')