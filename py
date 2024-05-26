import praw
import re

# Define your bot's credentials
reddit = praw.Reddit(
    client_id='YrIoQG2rUM3rwJ1UnHLiZQ',
    client_secret='9pu08oq10kvyHUJzqE75x1UdjxCSGw',
    username='Messiahofmorons',
    password='Xiao*2212',
    user_agent='Reddit Bot to Answer Questions with LMGTFY links'
)

# Function to generate LMGTFY link
def generate_lmgtfy_link(query):
    return f"http://lmgtfy.com/?q={query.replace(' ', '+')}"

# Function to check if a comment is a general question
def is_general_question(comment_body):
    # Simple check for question marks and common question words
    return re.search(r'\b(who|what|when|where|why|how)\b', comment_body, re.IGNORECASE) and '?' in comment_body

# Stream comments and reply with LMGTFY link if it is a general question
for comment in reddit.subreddit('all').stream.comments(skip_existing=True):
    if is_general_question(comment.body):
        query = comment.body
        lmgtfy_link = generate_lmgtfy_link(query)
        comment.reply(f"It's not even that hard, you dumbo. Let me do that for you lazy slog: [LMGTFY]({lmgtfy_link})")
        print(f"Replied to comment: {comment.body}")
