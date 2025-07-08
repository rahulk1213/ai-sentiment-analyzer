from textblob import TextBlob

def analyze_sentiment():
    print("----- AI Sentiment Analyzer -----\n")
    text = input("Enter your text: ")

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    print("\n🔍 Sentiment Polarity Score:", polarity)

    if polarity > 0:
        print("🙂 Positive Sentiment")
    elif polarity < 0:
        print("☹️ Negative Sentiment")
    else:
        print("😐 Neutral Sentiment")

if __name__ == "__main__":
    analyze_sentiment()
