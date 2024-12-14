import numpy as np
arr1 =np.array([2, 5, 9, 5, 2])
arr2 = [2, 5, 8, 3, 1]
new_arr1 = np.unique(arr1)#去掉list中重複的element
print(new_arr1)#[2 5 9]
print(np.union1d(new_arr1, arr2))#[1 2 3 5 8 9]
print(np.intersect1d(new_arr1, arr2))#[2 5]
print(np.setdiff1d(new_arr1, arr2))#
print(arr1.sum(axis=0))