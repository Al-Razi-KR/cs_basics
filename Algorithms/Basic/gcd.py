# Find the greatest common denominater of two numbers using Euclid's algorithm

def gcd1(a, b):
    lowest = min(a,b)
    while lowest != 0:
        if a%lowest == 0 and b%lowest == 0:
            return lowest
        else:
            lowest -= 1

def gcd(a, b):
    while b != 0:
        t, a = a, b
        b = t % b
    return a
    

def test_samplets():
    print(f"Answer: 12; Result: {gcd(60, 96)}") # should return 12
    print(f"Answer: 21; Result: {gcd(21, 42)}") # should return 21
    print(f"Answer: 4; Result: {gcd(12, 20)}") # should return 4
    print(f"Answer: 4; Result: {gcd(20, 8)}") # should return 4

def main():
    test_samplets()

if __name__ == "__main__":
    main()