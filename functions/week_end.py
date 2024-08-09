import random as rd

from datetime import datetime


# Lecture depuis bucket
# Modif fichier source
# Lambda lecture
# Lambda modif

def generate_weekend_program():
    """
    Generates a weekend program based on the activities listed in the "TODO.txt" file.

    Returns:
        str: A markdown-formatted string representing the weekend program.
    """
    with open("TODO.txt", 'r', encoding="utf-8") as f:
        activities = f.readlines()
    activities = [activity.strip() for activity in activities]

    # Si fin du mois, on fait les comptes
    if datetime.now().day > 26 or datetime.now().day < 5:
        selected_activities = ["Comptes", "Se raser"]
        selected_activities += rd.sample(activities, 3)
    else:
        selected_activities = ["Se raser"]
        selected_activities += rd.sample(activities, 4)

    markdown = "# Week-end program\n\n"
    for _, activity in enumerate(selected_activities):
        markdown += f"- {activity}\n"

    return markdown
