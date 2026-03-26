import customer
import admin

print('Welcome to Shop Project')
print("Who are you?")
print("1. Customer")
print("2. Admin")
ans=input("Your answer:").lower()
if ans=='1' or ans=='customer':
    customer.run()
elif ans=='2' or ans=='admin':
    admin.run()
else:
    print('Invalid Answer!')