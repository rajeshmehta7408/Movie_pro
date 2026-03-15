import joblib
import numpy as np

# Load trained model
model = joblib.load("movie_model.pkl")

def predict_movie(genre, budget, runtime):

    try:
        # convert values to integers
        genre = int(genre)
        budget = int(budget)
        runtime = int(runtime)

        # model expects 2D array
        data = np.array([[genre, budget, runtime]])

        prediction = model.predict(data)

        rating = float(prediction[0])

        if rating >= 7:
            success = "Hit Movie"
        else:
            success = "Average / Flop"

        return rating, success

    except Exception as e:
        print("Prediction Error:", e)
        return 0, "Prediction Failed"