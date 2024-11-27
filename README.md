# NBA MVP Text Predictions

## What is the project?
The goal of this project is to build a model that predicts the NBA MVP using Twitter data. Media personnel vote for MVP, making social media discussions around the voting period valuable predictors of the award.

---

## How do I plan to do the project?

1. **Collect Twitter Data**:
   - Use the Twitter API to gather tweets from February to April each year.
   - Filter tweets with relevant keywords such as "NBA" and "MVP" and include tweets from professional accounts.
   - Save tweets in a database for processing.

2. **Clean and Preprocess Data**:
   - Tokenize and preprocess text from tweets.

3. **Fine-Tune BERT**:
   - Fine-tune BERT on the preprocessed Twitter data for sentiment analysis.

4. **Named Entity Recognition (NER)**:
   - Identify how frequently players are mentioned in tweets.
   - Compute average sentiment scores for each player using sentiment analysis.

5. **Predict Top Players**:
   - Combine NER results and sentiment analysis to predict the top 5 players for MVP.

---

## Further Goals

1. Enhance predictions by pairing sentiment analysis with player statistics.
