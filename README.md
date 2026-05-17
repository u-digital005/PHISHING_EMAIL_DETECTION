# PHISHING_EMAIL_DETECTION
# Phishing Email Detection Model

## What is Phishing?
Phishing emails are fake emails that try to trick you into clicking bad links or giving away personal information. For example, an email saying *"You won a lottery! Click here!"* is a phishing email.

---

## What Does This Project Do?
This project builds a machine learning model that reads an email and decides whether it is **Phishing** or **Safe**. It is like teaching a computer to smell something suspicious in an email.

---

## How Does It Work?

**Step 1 - Give it data**
We give the model a list of emails. Some are phishing, some are safe. Each email has a label telling the model what it is.

**Step 2 - Convert text to numbers**
Computers cannot read words directly. So we use a tool called **TF-IDF** which converts words into numbers based on how important they are in the email.

**Step 3 - Train the model**
We use a simple algorithm called **Naive Bayes**. It learns patterns from the training emails. For example, it notices that words like *"click", "free", "win", "urgent"* usually appear in phishing emails.

**Step 4 - Test the model**
We give it new emails it has never seen before. It predicts whether each one is Phishing or Safe.

**Step 5 - Check accuracy**
We compare its predictions to the correct answers and calculate how often it was right. We also show a **confusion matrix** which tells us exactly how many emails it got right or wrong.

---

## Key Terms Explained Simply

| Term | Simple Meaning |
|---|---|
| TF-IDF | Gives importance score to each word in the email |
| Naive Bayes | A math-based algorithm that learns from patterns |
| Accuracy | Percentage of emails the model classified correctly |
| Confusion Matrix | A table showing correct vs wrong predictions |

---

## What Makes an Email Look Phishing?
The model learns to spot words like:
- *"Click here", "Free", "Win", "Urgent", "Verify your account"*

Safe emails usually contain words like:
- *"Meeting", "Report", "Invoice", "Schedule", "Project"*

---

## Real World Use
This is exactly how Gmail and Outlook detect spam in your inbox. Big companies use the same idea but with millions of emails and more advanced models. This project is a beginner-friendly version of that same concept.

# Output:

<img width="733" height="567" alt="Image" src="https://github.com/user-attachments/assets/10bffd20-eff4-4616-adff-962707e71049" />
