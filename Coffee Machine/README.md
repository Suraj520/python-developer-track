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

#### Pricing and Ingredients for brewing various coffee variants
  The Coffee machine serves three primary variants to the user commonly known as Espresso, Latte and Capuccino.
  Each of the variants of coffee require the following amount of ingredients for brewing one cup charged as per the corresponding amount:
    - Espresso: 250 ml of water and 16 g of coffee beans. Cost: $4.
    - Latte: 350 ml of water, 75 ml of milk and 20 g of coffee beans. Cost: $7.
    - Espresso: 200 ml of water, 100 ml of milk and 12 g of coffee. Cost: $6.

- Once the user enters the desired option mapped to one of the aforementioned actions, The coffee machine further invokes a series of nested actions through user prompt to complete it.
 The nested operations are described below
    - If the user enters buy coffee in the prompt
