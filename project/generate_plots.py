import pandas as pd
import matplotlib.pyplot as plt

# Data for the plots
model_scores = {
    "model": ["initial", "add_features", "hpo"],
    "score": [0.123, 0.456, 0.789]  # Replace with actual scores
}

kaggle_scores = {
    "submission": ["initial", "add_features", "hpo"],
    "score": [0.123, 0.456, 0.789]  # Replace with actual Kaggle scores
}

# Create DataFrame
df_model_scores = pd.DataFrame(model_scores)
df_kaggle_scores = pd.DataFrame(kaggle_scores)

# Plot model scores
plt.figure(figsize=(8, 6))
plt.plot(df_model_scores["model"], df_model_scores["score"], marker='o')
plt.title("Top Model Scores")
plt.xlabel("Model")
plt.ylabel("Score")
plt.savefig('img/model_train_score.png')
plt.show()

# Plot Kaggle scores
plt.figure(figsize=(8, 6))
plt.plot(df_kaggle_scores["submission"], df_kaggle_scores["score"], marker='o')
plt.title("Top Kaggle Scores")
plt.xlabel("Submission")
plt.ylabel("Score")
plt.savefig('img/model_test_score.png')
plt.show()