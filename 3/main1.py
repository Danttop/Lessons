def area_code(text):
    return (text.split("(", 2))[1][:3]
