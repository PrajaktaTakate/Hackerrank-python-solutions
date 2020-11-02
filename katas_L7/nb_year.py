def nb_year_v1(p0, percent, aug, p):
    count = 0
    while p0 < p:
        count = count + 1
        p0 = ((p0 * percent) / 100) + aug + p0
    return count


def nb_year_v2(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year_v2(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

print(nb_year_v1(1500, 5, 100, 5000))
print(nb_year_v2(1500, 5, 100, 5000))

