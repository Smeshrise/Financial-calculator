import math

#investment=True
#bond = True

print("Choose either bond or investment:")
print("investment -to calculate the amount of interest you'll earn on interest")
print("bond -to calculate the amount you'll have to pay on a home loan")
choice = input("What is your choice:")#The program asking the user to choose between the investment or bond,after choice then it will ask the calculations of each choice to the user


if  choice == "investment":#If the user chose investment,then he will perform the calculations of investment.

    investment = int(input("Enter the amount of money you want to deposit:"))#The user ask the amount of money to be deposited.
    interest_rate= float(input(" Enter the interest rate :"))#The user ask for the interest rate.
    total_interest= interest_rate/100#The interest rate is divided by 100.
    num_years= int(input("How many years you want to invest with us?:"))#The user ask the number of years to invest.
    interest=input("Do you want  'simple or 'compound interest:")#This asking the user to choose between simple and compound interest

    if interest == "simple":#if the user chose simple,then he will use the formular at the bottom to perform the calculations.
      total_amount = (investment * (1+total_interest*num_years))#The user calculate the total amount by using the formular given for simple,if chose simple
      print(total_amount)
    elif interest == "compound":#if chose compound,the calculations will be performed,using the formular of compound interest.
        total_amount =(investment*math.pow((1+total_interest),num_years))
        total_amount = round(total_amount,2)#The user will have to round off the total amount by 2
        print(total_amount)
        

elif choice == "bond":#if the user chose bond,then he will perform,the calculations at the bottom.
    bond = int(input("Please enter the value of the bond:"))
    interest_rate = float(input("Enter the interest rate :"))
    total_interest=interest_rate/12
    num_years = int(input("Enter the number of months to repay:"))
    total_amount = (interest_rate*bond) / (1-(1+interest_rate) **(-num_years))
    total_amount = round(total_amount,2)
    print(total_amount)


