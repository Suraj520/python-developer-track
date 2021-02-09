# About the Project
> > This is the implementation of the Project- Loan Calculator on Python Developer Track on Github
    Link to the Project's Problem Statement: https://hyperskill.org/projects/90

Personal finances are an important part of life. Sometimes you need some extra money and decide to take a loan, or you want to buy a house using a mortgage. To make an informed decision, you need to be able to calculate different financial parameters.

This project works towards simulating a Loan Calculator for the end user which will help him in keeping a track of his personal finances. 
### Execute
```$ cd src && python main.py ```

#### About the software version
This software version is capable of calculating one of the following provided the rest are being fed as an input to it alongwith some mandatory ones.
* Differential monthly payments along with overpayment.
* Annuity payment along with overpayment.  
* Loan principal.
* Number of payments i.e Loan period in months

Mandatory Inputs
* Nominal Interest Rate.

The software operates from command line with a series of input flags like
```buildoutcfg
--type, --principal, --period , --interest
```

However, there are a few constraints regarding the aforementioned flags as per standard norms which are discussed below:
* <strong>--type </strong> indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
<pre><code class="language-no-highlight">
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
</code></pre>

* <strong>--payment </strong> is the monthly payment amount. For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid, too:
<pre><code class="language-no-highlight">
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
</code></pre>

* <strong>--principal </strong>  is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.

* <strong>--periods </strong> denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.

* <strong>--interest </strong> is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because --interest is missing:
<pre><code class="language-no-highlight">
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
</code></pre>

## Loan Calculator Session(s)
```The similar prompt can be expected upon entering the same input as described below. User can however enter any choice to validate the working of the software as long as the input is in bounds of the software```

#### Session 1: Calculating Differentiated payments

<pre><code class="language-no-highlight">
> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837
</code></pre>

#### Session 2: Calculating the Annuity payment

<pre><code class="language-no-highlight">
> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
</code></pre>

#### Session 3: Error when less than four parameters are given.
<pre><code class="language-no-highlight">
> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.
</code></pre>


#### Session 4: Calculating Loan period
<pre><code class="language-no-highlight">
> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000
</code></pre>
