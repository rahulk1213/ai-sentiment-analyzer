# ai-sentiment-analyzer
🧠 AI Sentiment Analyzer — Python Project using TextBlob
The AI Sentiment Analyzer is a Python-based natural language processing (NLP) project designed to automatically detect and classify the sentiment of text data as positive, negative, or neutral. It leverages the TextBlob library for sentiment analysis, making it simple yet powerful for beginners and intermediate Python learners.

🚀 Key Features:
● Sentiment Detection: Analyzes input text and identifies the polarity (positive, negative, neutral).

● User Input Support: Accepts custom user input for real-time sentiment prediction.

■ Clean Output: Displays sentiment polarity score and a clear sentiment label.

¤ Lightweight & Efficient: Uses minimal dependencies, ideal for small-scale projects or learning purposes.

●Technologies Used:
Language: Python

Library: TextBlob (built on top of NLTK and Pattern)

📄 How It Works:
The user enters a sentence or paragraph.

The TextBlob library processes the text to compute:

Polarity: Ranges from -1 (negative) to +1 (positive)

Subjectivity: Degree of personal opinion

Based on the polarity value, the sentiment is classified as:

Positive (polarity > 0)

Negative (polarity < 0)

Neutral (polarity = 0)

Output is displayed with the polarity score and sentiment label.

📌 Sample Output:
Input: "I love this beautiful day!"
Polarity: 0.85
Sentiment: Positive
