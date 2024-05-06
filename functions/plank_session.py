import random as rd


def generate_plank_session():

    markdown = "# Plank session\n\n"
    positions = ["low", "high", "left", "right"]

    nb_series = rd.randint(1, 4)
    for i in range(nb_series):
        markdown += f"## Series {i+1}\n"
        for _, position in enumerate(positions):
            duration = rd.randint(1, 60)
            markdown += f"- {position} for {duration} seconds\n"

    return markdown
