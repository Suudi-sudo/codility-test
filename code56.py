# Calculate the size of the biggest square that can be found inside a sequence of columns of non-decreasing height.
# There are N columns made of 1x1 blocks standing next to each other. The heights of the consecutive columns form a non-decreasing sequence. The height of the K-th column (for K within the range [0..N−1]) is A[K]. What is the largest square made of blocks that can be found in the sequence?
# Write a function:
# int solution(int A[], int N);
# that, given an array A consisting of N integers, returns the side length of the largest square that can be found in A.
# Examples:
# 1. Given A = [1, 2, 2, 2, 4, 4, 5], your function should return 3. The largest square that can be found in the sequence is marked in blue in the picture below.
# Graphical representation of the first example
# 2. Given A = [1, 2, 2, 4, 5], your function should return 2.
# Graphical representation of the second example
# 3. Given A = [10, 10, 10, 10], your function should return 4.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..250,000];
# each element of array A is an integer within the range [1..100,000,000];
# elements of array A form a non-decreasing sequence.

def solution(A):
    N = len(A)
    max_square = 0

    for i in range(N):
       
        S = min(A[i], N - i)
        max_square = max(max_square, S)
    
    return max_square


print(solution([1, 2, 2, 2, 4, 4, 5]))  
print(solution([1, 2, 2, 4, 5]))        


