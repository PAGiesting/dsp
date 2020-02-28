# Solution to exercise 1 of Chapter 5 of ThinkStats
# Paul Giesting
# 28 February 2020

import numpy as np
from scipy import stats

# convert the Blue Man Group casting range to cm
# since the BRFSS parameters were quoted in cm
# I always use the conversion factor 1 m = 39.37 in

def InchesToCm(inches):
    return inches / 39.37 * 100

blue_a = InchesToCm(5*12 + 10)
blue_b = InchesToCm(6*12 + 1)

# Now, the definite integral from a to b of the normal distribution...

male_mean = 178
male_sigma = 7.7
cdf_a = stats.norm.cdf(blue_a, loc=male_mean, scale=male_sigma)
cdf_b = stats.norm.cdf(blue_b, loc=male_mean, scale=male_sigma)
blue_range_perc = (cdf_b - cdf_a) * 100
print("The percentage of men whose heights fit the Blue Man Group criterion is")
print(round(blue_range_perc, 0), "%.")