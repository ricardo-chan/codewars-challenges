def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1)*(tot_rows - row)

print(seats_in_theater(16, 11, 5, 3))