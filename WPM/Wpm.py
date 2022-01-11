#Implementation of the Multi-Criteria Decision-Making model known as the Weighted Product Model (WPM)

import numpy as np
import operator


decision_matrix = np.array([[1.9, 3.0, 2.4], [1.2, 3.2, 1.5]])
M = len(decision_matrix)
N = len(decision_matrix[0])

def set_weights(weights=[(1/N) for i in range(N)]):
    '''
    Set the weights for the criteria
    NB: Weights are set to equal weighting (i.e. 1/N) by default
    '''
    weights = weights
    return weights

def normalize_dm():
    '''
    The decision matrix is normalized to allow for consistency
    NB: it is assumed all criteria are poisitve criteria rather than cost criteria
    '''
    global decision_matrix
    max_criteria = np.amax(decision_matrix, axis=0)
    decision_matrix = np.divide(decision_matrix, max_criteria)
    
def calc_ratios():
    '''
    The weighted ratios between all alternatives are calculated 
    '''
    weights = set_weights()
    ratios = np.zeros((M, M))
    product = 1.0
    for K in range(M):
        for L in range(M):
            product = 1.0
            for j in range(N):
                product = product * np.power((decision_matrix[K][j] / decision_matrix[L][j]), weights[j])
            ratios[K][L] = product
    return ratios

def calc_scores():
    '''
    The score for each alternative is calculated by counting the number of times an alternative is preferred to 
    another alternative 
    '''
    ratios = calc_ratios()
    values = np.array([0.0 for i in range(M)])
    for L in range(M):
        for K in range(M):
            if K != L:
                if ratios[K][L] >= 1:
                    values[K] = values[K] + 1
    return values

def rank():
    '''
    rank the alternatives from best to worst 
    '''
    values = calc_scores()
    alternatives = np.array([i for i in range(1, M + 1)])
    scores = dict.fromkeys(alternatives)
    
    i = 0
    for alt, val in scores.items():
        scores[alt] = values[i]
        i = i + 1
        
    ranked_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    print(str(ranked_scores))
    
rank()