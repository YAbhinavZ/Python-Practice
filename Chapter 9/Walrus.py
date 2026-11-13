 

# Walrus Operator

if(n:=len([1,2,3,4]) ) > 3:
    print(f"List is too long ({n}) elements")

# Type definition
n : int = 5
name : str  = "Harry"

def sum(a : int ,b : int) -> int:
    return a+b
