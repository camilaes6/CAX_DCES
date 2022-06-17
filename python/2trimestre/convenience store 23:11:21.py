print("hi dear clinet, welcome to whole foods!")

product1=(input("insert the first product:"))
price1=int(input("insert the price of the product:"))

product2=(input("insert the second product:"))
price2=int(input("insert the price of the product:"))

product3=(input("insert the third product:"))
price3=int(input("insert the price of the product:"))

product4=(input("insert the fourth product:"))
price4=int(input("insert the price of the product:"))

product5=(input("insert the fifth product:"))
price5=int(input("insert the price of the product:"))

print("your order number is 60783 employee 1234 had the pleasure to attend you, if youd like an invoice enter your order number st wholefoods.com")

print("Product:", product1, "price:", price1)
print("Product:", product2, "price:", price2)
print("Product:", product3, "price:", price3)
print("Product:", product4, "price:", price4)
print("Product:", product5, "price:", price5)

subtotal= (price1+price2+price3+price4+price5)
print("Your subtotal is:", subtotal)

IVA=(subtotal*.16)
print("Your IVA is:", IVA)

total=(subtotal+IVA)
print("Your total is:", total)
print("Thank you for choosing whole foods, see you!!!")