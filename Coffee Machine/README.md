# About the Project
> > This is the implementation of the Project- Coffee Machine on Python Developer Track on Github
    Link to the Project's Problem Statement: https://hyperskill.org/projects/68/

This project works towards simulating the software of a coffee machine which primarily runs on the following ingredients and can be used to track the money:
* Milk
* Water
* Disposable cups
* Coffee beans

### Execute
```$ cd Script || python main.py ```

### About the Software
The coffee machine will have limited amount of water, milk, coffee beans and disposable cups along with a logic to track the amount of money earned.
The coffee machine allows user to perform one of the following actions upon rebooting or in a new session: 
* Buy coffee
* Fill the ingredients
* Take the money
* Check Remaining

The software gets initialized with a limited amount of ingredients everytime it is called. One can add sql database to store the previous state,if desired. 

#### Pricing and Ingredients for brewing various coffee variants
The Coffee machine serves three primary variants to the user commonly known as Espresso, Latte and Capuccino.
Each of the variants of coffee require the following amount of ingredients for brewing one cup charged as per the corresponding amount:
* Espresso: 250 ml of water and 16 g of coffee beans. Cost: $4.
* Latte: 350 ml of water, 75 ml of milk and 20 g of coffee beans. Cost: $7. 
* Espresso: 200 ml of water, 100 ml of milk and 12 g of coffee. Cost: $6.

##### Nested actions corresponding to each action of the user
Once the user enters the desired option mapped to one of the aforementioned actions, The coffee machine further invokes a series of nested actions through user prompt to complete it.<br><br>
The nested operations are described below 
If the user enters buy coffee in the prompt, then a prompt appears waiting for user to enter the variant of coffee to be brewed i.e 
<ul>
<li>Espresso</li>
<li>Latte</li>
<li>Cappucino</li>
</ul>

> Depending upon the choice made, the coffee machine brews the coffee variant for the user and displays the one of the following prompt depending upon the amount of ingredients in stock inside the machine.
      
``` I have enough resources, making you a coffee!```
<br>or ```Sorry, not enough {Ingredient Name}! :: Where Ingredient can be water, coffee, disposable cup or milk```
<p>If the coffee machine doesn't have enough ingredients then the <strong> user can either check for the remaining ingredients using the remaining action and brew an according variant or inform the shopkeeper to fill it with the ingredients which is done by fill action of the coffee machine </strong> </p>

If the shopkeeper enters the <strong>fill button </strong> then he is prompte to enter the quantity of each ingredient iteratively that he wishes to update as shown below.
<ul>
<li>Write how many ml of water do you want to add:</li>
<li>Write how many ml of milk do you want to add:</li>
<li>Write how many grams of coffee beans do you want to add:</li>
<li>Write how many disposable cups of coffee do you want to add:</li>
</ul>

If the shopkeeper desires to take out the money, he will enter the <strong>take button </strong> from the main prompt and collect the money, thus resetting the amount of money to 0

If the shopkeeper is closing the shop then he can enter the <strong>exit button </strong> and shutdown the coffee machine.

## Coffee Machine Session
```The similar prompt can be expected upon entering the same input as described below. User can however enter any choice to validate the working of the software as long as the input is in bounds of the software```

<pre><code class="language-no-highlight">
# Cofee Machine Boots up :::

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
> fill

Write how many ml of water do you want to add:
> 1000
Write how many ml of milk do you want to add:
> 0
Write how many grams of coffee beans do you want to add:
> 0
Write how many disposable cups of coffee do you want to add:
> 0

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
> take

I gave you $564

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit):
> exit
</code></pre>
