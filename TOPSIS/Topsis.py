#Implementation of Multi-Criteria Decision-Making model named Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)

import numpy as np
import operator

decision_matrix = np.array([[1.2, 2.341, 0.701], [4.1, 0.009, 1.09]])
M = len(decision_matrix) #number of alternatives
N = len(decision_matrix[0]) #number of criteria per alternative

def normalize_dm():
    '''
    normalize the decision matrix to allow for criterion consistency amongst alternatives 
    '''
    dm_copy = np.copy(decision_matrix)
    for i in range(M):
        for j in range(N):
            dm_copy[i][j] = dm_copy[i][j] * dm_copy[i][j]
    column_sum = np.sum(dm_copy, axis=0)
    for i in range(M):
        for j in range(N):
            decision_matrix[i][j] = decision_matrix[i][j] / np.sqrt(column_sum[i])
            
def apply_weights(weight_vector=[(1/N) for i in range(N)]):
    '''
    this method multiplies each value in the decision matrix by its assigned weight, by default the weights are set to equal values of (1/N)
    '''
    for i in range(M):
        for j in range(N):
            decision_matrix[i][j] = decision_matrix[i][j] * weight_vector[j]
                
def calc_seperations():
    '''
    calculate the Euclidean distance between every alternative and (1) the Positive Ideal Solution, and (2) the Negative Ideal Solution
    '''
    
    pos_ideal = (np.amax(decision_matrix, axis=0))
    neg_ideal = (np.amin(decision_matrix, axis=0))
    
    seperations = np.array([[0.0 for i in range(M)], [0.0, 0.0]])
    pos_distance = 0.0
    neg_distance = 0.0
    for i in range(M):
        pos_distance = np.subtract(decision_matrix[i], pos_ideal)
        pos_distance = np.sqrt(np.sum(np.square(pos_distance)))
        
        neg_distance = np.subtract(decision_matrix[i], neg_ideal)
        neg_distance = np.sqrt(np.sum(np.square(neg_distance)))
 
        seperations[i][0] = pos_distance
        seperations[i][1] = neg_distance
        
        pos_distance = 0.0
        neg_distance = 0.0
    return seperations

def calc_relative_closeness():
    '''
    calculate how close each alternative is to the positive ideal solution, relative to the negative ideal solution
    '''
    seperations = calc_seperations()
    relative_closeness = np.array([0.0 for i in range(M)])
    for i in range(M):
        relative_closeness[i] = seperations[i][1] / (seperations[i][1] + seperations[i][0])
    return relative_closeness
        
def rank():
    '''
    rank the alternatives from best to worst according to their relative closeness values, maximum closeness scores are desired 
    '''
    relative_closeness = calc_relative_closeness()
    alternatives = np.array([i for i in range(1, M + 1)])
    scores = dict.fromkeys(alternatives)
    
    i = 0
    for alt, val in scores.items():
        scores[alt] = relative_closeness[i]
        i = i + 1
        
    ranked_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    print(str(ranked_scores))
    