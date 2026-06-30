"""
write a function called discount_price
that takes original_price and discount_percent as parameters
and prints the final price after discount

"""

def discount_prize(original_price, discount_percent):
    
    discount = ((discount_percent/100)*original_price)
    final_prize = original_price - discount
    print(f"the final prize after applying {discount_percent}% of discount: {final_prize}")
o1 = int(input("Enter Original Prize: "))
dp = int(input("Enter the percentage of discount given: "))
discount_prize(o1, dp)