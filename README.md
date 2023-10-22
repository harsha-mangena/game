# Hangman Game

## Game Objectives

The goal of the player in this game is to guess the hidden word

## Game Rules

The player has 6 guesses in order to uncover the hidden word

If after all the guesses are expended the word has not been guessed the player loses

If the word is completed within 6 guesses the player wins

In order to guess a player can either fill in each box and guess letters for those boxes.
Or the player can click the provided letter buttons.

There are also hints for players, you can fill in one letter or you can see the definition of the word. 
Each hint button is located within the left side panel.

## Game Modes

We have two main game modes, Free Play and Timed

In free play there is no time limit simply guess until you either win or lose

In Timed mode you have a ten-minute time limit to guess the word. If after ten minutes you have not guessed the word you lose

## Tech Stack

We utilized the Django Web Framework for our game as well as the Streamlit app framework for hosting and frontend.

Also utilized in our application is the random word api

`https://random-word-api.vercel.app/`

As well as the dictionary api 

`https://dictionaryapi.dev/`

These apis were used to get our random word and then get a definition of said word
## Setup

In order to set up your own hosted version of the game simply install streamlit and download the repository

Then within the game folder type 

`streamlit run app.py`

## Reflection

We began the development process by discussing our tech stack and finalized it early on. 
Then at a later date we began the development of our application. We worked incrementally
and over time a functional application was completed. We believe that our early discussions
worked quite well, we finalized design decisions quite quickly and with little disagreement.
During the time in which we were communicating clearly, and often we had little issues or 
confusion. However, later in the design process we all got quite busy with other projects 
and had a few lapses in communication which resulted in some confusion. There was work being
done more than once or being made obsolete. At one point a new repository was created which 
caused some minor confusion at certain points. This caused some issues in the design process 
as we did not communicate effectively on what was being done or was in the works. After this 
period of confusion we began more clear communication and continued on to create a functional 
application. We think that this period of communication was quite effective, and we were able 
to work out bugs and complete the application with few further issues. There were a number of 
lessons learned here such as the importance of proper communication within a team. We had a few 
issues with communication and all agree that had we communicated more clearly and more often we 
could have avoided several of the main issues that we faced. We also learned many skills relating 
to web development. While we all had some prior experience none of us are experts in web development, 
and thus we had to learn many skills within the scope of this project such as utilizing apis, 
UI/UX development, and more. This allowed us to all grow as developers and to further hone our skills 
in web development. Overall we feel that this project went reasonably well and that we created a well-made, 
functional project. While we had some minor communication issues we worked through them and were able to 
increase our skills not just as developers but as team members. These experiences will allow us to be 
significantly more effective as software developers in the future and will be greatly beneficial in 
future endeavors.  