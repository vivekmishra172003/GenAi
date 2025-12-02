import random
from fastmcp import FastMCP

# Creating server instance

mcp = FastMCP(name="server", port=5000)

@mcp.tool
def roll_dice(n: int) -> list[int]:
    return [random.randint(1, 6) for _ in range(n)]

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run()

    