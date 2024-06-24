def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
def lcm(a, b):
    return abs(a * b) / gcd(a, b)

def pow(a, b):
    return a**b

def 
     
def basic_arithmetic(a, b):
    print("a + b = ",a + b)
    print("a - b = ",a - b)
    print("a * b = ",a * b)
    if b == 0:
        print("a/b error(0 division)")
    else:
        print("a / b = ",a / b)
   
def main():
    a = float(input("a = "))
    b = float(input("b = "))
    basic_arithmetic(a, b)
    print("gcd(a, b) = ",gcd(a, b))
    print("lcm(a, b) = ",lcm(a, b))
    print("aのb乗",pow(a, b))
    
if __name__ == "__main__":
    main()
    
