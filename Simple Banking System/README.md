# About the Project
> > This is the implementation of the Project- Simple Banking System on Python Developer Track on Github
    Link to the Project's Problem Statement: https://hyperskill.org/projects/109

Everything goes digital these days, and so does money. Today, most people have credit cards, which save us time, energy and nerves. From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways.
This project works towards simulating a Simple Banking System with a database to create a credit card, transfer funds and other basic operations.

### Execute
```$ cd Script || python main.py ```

#### About the software version
Assuming that the user is aware about the anatomy of <a href="https://www.creditcardinsider.com/learn/anatomy-of-a-credit-card/#:~:text=Visa%20cards%20%E2%80%93%20Begin%20with%20a,6%20and%20have%2016%20digits"> credit cards </a>.
This software version greets the user with a welcome prompt where he is expected to perform one of the following actions
<pre><code class="language-no-highlight">
1. Create an account
2. Log into account
0. Exit
</code></pre>

###### Operation for new users
* If the user is new to the bank then supposedly he is invited to create an account by the bank/branch manager. Upon choosing the option 1, The software assigns user a credit card number and a pin using <a href="https://en.wikipedia.org/wiki/Luhn_algorithm "> Luhn Algorithm </a> which gets appended to the customer database(sqlite, here) of the bank.


* If the user is a customer to the bank then he will press the second option of logging into the account after which the simple banking system validates the card number and pin entered by the user with existing credentials in the sqlite database and upon successful authentication grants the user rights to perform the following activities:
    * Check balance.
    * Add money to the account.
    * Transfer money to an existing user in the bank.
    * Close account.
    * Logout

## Loan Calculator Session(s)
```The similar prompt can be expected upon entering the same input as described below. User can however enter any choice to validate the working of the software as long as the input is in bounds of the software```

#### Session 1

<pre><code class="language-no-highlight">
1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000009455296122
Your card PIN:
1961

1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000003305160034
Your card PIN:
5639

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000009455296122
Enter your PIN:
>1961

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>2

Enter income:
>10000
Income was added!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 10000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160035
Probably you made a mistake in the card number. Please try again!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305061034
Such a card does not exist.

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>15000
Not enough money!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>5000
Success!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 5000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

>0
Bye!
</code></pre>

#### Session 2

<pre><code class="language-no-highlight">1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000007916053702
Your card PIN:
6263

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000007916053702
Enter your PIN:
>6263

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>4

The account has been closed!

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000007916053702
Enter your PIN:
>6263

Wrong card number or PIN!

1. Create an account
2. Log into account
0. Exit
>0

Bye!
</code></pre>

