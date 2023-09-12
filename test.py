import numpy as np
import pytest
import math

x = np.zeros((3,3))
print(x)

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(AttributeError):
        capital_case(9)

        
test_raises_exception_on_non_string_arguments()
test_capital_case()

class pairs:
    def __init__(self, w,h):
        self.w = w
        self.h = h


if __name__ == "__main__":
    
    
    A = [1,3,15,11,2]
    B = [23,127,235,19,8]
    
    A = np.array(A).reshape(-1, 1)
    B = np.array(B).reshape(1, -1)
    
    C = np.abs(A-B)
    print(C)
    
    # Get the flat index of the minimum value
    min_index_flat = np.argmin(C)

    # Convert the flat index to 2D index
    min_index_2d = np.unravel_index(min_index_flat, C.shape)
    print(min_index_2d)
    print(A[min_index_2d[0],0],B[0,min_index_2d[1]])
    
    # A = sorted(A)
    # B = sorted(B)

    # min_diff = 1e9
    # a_v = -1
    # b_v = -1
    
    # A_index = 0
    # B_index = 0
    # while A_index < len(A) and B_index< len(B):
    #     diff = np.abs(A[A_index]-B[B_index])
    #     print(A[A_index],B[B_index],diff)
    #     if diff < min_diff:
    #         min_diff = diff 
    #         a_v = A[A_index]
    #         b_v = B[B_index]
    #         print("here")
    #     if A[A_index] < B[B_index]:
    #         A_index+=1
    #     else:
    #         B_index+=1
            
    # while A_index < len(A):
    #     B_index -= 1
    #     diff = np.abs(A[A_index]-B[B_index])
    #     print(A[A_index],B[B_index],diff)
    #     if diff < min_diff:
    #         min_diff = diff 
    #         a_v = A[A_index]
    #         b_v = B[B_index]
    #         print("here")
    #     A_index+=1
        
    # while B_index < len(B):
    #     A_index -=1
    #     diff = np.abs(A[A_index]-B[B_index])
    #     print(A[A_index],B[B_index],diff)
    #     if diff < min_diff:
    #         min_diff = diff 
    #         a_v = A[A_index]
    #         b_v = B[B_index]
    #         print("here")
    #     B_index+=1
        
    # diff = np.abs(A[A_index]-B[B_index])
    # print(A[A_index],B[B_index],diff)
    # if diff < min_diff:
    #     min_diff = diff 
    #     a_v = A[A_index]
    #     b_v = B[B_index]
    #     print("here")

        
    # print(min_diff, a_v, b_v)
            
    
    # X = np.random.rand(4,4)-.5
    

    
    # print(X)

    
    # max_sum = X[0,0]
    # i_save = 0
    # j_save = 1
    # k_save = 0 
    # l_save = 1
    
    # partial = np.zeros((5,5))
    
    # for i in range(5):
    #     for j in range(5):
    #         partial[i,j] = X[:i,:j].sum()
    # print(partial)
    # max_partial = -1
    # for i in range(4):
    #     for j in range(4):
    #         for k in range(i+1,5):
    #             for l in range(j+1, 5):  
    #                 partial_score = partial[k,l] + partial[i,j] - partial[i,l] - partial[k,j]
    #                 print(i,j,k,l,partial_score)
    #                 if partial_score > max_partial:
    #                     print(partial[k,l], partial[i,j] , partial[i,l],partial[k,j])
    #                     max_partial = partial_score
    
    # print("MP:", max_partial)

    
    
    # for i in range(4):
    #     for j in range(i+1,5):
    #         for k in range(4):
    #             for l in range(k+1, 5):           
    #                 selected_sum = X[i:j,k:l].sum()
    #                 if selected_sum > max_sum:
    #                     max_sum = selected_sum
    #                     i_save = i
    #                     j_save = j
    #                     k_save = k
    #                     l_save = l
    # print(max_sum)
    # print(i_save,j_save,k_save,l_save)
    
    
    
    
    
    # all_pairs = [pairs(65,100),pairs(70,150),pairs(56,90),pairs(75,190),pairs(60,95),pairs(68,33)]
    # lenpairs = len(all_pairs)
    # print(all_pairs)

    # sorted_list = sorted(all_pairs, key=lambda x: -x.w)
    
    # best_ix = []
    # best_indices = []
    
    # for ix, elem in enumerate(sorted_list):
    #     best_score = 0
    #     best_index = -1
    #     for j in range(ix):
    #         if elem.h < sorted_list[j].h:
    #             best_score = max(best_ix[j], best_score)
    #             best_index = j
    #     best_ix.append(best_score+1)
    #     best_indices.append(best_index)

    

    # print(best_ix)
    # print(best_indices)
    
    # # Find the maximum element
    # max_value = max(best_ix)

    # # Find the index of the maximum element
    # max_index = best_ix.index(max_value)
    
    # print(max_index)
    
    # while True:
    #     print (max_index, sorted_list[max_index].h, sorted_list[max_index].w)
    #     max_index = best_indices[max_index]
    #     if max_index == -1:
    #         break