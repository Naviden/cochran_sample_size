from scipy.stats import norm

#https://shodhganga.inflibnet.ac.in/bitstream/10603/23539/7/07_chapter%202.pdf


def cochran(confidence_level, margin_of_error, population_size=None, round=True, p=0.5):
    """Calculate sample size based on Cochran (1977) method """
    Z = norm.ppf(1 - (1 - confidence_level) / 2) # two-tailed
    print(Z)
    n0 = ((Z ** 2) * p * (1-p)) / (margin_of_error ** 2)
    if population_size is None:
        if round:
            n0 = int(n0)
        return n0
    else:
        n = n0 / (1 + ((n0 - 1)  / population_size))
        if round:
            n = int(n)
        return n

def yamane(margin_of_error, population_size, round=True):

    """Calculate sample size based on Yamane (1967) method
       Assumption : 95% confidence level and p = 0.5 """
    n = population_size / (1 + (population_size * (margin_of_error ** 2)))
    if round:
        n = int(n)
    return n

print(cochran(0.95, 0.05, 60_000_000))
print(yamane(0.05, 60_000_000))

