import string
def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.endswith("?") and not hey_bob.isupper():
        answer = "Sure."
    elif hey_bob.isupper() and not hey_bob.endswith("?"):
        answer = "Whoa, chill out!"
    elif hey_bob.isupper() and hey_bob.endswith("?"):
        answer = "Calm down, I know what I'm doing!"
    elif len(hey_bob) == 0:
        answer = "Fine. Be that way!"
    else:
        answer = "Whatever."
    return answer
