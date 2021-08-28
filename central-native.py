#dataset
values = [47,95,88,73,88,84]
print('values: ' ,values )

#count
count = len(values)
print('Amount of numbers in dataset:', count)

#sum
Totalsum = sum(values)
print('Sum: ', Totalsum)

#mean
mean = Totalsum/count
print('Mean: ', round(mean, 2))

#sorthing dataset
sortedvalues= sorted(values)
index = count//2

#median
if (count%2)==0:
    #if data set is even
    median = ((sortedvalues[index-1] + sortedvalues[index +1])/2)
    print('Median: ', median)
else:
    #if data set is odd
    median= sortedvalues[index]
    print('Median: ', median)

#mode

mode = max(values, key = values.count)
print('Mode: ', mode)
