def abcd_to_xywh(a, b, c, d, width, height):
    """
    Convert absolute coordinates (a, b, c, d) to relative XYWH format.
    
    Parameters:
    a (int): The horizontal starting point.
    b (int): The vertical starting point.
    c (int): The horizontal ending point.
    d (int): The vertical ending point.
    width (int): The width of the image.
    height (int): The height of the image.
    
    Returns:
    A tuple of (X, Y, W, H) in relative percentage format.
    """
    X = (a / width) * 100
    Y = (b / height) * 100
    W = (c - a) / width * 100
    H = (d - b) / height * 100
    
    return X, Y, W, H

# Example usage:
# For an image of 1500x1000 pixels, convert the absolute coordinates {150, 100, 450, 300} to XYWH.
# a, b, c, d = 571, 22, 1359, 810
# width, height = 1456, 816
# xywh = abcd_to_xywh(a, b, c, d, width, height)

# print(f"Absolute coordinates {a, b, c, d} convert to XYWH format: {xywh}")