from strands import Agent, tool  # Step 1: import tool


@tool  # Step 1: decorator transforms the function into a tool
def roll_dice(faces: int = 6) -> int:
    """Roll a single die and return the result.

    Use this tool every time a die needs to be rolled. Each call rolls
    exactly one die, so call it once per die.

    Args:
        faces: Number of faces on the die (for example 6 for a d6, 20 for a d20).

    Returns:
        An integer between 1 and the number of faces, inclusive.
    """
    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


print(roll_dice.tool_spec)  # what Strands tells the model about your tool

dice_master = Agent(
    tools=[roll_dice],  # Step 3: add the tool to the agent
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in fantasy role-playing adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about the game mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

dice_master("Help me create a new fantasy character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")