import string

# Define a basic sentiment lexicon
positive_words = {"love", "great", "awesome", "fantastic", "good", "happy", "excited", "amazing", "best"}
negative_words = {"hate", "terrible", "awful", "bad", "angry", "upset", "disappointed", "worst"}

def clean_text(text):
"""Clean and preprocess the input text.""" text = text.lower() # Convert to lowercase
text = text.translate(str.maketrans("", "", string.punctuation)) # Remove punctuation
return text

def analyze_sentiment(text):
"""Analyze the sentiment of the given text.""" cleaned_text = clean_text(text)
words = set(cleaned_text.split()) # Convert text to a set of words

# Count the occurrences of positive and negative words positive_count = len(words & positive_words) negative_count = len(words & negative_words)

# Determine the sentiment based on word counts if positive_count > negative_count:
return "Positive"
elif negative_count > positive_count: return "Negative"
else:
return "Neutral"

# Example social media posts posts = [
"I absolutely love this new phone! It's amazing.", "This is the worst service I've ever experienced.",
 
"The weather is nice today, but I have a lot of work to do.", "Feeling great after a long workout session!"
]

# Analyze and print the sentiment of each post for post in posts:
sentiment = analyze_sentiment(post)
print(f"Post: {post}\nSentiment: {sentiment}\n")
