#dataset
values = [47,95,88,73,88,84]
print('values: ' ,values )

import statistics

#count
count = len(values)
print('Amount of numbers in dataset:', count)

#sum
Totalsum = sum(values)
print('Sum: ', Totalsum)

#mean
mean = statistics.mean(values)
print('Mean: ', round(mean, 2))

#median
median = statistics.median(values)
print('Median: ', median)

#mode

mode = statistics.mode(values)
print('Mode: ', mode)

