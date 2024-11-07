def create_summary(review, length = 30):
    if len(review) <= length: 
        return review
    end_index = review.rfind(" ", 0, length)
    if end_index == -1:
        end_index = length 
    summary = review[:end_index] + "..."
    return summary

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

summaries = [create_summary(review) for review in reviews]
for summary in summaries:
    print(summary)