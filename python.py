import random

# Define the coordinates of the rectangle
A = (1, 1)
B = (5, 1)
C = (5, 5)
D = (1, 5)

# Define the number of points to generate
N = 100

# Generate the points and count how many fall into each section
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0
p6_count = 0
p7_count = 0
p8_count = 0

for i in range(N):
    x = random.uniform(A[0], C[0])
    y = random.uniform(A[1], C[1])

    if x < (A[0] + B[0]) / 2 and y > (B[1] + C[1]) / 2:
        p1_count += 1
    elif x > (A[0] + B[0]) / 2 and y > (B[1] + C[1]) / 2:
        p2_count += 1
    elif x > (A[0] + B[0]) / 2 and y < (B[1] + C[1]) / 2:
        p3_count += 1
    elif x < (A[0] + B[0]) / 2 and y < (B[1] + C[1]) / 2:
        p4_count += 1
    elif x < (D[0] + A[0]) / 2 and y > (B[1] + C[1]) / 2:
        p5_count += 1
    elif x > (D[0] + A[0]) / 2 and y > (B[1] + C[1]) / 2:
        p6_count += 1
    elif x > (D[0] + A[0]) / 2 and y < (B[1] + C[1]) / 2:
        p7_count += 1
    elif x < (D[0] + A[0]) / 2 and y < (B[1] + C[1]) / 2:
        p8_count += 1

# Calculate the probability of points in each section
p1_prob = p1_count / N * 100
p2_prob = p2_count / N * 100
p3_prob = p3_count / N * 100
p4_prob = p4_count / N * 100
p5_prob = p5_count / N * 100
p6_prob = p6_count / N * 100
p7_prob = p7_count / N * 100
p8_prob = p8_count / N * 100

# Print the results'
print("p1: {:.2f}%".format(p1_prob),",""p2: {:.2f}%".format(p2_prob),",""p3: {:.2f}%".format(p3_prob),","
      "p4: {:.2f}%".format(p4_prob),",""p5: {:.2f}%".format(p5_prob),",""p6: {:.2f}%".format(p6_prob),","
      "p7: {:.2f}%".format(p7_prob)
,",""p8: {:.2f}%".format(p8_prob))





