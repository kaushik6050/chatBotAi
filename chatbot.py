import random

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources (only first time)
nltk.download('punkt')

greetings = ["hi", "hello", "hey", "good morning", "good evening"]
responses = ["Hello there!", "Hi, how can I help you?", "Hey! What’s up?"]

qa_pairs = {
    "what is your name": "I’m PyBot — your friendly AI assistant.",
    "how are you": "I’m just code, but I’m feeling great today!",
    "what can you do": "I can chat with you and answer simple questions.",
    "bye": "Goodbye! Have a nice day!"
}


def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in greetings:
        return random.choice(responses)
    for question, answer in qa_pairs.items():
        if question in user_input:
            return answer

    all_sentences = list(qa_pairs.keys()) + [user_input]
    vectorizer = CountVectorizer().fit_transform(all_sentences)
    similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])
    idx = similarity.argmax()

    if similarity[0, idx] > 0.3:
        return list(qa_pairs.values())[idx]
    else:
        return "I’m not sure about that. Could you rephrase?"


print("🤖 PyBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("🤖 PyBot:", qa_pairs["bye"])
        break
    print("🤖 PyBot:", chatbot_response(user_input))
