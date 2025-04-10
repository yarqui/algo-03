"""This script draws the Koch snowflake fractal using the turtle graphics module.

It includes two functions:
- `koch_curve()`: Recursively generates a Koch curve segment.
- `draw_koch_curve()`: Uses three Koch curves to draw a full Koch snowflake of specified order.
"""

import turtle


def koch_curve(t, order, size):
    """
    Recursively draws a single side of the Koch curve using the turtle.

    Args:
        t (turtle.Turtle): A turtle instance used for drawing.
        order (int): The recursion depth (fractal complexity).
        size (float): The length of the curve to draw.

    Base Case:
        If order == 0, draw a straight line.

    Recursive Step:
        Divide the line into 3 parts and recursively draw with turns to form a "snowflake" shape.
    """

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    """
    Sets up the turtle screen and draws a full Koch snowflake.

    Args:
        order (int): The depth of recursion to control the fractal complexity.
        size (float): Total length of each side of the snowflake.

    This function:
    - Initializes the drawing screen and turtle.
    - Positions the turtle to the starting point.
    - Draws 3 Koch curves rotated to form an equilateral triangle.
    - Keeps the window open for viewing.
    """

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    while True:
        resp = input(
            "Please select an order of recursion (only integers), or 'q' to exit: "
        )
        if resp == "q":
            print("\nExiting...\n")
            break

        try:
            order = int(resp)
            draw_koch_curve(order)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
