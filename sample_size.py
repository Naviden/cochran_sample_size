from scipy.stats import norm

def cochran(confidence_level, precision, population_size=None, round=True, p=0.5):
    Z = norm.ppf(confidence_level)
    print(Z)
    n0 = ((Z ** 2) * p * (1-p)) / precision ** 2
    if population_size is None:
        if round:
            n0 = int(n0)
        return n0
    else:
        n = n0 / (1 + (n0 -1) / population_size)
        if round:
            n = int(n)
        return n

def yamane(precision, population_size):
    
    """Calculate sample size based on Yamane (1967) method
    Assumption : 95% confidence level and p = 0.5"""
    return population_size / (1 + (population_size * (precision ** 2)))

print(sample_size(0.95, 0.05))

