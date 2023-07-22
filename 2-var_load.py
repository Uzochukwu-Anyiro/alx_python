# file: variable_load_2.py

a = 42

if __name__ =="__main__":
    import variable 
    
    # Access the variable 'a' from the imported module
    value_of_a = variable.a 
    
    # print the value of 'a'
    print("value of 'a'", value_of_a)