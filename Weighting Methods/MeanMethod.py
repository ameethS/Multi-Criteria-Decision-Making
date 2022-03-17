# Mean Weighting method

'''
returns a list of weights for each criterion, where the ith weight corresponds to the ith criterion
'''
def calculate_weights(number_of_criteria):
    if number_of_criteria == 0:
        return 0
    else:
        weights = [(1/number_of_criteria) for i in range(0, number_of_criteria)]
    return weights


'''
Application
'''
num_criteria = 10
print(calculate_weights(num_criteria))