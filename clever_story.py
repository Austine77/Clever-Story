def clever_stories():
    # Ask the user for inputs
    silly = input("Enter a silly adjective: ")
    cat = input("Enter an animal (e.g., cat): ")
    run = input("Enter a verb (e.g., run): ")
    wow = input("Enter an exclamation (e.g., wow): ").capitalize()  # Automatically capitalize exclamation
    jump = input("Enter a verb (e.g., jump): ")
    dance = input("Enter a verb (e.g., dance): ")
    
    # Story template
    story = (
        f"The other day, I was really in trouble. It all started when I saw a very "
        f"{silly} {cat} {run} down the hallway. \"{wow}!\" I yelled. "
        f"But all I could think to do was to {jump} over and over. Miraculously, "
        f"that caused it to stop, but not before it tried to {dance} "
        f"right in front of my family."
    )
    
    # Print the final story
    print("\nHere's your story:\n")
    print(story)

# Call the function
clever_stories()