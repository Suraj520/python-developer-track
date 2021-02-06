# About the Project
> > This is the implementation of the Project- Hangman on Python Developer Track on Github
    Link to the Project's Problem Statement: https://hyperskill.org/projects/69/

This project works towards simulating <a target="_blank" href="https://en.wikipedia.org/wiki/Hangman_(game)">The Hangman Game</a> where the computer starts the game with a random word for the user and the user has to predict the word letter by letter. 

The end outcome of the game is either a win that let's the user survive or a lose where the user will be hanged!

### Execute
```$ cd Script || python main.py ```

### Rules of the game
* This user gets 8 tries to iteratively predict the entire word or get hanged!
* If the letter that the user enters doesn't appear in the word, the computer takes away one try!
* If the letter that the user enters appear in the word, the computer reveals the letter at all positions at the word and takes away one try!

#### About the software version
* It contains a pre-defined dictionary of words which are as follows
```'python', 'java', 'kotlin', 'javascript'``` . The functionality can be extended at Line 4 of main.py to incorporate more words or use a sqlite database, if desired. 
  
* The game starts with hyphens which are equal to the number of letters, for e.g
```---- for java```
## Game Session
```The similar prompt can be expected upon entering the same input as described below. User can however enter any choice to validate the working of the software as long as the input is in bounds of the software```

<pre><code class="language-no-highlight">
# Hangman Game starts :::

H A N G M A N

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word

-a-a---i--
Input a letter: > o
You've already guessed this letter

-a-a---i--
Input a letter: > p

-a-a---ip-
Input a letter: > p
You've already guessed this letter

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > a
You've already guessed this letter

-a-a---ip-
Input a letter: > z
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > t

-a-a---ipt
Input a letter: > x
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > b
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > d
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > w
That letter doesn't appear in the word
You lost!

</code></pre>
