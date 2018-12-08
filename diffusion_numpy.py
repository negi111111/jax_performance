import numpy as np
import time

grid_shape = (1024, 1024)


def laplacian(grid):
    return np.roll(grid, +1, 0) + np.roll(grid, -1, 0) + np.roll(grid, +1, 1) + np.roll(grid, -1, 1) - 4 * grid


def evolve(grid, dt, D=1):
    return grid + dt * D * laplacian(grid)


def run_experiment(num_iterations):
    grid = np.zeros(grid_shape)
    block_low = int(grid_shape[0] * .4)
    block_high = int(grid_shape[0] * .5)
    grid[block_low:block_high, block_low:block_high] = 0.005

    start = time.time()
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)
    return time.time() - start


if __name__ == '__main__':
    time = run_experiment(1)
    print(time)
