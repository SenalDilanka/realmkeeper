import logging
from strands import Agent

# Step 1: Enable debug logging
logging.getLogger("strands").setLevel(logging.DEBUG)

logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# Step 2: Create the Game Master agent
agent = Agent(
    system_prompt="You are a game master for a fantasy role-playing game"
)

# Step 3: Invoke your agent
agent("Hi, I am an adventurer ready for adventure!")