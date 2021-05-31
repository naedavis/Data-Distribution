import numpy
from scipy import stats
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
my_mean = numpy.mean(test_scores)
print("the mean is: ", my_mean)
my_median=numpy.median(test_scores)
print("The median is ", my_median)
my_mode = stats.mode(test_scores)
print("The mode is ", my_mode)
my_range=numpy.ptp(test_scores)  #ptp for range
print("The range is ", my_range)

import matplotlib.pyplot as plt
cities=['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall= [140,  200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)] #labels on the x-axis
#labeling and visuals
plt.bar(x_pos, rainfall, color='green')
plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)
plt.show()