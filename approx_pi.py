from random import random

def approx_pi(total_samples):

    samples_in_circle = 0

    for i in range(total_samples):
        x = random()
        y = random()

        # is the sample in the circle?
        if x**2 + y**2 < 1:
            samples_in_circle += 1

    return 4.0 * float(samples_in_circle) / float(total_samples)

print approx_pi(10000)
