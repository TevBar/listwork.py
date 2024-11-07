def capitalize_letter(text_list, keywords):
    result = []
    for text in text_list:
        words = text.split()
        for i , word in enumerate(words):
            if word.lower() in keywords:
                words[i] = word.upper()
        result.append(' '.join(words))
    return result

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good.", "excellent.", "bad", "poor", "average."]

highlighted_reviews = capitalize_letter(reviews,keywords)
for review in highlighted_reviews:
    print(review)


            