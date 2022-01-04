#Implementation of the Multi-Criteria Decision-Making model entitled Weighted Sum Model (WSM)

import numpy as np
import operator

decision_matrix = np.array([[1.9, 3.0, 2.4], [1.2, 3.2, 1.5]])
M = len(decision_matrix)
N = len(decision_matrix[0])

def apply_weights(weights=[(1/N) for i in range(N)]):
    '''
    apply weights (given as parameter) to the decision matrix, weights are set by default to equal weighting
    '''
    for i in range(M):
        decision_matrix[i] = np.multiply(decision_matrix[i], weights)
        
def calc_score():
    '''
    calculate the WSM-score for each alternative, which is the sum of that alternatives weighted criteria 
    '''
    wsm_score = np.full(M, 0.0)
    for i in range(M):
        wsm_score[i] = np.sum(decision_matrix[i])
    return wsm_score
        
def rank():
    '''
    rank the WSM-scores, higher scores are desirable
    '''
    wsm_score = calc_score()
    alternatives = np.array([i for i in range(1, M + 1)])
    scores = dict.fromkeys(alternatives)
    
    i = 0
    for alt, val in scores.items():
        scores[alt] = wsm_score[i]
        i = i + 1
        
    ranked_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    print(str(ranked_scores))  
    