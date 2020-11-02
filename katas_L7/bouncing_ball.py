def bouncing_ball(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1


print(bouncing_ball(3, 0.66, 1.5))

# testing(3, 0.66, 1.5, 3)
# testing(30, 0.66, 1.5, 15)
