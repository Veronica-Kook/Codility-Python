'''

5. PermMissingElem

A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

'''

# (1) Find the Missing Element

def solution(A):
    # write your code in Python 3.6
    lst = [False] * (len(A)+1)
    
    for i in range(len(A)):
        if A[i]:
            lst[A[i]-1] = True
    print("List : ", lst)
    
    for i in range(len(lst)):
        if lst[i] == False:
            print("Answer : ", i+1)
            print()
            return i+1


# (2) Testing Program

if __name__ == '__main__':
    
    solution([2,3,1,5]) 
    solution([1,5,7,6,4,3,9,2])
    solution([2,3,4,5,6,7,8])
    
    '''
    List :  [True, True, True, False, True]
    Answer :  4

    List :  [True, True, True, True, True, True, True, False, True]
    Answer :  8

    List :  [False, True, True, True, True, True, True, True]
    Answer :  1
    '''