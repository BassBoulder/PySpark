def response(hey_bob):
    bobby_talk = hey_bob.strip()
    
    match bobby_talk:
        case "":
            return "Fine. Be that way!"
        case answer if bobby_talk.isupper() and bobby_talk.endswith("?"):
            return "Calm down, I know what I'm doing!"
        case answer if bobby_talk.isupper():
            return "Whoa, chill out!"
        case answer if bobby_talk.endswith("?"):
            return "Sure."
        case _:
            return "Whatever."