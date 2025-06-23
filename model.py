import pandas as pd
import numpy as np
import pickle
import os
# Load all required data and models from the 'pickle' directory
root_path = os.path.join("pickle", "")

user_final_rating = pickle.load(open(os.path.join(root_path, "user_final_rating.pkl"), "rb"))
prod_reviews_final_data = pickle.load(open(os.path.join(root_path, "prod_reviews_final_data.pkl"), "rb"))
tfidf_vectorizer = pickle.load(open(os.path.join(root_path, "tfidf_vectorizer.pkl"), "rb"))
logreg = pickle.load(open(os.path.join(root_path, "final_model.pkl"), "rb"))

def get_sentiment_recommendations(user):
    
    if user in user_final_rating.index:
        recommendations = list(user_final_rating.loc[user].sort_values(ascending=False)[:20].index)
        temp = prod_reviews_final_data[prod_reviews_final_data['id'].isin(recommendations)].copy()
        X = tfidf_vectorizer.transform(temp["text_reviews_combined"].astype(str))
        temp["predicted_sentiment"] = logreg.predict(X)
        temp = temp[["name", "predicted_sentiment"]]
        temp_grouped = temp.groupby("name", as_index=False).count()
        temp_grouped["pos_review_count"] = temp_grouped["name"].apply(
            lambda x: temp[(temp["name"] == x) & (temp["predicted_sentiment"] == 1)]["predicted_sentiment"].count()
        )
        temp_grouped["total_review_count"] = temp_grouped["predicted_sentiment"]
        temp_grouped["pos_sentiment_percent"] = np.round(
            temp_grouped["pos_review_count"] / temp_grouped["total_review_count"] * 100, 2
        )
        temp_grouped.columns = ['ProductName', 'ProductReviewPredictedSentiment', 'NumberOfPositiveReviews', 'TotalNumberOfReviews', 'PercentageofPositiveReviews']
        return temp_grouped.sort_values("PercentageofPositiveReviews", ascending=False)[:5]
    else:
        return f"User name '{user}' doesn't exist."

#"""function to classify the sentiment to 1/0 - positive or negative - using the trained ML model"""

def classify_sentiment(review_text):
    """
    Classify free-form review text as positive (1) or negative (0).
    
    Args:
        review_text (str): User-submitted review

    Returns:
        int: 0 for negative, 1 for positive
    """
    review_text = review_text.lower().strip()
    X = tfidf_vectorizer.transform([review_text])
    y_pred = logreg.predict(X)
    return int(y_pred[0])
