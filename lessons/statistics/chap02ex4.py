# Solution to exercise 4 of Chapter 2 of ThinkStats
# Paul Giesting
# 28 February 2020

import numpy as np
import nsfg

def CohenEffectSize(group1, group2):
    """Computes the size of Cohen's effect for two groups.
    These groups can be Series or DataFrame types.
    I am told that this code will return:
        float if the arguments are Series
        Series if the arguments are DataFrames
    At my current level of mastery I take the latter on faith.
    """

    diff = group1.mean() - group2.mean()
    pooled_var = (len(group1) * group1.var() + len(group2) * group2.var())
    pooled_var /= len(group1) + len(group2)
    return diff / np.sqrt(pooled_var)

# Exercise 2.4. Using the variable totalwgt_lb (from nsfg, which
# reads in the federal pregnancy data file), investigate whether
# first babies are lighter or heavier than others.
# Compute Cohen's _d_ to quantify the difference.
# How does it compare to the difference in pregnancy length?
# [In the text, the difference in pregnancy length between
# the two groups was found to be 0.03 of the pooled standard deviation.]

# Pregnancy data is read in from the nsfg library as a DataFrame
# nsfg calls thinkplot2 which calls pandas... ok.

#subprocess.run(['cd', '~/OneDrive/Documents/Metis/Programming/ThinkStats2/code'])
preg = nsfg.ReadFemPreg()

# We are only looking at live births, code 1 in outcome

live = preg[preg.outcome == 1]

#################################################
# Birth weight is coded as pounds and ounces.
# I think both are integers.
# Down with ounces. Convert to float pounds.
# I'm half tempted to convert to kilos, but that's a bridge too far.

#weight = live.birthwgt_lb * 1.0
#weight += live.birthwgt_oz / 16.0

#print(weight.tail())

# Add this column back to the live dataframe

#live['weight'] = weight
#print(live.tail())
#################################################

# Yeah, so all of that was unnecessary since there is a column
# for totalwgt_lb, the very last column of the dataframe.
# But I by God practiced.

# The birth order variable name is birthord
# We separate firstborn from the rest... very biblical, this code.

firsts = live[live.birthord == 1]
laters = live[live.birthord != 1]

# All over but the crying now.

diff_weight = firsts.totalwgt_lb.mean() - laters.totalwgt_lb.mean()
if diff_weight < 0:
    print("First babies are lighter on average by", round(abs(diff_weight), 1), "lb.")
else:
    print("First babies are heavier on average by", round(diff_weight, 1), "lb.")
first_weight_Cohen_eff = CohenEffectSize(firsts.totalwgt_lb, laters.totalwgt_lb)
print("The Cohen difference between first and later children's birth weight is")
print("  ", abs(round(first_weight_Cohen_eff, 1)), "standard deviations.")