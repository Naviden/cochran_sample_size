rom scipy.stats import norm

def sample_size(confidence_level, precision, population_size=None):
    Z = norm.ppf(confidence_level)

