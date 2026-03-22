def rod_cutting(prices,n):
    dp=[0]*(n+1)

    for i in range(1,n+1):
      max_revenue=0
      for j in range(1,i+1):
         current=prices[j-1]+dp[i-j]
         if current>max_revenue:
            max_revenue=current
      dp[i]=max_revenue
    return dp[n]       
  
# Test cases
if __name__ == "__main__":
    # Test case 1
    prices1 = [1, 5, 8, 9, 10, 17, 17, 20]
    n1 = 4
    print(f"Test 1 - Rod length: {n1}")
    print(f"Prices: {prices1}")
    print(f"Maximum revenue: {rod_cutting(prices1, n1)}")
    print(f"Expected: 10 (cut into 2+2)")
    print()
    
    # Test case 2
    prices2 = [3, 5, 8, 9, 10, 17, 17, 20]
    n2 = 8
    print(f"Test 2 - Rod length: {n2}")
    print(f"Prices: {prices2}")
    print(f"Maximum revenue: {rod_cutting(prices2, n2)}")
    print(f"Expected: 22")
    print()
    
    # Test case 3
    prices3 = [1, 5, 8, 9]
    n3 = 1
    print(f"Test 3 - Rod length: {n3}")
    print(f"Prices: {prices3}")
    print(f"Maximum revenue: {rod_cutting(prices3, n3)}")
    print(f"Expected: 1")  