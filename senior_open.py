def open_or_senior(data):
    output = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])