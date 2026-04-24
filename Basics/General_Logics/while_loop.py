class Solution:
    def whileLoop(self, d: int) -> int:
        count = 0
        total = 0
        while count < 50:
            total += d + count*10
            count += 1
        return total

def main():
    x = Solution()
    result = x.whileLoop(5)
    print("Total:", result)

if __name__ == "__main__":
    main()

