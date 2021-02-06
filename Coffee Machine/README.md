# About the Project
> > This is the implementation of the Project- Coffee Machine on Python Developer Track on Github
    Link to the Project's Problem Statement: https://hyperskill.org/projects/68/

This project works towards simulating the software of a coffee machine which primarily runs on the following ingredients and can be used to track the money:
* Milk
* Water
* Disposable cups
* Coffee beans

### Execute
```$ python main.py ```

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
Once the user enters the desired option mapped to one of the aforementioned actions, The coffee machine further invokes a series of nested actions through user prompt to complete it.
- The nested operations are described below 
  * If the user enters buy coffee in the prompt, then a prompt appears waiting for user to enter the variant of coffee to be brewed i.e
    - Espresso.
    - Latte.
    - Cappucino.
  Depending upon the choice made, the coffee machine brews the coffee variant for the user and displays the one of the following prompt depending upon the amount of ingredients in stock inside the machine.
      ``` I have enough resources, making you a coffee!```
      or ```Sorry, not enough {Ingredient Name}! :: Where Ingredient can be water, coffee, disposable cup or milk```
