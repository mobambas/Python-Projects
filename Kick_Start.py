def min_strokes_to_paint(N, painting):
    strokes = 0
    current_color = "Uncolored"

    for color in painting:
        if color == "Uncolored":
            continue
        elif color == "Gray":
            # Gray can be combined with any color, so we just update the current color
            current_color = "Gray"
        else:
            # For primary colors, we need a new stroke
            if current_color != color:
                strokes += 1
            current_color = color

    # If the last square is uncolored, no additional stroke is needed
    if current_color != "Uncolored":
        strokes += 1

    return strokes

# Example usage:
N = 8
painting = ["Red", "Yellow", "Blue", "Uncolored", "Red", "Yellow", "Blue", "Gray"]
result = min_strokes_to_paint(N, painting)
print("Minimum strokes:", result)
