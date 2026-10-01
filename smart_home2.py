   
'''
    task: convert c to f
    name: c_to_f
    input: degrees_c
    side effects: none
    return: degrees_f
    '''

def c_to_f(degrees_c):

    degrees_f = (degrees_c * 9/5 + 32)
    return degrees_f

    '''
    task: tell user current temp
    name: prtint_temp
    input: temp_in_f
    side effects: "The tempature is: x"
    return: none
    '''

def print_temp(temp_in_f):
    print("The tempature is: ", temp_in_f)
    return None

def main():
    temp_in_c = input("what is temp in C") # ask for temp in c
    f_degrees = c_to_f(temp_in_c) # converts it to f
    print_temp(f_degrees) # calls the fn to tell the user the temp


def c_to_f(degrees_c):
    # assignment statment
    #stuff on the right has to be evaluated first
    #variable on the left hand side holds the value
    degrees_f = (degrees_c * 9/5) + 32
    return degrees_f


name = sam #data type text
age = 25 # int data type - whole real number
pi = 3.1415 # floats data type - number with decimal
# boolean data types
is_hungry = True
is_thirsty = False


# defining a function 
def display_temp(degrees):
    '''
    task- tell user current temp
    imput - current temp in F
    side effects - prints message w/ temp
    return - none
    '''
    print("The current temp is: ", degrees)
    return None

# running a function is also callign a function 
# name of the function + parenthasis
display_temp(0)
display_temp(056)
display_temp("40")