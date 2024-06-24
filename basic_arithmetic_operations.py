def main():
    a = float(input("a = "))
    b = float(input("b = "))
    print("a + b = ",a + b)
    print("a - b = ",a - b)
    print("a*b = ",a*b)
    if b == 0:
        print("a/b error(0 division)")
    else:
        print("a/b = ",a/b)

    
if __name__ == "__main__":
    main()
    
