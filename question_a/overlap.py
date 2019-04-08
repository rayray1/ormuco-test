def check_overlap(line1, line2):
    if line1[0] > line2[0]:
        line1, line2 = line2, line1
    return line2[0] >= line1[0] and line2[0] < line1[1]
