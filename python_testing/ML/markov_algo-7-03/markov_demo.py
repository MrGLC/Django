import random

def create_markov_model(sentences):
    ngram_freq = {}
    for sentence in sentences:
        for i in range(len(sentence)-1):
            word, next_word = sentence[i], sentence[i+1]
            if word not in ngram_freq:
                ngram_freq[word] = {}
            ngram_freq[word][next_word] = ngram_freq[word].get(next_word, 0) + 1
    return ngram_freq

def predict_next_word(ngram_freq, start_word):
    if start_word in ngram_freq:
        next_words = list(ngram_freq[start_word].keys())
        weights = list(ngram_freq[start_word].values()) # Weights for choosing the next word
        return random.choices(next_words, weights=weights)[0]
    else:
        return None

def main():
    sentences = [
        ["Hello,", "how", "are", "you", "today", "?"],
        # Add more sentences as needed
    ]
    model = create_markov_model(sentences)
    start_word = "Hello,"
    next_word = predict_next_word(model, start_word)
    print(f"Next word after '{start_word}' is: {next_word}")

if __name__ == "__main__":
    main()

