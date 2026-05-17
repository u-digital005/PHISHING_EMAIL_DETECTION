import subprocess
import sys

REQUIRED_PACKAGES = {
    "pandas": "pandas",
    "sklearn": "scikit-learn",
}


def install_required_packages():
    for module_name, package_name in REQUIRED_PACKAGES.items():
        try:
            __import__(module_name)
        except ModuleNotFoundError:
            print(f"Installing {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])


install_required_packages()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "email": [
        "Click here to claim your free prize now",
        "Verify your bank account immediately or it will be closed",
        "You have won a lottery of 1 million dollars click now",
        "Your password will expire reset it now via this link",
        "Urgent your account has been compromised click to fix",
        "Meeting scheduled for tomorrow at 10am please confirm",
        "Here is the report you requested for this quarter",
        "Happy birthday hope you have a wonderful day",
        "The project deadline has been extended to next Friday",
        "Please find the attached invoice for your records",
        "Free gift cards available click the link to get yours",
        "Your loan is approved click here to claim the money",
        "Team lunch is on Wednesday let me know if you can join",
        "Reminder your subscription renews next month",
        "Congratulations you are selected click to get reward",
    ],
    "label": [
        "Phishing", "Phishing", "Phishing", "Phishing", "Phishing",
        "Safe", "Safe", "Safe", "Safe", "Safe",
        "Phishing", "Phishing", "Safe", "Safe", "Phishing",
    ]
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(df["email"], df["label"], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")
print("Confusion Matrix:")
print(cm)

print("\nTest Predictions:")
for email, actual, predicted in zip(X_test, y_test, y_pred):
    print(f"Email    : {email}")
    print(f"Actual   : {actual}")
    print(f"Predicted: {predicted}")
    print()

def check_email(email_text):
    vec = vectorizer.transform([email_text])
    result = model.predict(vec)[0]
    print(f"Result: {result}")

check_email("Click here to win a free iPhone now")
check_email("Please send me the updated project file")