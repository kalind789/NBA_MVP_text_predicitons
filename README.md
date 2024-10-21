# NBA_MVP_text_predicitons

## What is the project?
In this project I want to build a model that is able to predict the NBA's MVP using articles. The people who vote for MVP are media personnel. This means that the articles written around the time of the MVP voting should be a good prediction of who will win the MVP. 

## How do I plan to do the project?
- Web scrape articles from BleacherReport, ESPN, and other similar outlets.
- Clean and tokenize data.
- FineTune BERT on the data.
- Use Named Entity Recognition to see how frequently a player in mentioned.
- Use Named Entity Recognition to get the average sentiment for that player.
- Use the prev two steps in order to predict top 5 players.

## Further Goals
- Pair the sentiment analysis with player stats to get even better predictions.
- Use twitter data to see what is being said on these apps as they are very relavent as well.
  
