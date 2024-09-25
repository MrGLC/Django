def desk_chair_height(height):
    # Split the string into feet and the rest (inches with the inch symbol)
    feet, rest = height.split('\'')
    # Remove the inch symbol (") from the inches part
    inches = rest.replace('"', '')  # This removes the " character from the inches part
    # Convert feet and inches to total inches
    total_inches = int(feet) * 12 + int(inches)
    # Calculate desk and chair heights
    desk_height = total_inches * 0.56  # 56% of total height
    chair_height = total_inches * 0.29  # 29% of total height
    return {'desk_height': desk_height, 'chair_height': chair_height}

# Example usage
height = "5'10\""  # 5 feet 10 inches
suggested_heights = desk_chair_height(height)
print(suggested_heights)

