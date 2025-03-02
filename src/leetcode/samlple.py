import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from domain.CustomerInfo import CustomerInfo

if __name__ == "__main__":
    aaa = "1 2 3 4 5"
    kkk = aaa.split()
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"nums: {nums}")
    print(f"nums: {kkk}")
    c1 = CustomerInfo("Tom", 20,100)
    print(c1)
    c1.setScore(99)
    print(c1.getScore())