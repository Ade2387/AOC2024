with open("data.txt", "r") as file:
    list = file.readlines()

column1 = []
column2 = []

for i in list:
    column1.append(int(i.split()[0]))
    column2.append(int(i.split()[1]))

# compare the two columns starting from the smallest number in column1 with the smallest number in column2 and calculating the distance between them.

# Sort columns
column1.sort()
column2.sort()

# Calculate the similarity by adding up each number in column1 after multiplying it by the number of times that number appears in the column2.
similarity = 0
for i in range(len(column1)):
    similarity += column1[i] * column2.count(column1[i])

print(similarity)