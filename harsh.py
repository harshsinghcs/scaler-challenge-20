def mad_libs():
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")
    pronoun = input("Enter a pronoun: ")
    adjective = input("Enter an adjective: ")

    story = (
        f"On a {adjective} morning, {pronoun} {verb} to school with excitement. " 
        f"The {noun} in {pronoun}'s backpack feels heavy but full of potential adventures. " 
        f"At the school gate, {pronoun} waves goodbye to {pronoun} {adjective} parents, ready to face the day. " 
        f"In class, {pronoun} eagerly raises {pronoun} hand, eager to learn and explore."
    )

    print(story)


if __name__ == "__main__":
    mad_libs()
