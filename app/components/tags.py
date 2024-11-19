from streamlit_extras.tags import tagger_component

def render_tags(tag_dict, description="AI subject tags"):
    """
    Displays tags with consistent color coding for each subject using the tagger_component.

    Parameters:
    description (str): A brief description or label for the tag set.
    tags (list): A list of tags to display.
    """

    tags = tag_dict.get("tags", [])

    # Predefined colors limited to the allowed list
    colors = ["lightblue", "orange", "bluegreen", "blue", "violet", "red", "green", "yellow"]
    # Generate colors for the tags (cycle through the colors list if more tags than colors)
    tag_colors = [colors[i % len(colors)] for i in range(len(tags))]

    # Optional: You can define text colors as well, here using 'white' for all tags
    text_colors = ["white"] * len(tags)  # All tags will have white text

    # Display the tags using tagger_component
    tagger_component(content=description, tags=tags, color_name=tag_colors, text_color_name=text_colors)
