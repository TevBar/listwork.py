def sentiment_tally(reviews,positive_words, negative_words):
    positive_count = 0 
    negative_count = 0

    for review in reviews:
        words = review.split()
        for word in words:
            clean_word = word.strip(".,!").lower()
            if clean_word in positive_words:
                positive_count += 1
            elif clean_word in negative_words:
                negative_count += 1
    return{"positive": positive_count, "negative": negative_count}
# the code below needs to not be indented because we do not want sample code to be part of the function   
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

tally = sentiment_tally(reviews,positive_words, negative_words)
print("positive words count:",tally["positive"])
print("negative words count:", tally["negative"])