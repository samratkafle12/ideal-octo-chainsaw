import numpy as np


# to validate the list if it caonts 9 elements or not
def validate_list(list):
    if (len(list) != 9 ):
        raise ValueError("List must contain nine numbers.")
    
    return list
while True:
 try:
    list1 = list(map(int,input("Enter the elements: ").split()))
    # valid the list length
    vld_list = validate_list(list1)

    # if the input is valid break the loop
    break
    
 except ValueError as e:
    print(e)
    print("please try again: ")

# print("\n\n'validated List'",vld_list)
# print("\n")
# converting the list into array
my_array = np.array(list1)

# my_array = [0,1,2,3,4,5,6,7,8]
# reshapping it into 3*3 matrix form
matrix = np.array(my_array).reshape(3,3)
    # main function to calculate the requrements

def calculate(my_array):

    # for mean value
    mean_ax1 = np.mean(my_array,axis=0).tolist()
    mean_ax2 = np.mean(my_array,axis = 1).tolist()
    mean_flat = np.mean(my_array).tolist()

    #for variance
    var_ax1 = np.var(my_array,axis=0).tolist()
    var_ax2 = np.var(my_array,axis=1).tolist() 
    var_flat = np.var(my_array).tolist()

    # for standard deviation
    std_ax1 = np.std(my_array,axis=0).tolist()
    std_ax2 = np.std(my_array,axis=1).tolist()
    std_flat = np.std(my_array).tolist()

    # for maximum
    max_ax1 = np.max(my_array,axis=0).tolist()
    max_ax2 = np.max(my_array,axis=1).tolist()
    max_flat = np.max(my_array).tolist()

    # for minimum

    min_ax1 = np.min(my_array,axis=0).tolist()
    min_ax2 = np.min(my_array,axis=1).tolist()
    min_flat = np.min(my_array).tolist()

    #  for sum
    sum_ax1 = np.sum(my_array,axis=0).tolist()
    sum_ax2 = np.sum(my_array,axis=1).tolist()
    sum_flat = np.sum(my_array).tolist()

    # creating the dictionary of the results of mean,variance, std, max , min and sum

    result = {
        'mean':[mean_ax1,mean_ax2,mean_flat],
        'variance':[var_ax1,var_ax2,var_flat],
        'standard deviation':[std_ax1,std_ax2,std_flat],
        'max': [max_ax1,max_ax2,max_flat],
        'min':[min_ax1,min_ax2,min_flat],
        'sum':[sum_ax1,sum_ax2,sum_flat]
    }

    return result







result = calculate(matrix)
print(result)
