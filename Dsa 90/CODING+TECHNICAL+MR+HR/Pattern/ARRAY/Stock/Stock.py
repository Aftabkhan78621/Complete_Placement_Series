# ============================================================
# STOCK PATTERN
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. BEST TIME TO BUY & SELL STOCK (Single Transaction)
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me hume stock ko sirf ek baar buy aur ek baar sell karna hai
taaki maximum profit mile. Rule ye hai ki buy hamesha sell se pehle hona
chahiye. Hum array ko ek baar traverse karte hain aur ab tak ka minimum
price maintain karte hain. Har naye price par dekhte hain ki agar aaj
sell kare to kitna profit milega. Agar profit current maximum se bada
hai to update kar dete hain. Ye approach sirf ek traversal me answer
de deti hai aur interview me bahut frequently puchi jati hai.
"""

def max_profit(prices):

    minimum_price = float("inf")

    maximum_profit = 0

    for price in prices:

        minimum_price = min(minimum_price, price)

        profit = price - minimum_price

        maximum_profit = max(maximum_profit, profit)

    return maximum_profit


prices = [7,1,5,3,6,4]

print("Maximum Profit :", max_profit(prices))


# Complexity
# Time  : O(n)
# Space : O(1)



# ============================================================
# 2. BEST TIME TO BUY & SELL STOCK II
# (Multiple Transactions)
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me jitni baar chahe buy aur sell kar sakte hain, lekin ek
time par sirf ek stock hold kar sakte hain. Logic simple hai, jab bhi
aaj ka price kal se bada ho to us difference ko profit me add kar do.
Isse har increasing sequence ka maximum profit automatically mil jata
hai. Is greedy approach ki wajah se sirf ek traversal me solution mil
jata hai. Service-based interviews me ye Stock Pattern ka second sabse
important question hai.
"""

def max_profit_multiple(prices):

    profit = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i-1]:

            profit += prices[i] - prices[i-1]

    return profit


prices = [7,1,5,3,6,4]

print("Maximum Profit (Multiple) :", max_profit_multiple(prices))


# ============================================================
# Expected Output
# ============================================================

# Maximum Profit :
# 5

# Maximum Profit (Multiple) :
# 7


# ============================================================
# Complexity
# ============================================================

# Single Transaction
# Time  : O(n)
# Space : O(1)

# Multiple Transactions
# Time  : O(n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Single Transaction
# Keep track of minimum buying price.

# ✔ Multiple Transactions
# Add every positive difference.

# ✔ Pattern
# Greedy + Array Traversal

# ✔ Asked In
# TCS Prime
# Infosys
# Accenture
# Capgemini
# Cognizant
# IBM
# Deloitte
# Wipro
# HCL
# Cyntexa


# ============================================================
# STOCK PATTERN COMPLETE ✅
# ============================================================