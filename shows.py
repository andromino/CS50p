SHOWS = [
    "Avitar: the last airbender",
    "The office",
    "The simpsons",
    "The walking dead",
    "The big bang theory",
    "The office",
    "The simpsons",
    "The walking dead",
    "The big bang theory",
    "The office",
    "The simpsons",
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    
    print("; ".join(cleaned_shows))


main()