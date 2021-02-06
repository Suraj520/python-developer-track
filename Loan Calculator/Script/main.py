#stage 2:
import math
import argparse
import sys
def main():
    parser = argparse.ArgumentParser()
    #adding series of optional arguments
    parser.add_argument('--type')
    parser.add_argument('--payment')
    parser.add_argument('--periods')
    parser.add_argument('--interest')
    parser.add_argument('--principal')
    args = parser.parse_args()
    if args.type =="diff":
        if args.principal and args.periods and args.interest:
            principal = int(args.principal)
            periods = int(args.periods)
            interest= float(args.interest)
            interest = float(interest/1200)
            #calculating differential payments
            net_dp =0
            for i in range(1,periods+1):
                dp = math.ceil(principal / periods + interest * (principal - (principal * (i - 1)) / periods))
                net_dp+=dp
                print("Month {0}: payment is {1}".format(i,dp))
            overpayment = float(net_dp - principal)
            print("Overpayment = {0}".format(overpayment))
        else:
            print("Incorrect parameters.")
    elif args.type =="annuity":
        #calculate annuity payment
        if args.principal and args.periods and args.interest:
            loan_principal = int(args.principal)
            n = int(args.periods)
            loan_interest = float(args.interest)
            loan_interest = float(loan_interest/1200)
            a = math.ceil(loan_principal * (loan_interest * math.pow(1 + loan_interest, n)) / (math.pow(1 + loan_interest, n) - 1))
            overpayment = a * n - loan_principal
            print("Your annuity payment = {0}!".format(a))
            print("Overpayment = {0}".format(overpayment))
        #calculate loan principal
        elif args.payment and args.interest and args.periods :
            a = int(args.payment)
            n = int(args.periods)
            loan_interest = float(args.interest)
            loan_interest = float(loan_interest/1200)
            loan_principal = math.ceil((a)/(((loan_interest)*math.pow((1+loan_interest),n)/ (math.pow((1+loan_interest),n)-1))))
            overpayment = a*n -loan_principal
            print("Your loan principal = {0}!".format(loan_principal))
            print("Overpayment = {0}".format(overpayment))
        #calculate period
        elif args.principal and args.payment and args.interest:
            loan_principal = int(args.principal)
            monthly_payment = int(args.payment)
            loan_interest = float(args.interest)
            loan_interest = float(loan_interest/1200)
            Numerator = (monthly_payment)/(monthly_payment - loan_interest*loan_principal)
            n = (math.log(Numerator,(1+loan_interest)))
            n = math.ceil(n)
            month = math.ceil(n%12)
            year = int(n//12)
            if month ==12:
                year = year+1
                print("It will take {0} years to repay this loan!".format(year))
            else:
                print("It will take {0} years and {1} months to repay this loan!".format(year,month))
            overpayment = (monthly_payment * n) - loan_principal
            print("Overpayment = {0}".format(overpayment))
        else:
            print("Incorrect parameters.")
    else:
        print("Incorrect parameters.")


if __name__ == "__main__":
    main()
