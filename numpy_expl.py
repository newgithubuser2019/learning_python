import sys

import numpy as np

# ---------------------------------------------------------------Creating Simple One-Dimensional NumPy Arrays--------------------
# create a one-dimensional NumPy array
arr = np.arange(10, 110, 10)
print(arr)

# create the same NumPy array using a Python range and a list
arr = np.array([i for i in range(10, 110, 10)])

# create a ten-element NumPy array object of all zeros
arr = np.zeros(10)
print(arr.dtype)

arr = np.ones(10)

# ten-element array of random integers between 1 and 5 (inclusive)
arr = np.random.randint(1, 6, 10)
print(arr)

# How can you create a normal distribution of 10 numbers, centered on 5?
# Note, the 1 in center represents mu, size of STD DEV
arr = np.random.normal(5, 1, 10)
print(arr)

# create an array of 10 random numbers between zero and one
arr = np.random.rand(10)
print(arr)

# -----------------------------------------------------------Creating and Using Multidimensional Arrays--------------------------------
arr = np.arange(1, 13)
print(arr)
newarr = arr.reshape(3, 4)
print(newarr)
print(newarr[0, 0])

# create a two-dimensional, 3 x 4 array (three arrays of four elements each)
values = np.random.randint(1, 11, (3, 4))
print(values)

zeros = np.zeros(dtype=np.int64, shape=(3, 4))
print(zeros)

z_list = [z for z in range(0, 5)]
y_list = [z_list for y in range(0, 4)]
x_list = [y_list for x in range(0, 3)]
x_array = np.array(x_list)
print(x_list)
print(x_array)

# ----------------------------------------------------------Vectorized Operations-------------------------------------------------------
print("\n")
one_dim = np.arange(1, 6)
print(one_dim)
# print(one_dim * 2)
arr = np.arange(5, 0, -1)
print(arr)
new_arr = one_dim + arr
print(new_arr)
print(one_dim > 2)
print((one_dim > 4) | (one_dim == 1))
arr = (one_dim > 4) | (one_dim == 1)
print(arr)
arr = -(one_dim[3:])
print(arr)
print(np.absolute(arr))
arr = one_dim.sum()
print(arr)

# -----------------------------------------------------------Working with Files---------------------------------------------------------
people = np.array(["John", "Jennifer", "Helen", "Miryam"])
languages = np.array([2, 2, 1, 1])
np.savez("data.npz", people=people, languages=languages)

arrays = np.load("data.npz")
people2 = arrays["people"]
languages2 = arrays["languages"]
print(people2)
print(languages2)

arr = np.arange(1, 13).reshape(3, 4)
np.savetxt("myarray.csv", arr, delimiter=",")

arr2 = np.loadtxt("myarray.csv", delimiter=",")
print(arr2)

# --------------------------------------------------------NumPy String Functions-----------------------------------
lumberjack = np.array("I'm a lumberjack and I'm OK I sleep all night and I work all day".split(" "))
print(lumberjack)
search_results, = np.where(np.char.str_len(lumberjack) >= 5)
print(search_results)
print(lumberjack[search_results])
