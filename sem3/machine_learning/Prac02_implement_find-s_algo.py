# concept learning / two way classification / binary classification
import csv
num_attribute = 6
a = []

print('\n The Given Training Dataset \n')
with open('data\\enjoysport.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        if count == 0:
            print(row)
            count = +1
        else:
            a.append(row)
            print(row)
            count += 1

print('\n The initial value of hypothesis:')
hypothesis = ['0'] * num_attribute
print(hypothesis)

for j in range(0, num_attribute):
    hypothesis[j] = a[0][j]
    print(hypothesis)

print('\n Find S: Finding  a maximally specific hypothesis\n')
for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]
                print(' For Training Example No : {0} the hpothesis is '.format(
                    i), hypothesis)


print('\n The Maximally specific hypothesis for a given training example: \n')
print(hypothesis)
print('\n')
