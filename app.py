from flask import Flask, request, render_template
import model  # Your model.py file with the functions
from model import get_sentiment_recommendations, classify_sentiment
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the homepage with the input form.
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def prediction():
    user = request.form.get('user_input')
    if not user:
        return render_template("index.html", message="Please enter a user name.")

    user = user.lower()
    items = get_sentiment_recommendations(user)

    print("DEBUG - type of items:", type(items))
    print("DEBUG - content of items:", items)

    if isinstance(items, str):
        return render_template("index.html", message=items)

    elif isinstance(items, pd.DataFrame):
        print("DEBUG - items.empty:", items.empty)
        if not items.empty:
            return render_template("index.html",
                       column_names=list(items.columns.values),
                       row_data=items.values.tolist(),
                       zip=zip,
                       user=user)
        else:
            return render_template("index.html", message="No recommendations found for this user.")


@app.route('/predictSentiment', methods=['POST'])
def predict_sentiment():
    """
    Handle free-form review and classify it as positive or negative.
    """
    review_text = request.form.get("reviewText")
    if not review_text:
        return render_template("index.html", sentiment="Please enter review text.")
    
    prediction = classify_sentiment(review_text)
    sentiment = "Positive" if prediction == 1 else "Negative"
    
    return render_template("index.html", sentiment=sentiment, review_text=review_text)


if __name__ == '__main__':
    app.run(debug=True)
