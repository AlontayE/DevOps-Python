#This is a program that prints out only odd numbers
count=0
while count < 100:
    if count % 2==0:
        count +=1
        continue
    print(f"We are counting odd numbers:{count}")
    count +=1
