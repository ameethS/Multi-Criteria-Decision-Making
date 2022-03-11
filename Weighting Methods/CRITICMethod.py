# CRITIC Weighting Method - Criteria Importance through Inter-criteria Correlation  

import numpy as np
import csv

def normalize(decision_matrix):
    parameters = [[0.0 for i in range(0, len(decision_matrix))], [0.0 for i in range(0, len(decision_matrix))]] #0=max, 1=min
    
    for i in range(0, len(decision_matrix[0])):
        max = decision_matrix[0][i]
        min = decision_matrix[0][i]        
        for j in range(0, len(decision_matrix)):
            if decision_matrix[j][i] > max:
                max = decision_matrix[j][i]
            if decision_matrix[j][i] < min:
                min = decision_matrix[j][i]
        parameters[0][i] = max
        parameters[1][i] = min
    
    for i in range(0, len(decision_matrix[0])):
        for j in range(0, len(decision_matrix)):
            decision_matrix[j][i] = (decision_matrix[j][i] - parameters[1][i]) / (parameters[0][i] - parameters[1][i])
            
    return decision_matrix

def calculate_std_dev(decision_matrix):
    std_dev = [0.0 for i in range(0, len(decision_matrix[0]))]
    mean = [0.0 for i in range(0, len(decision_matrix[0]))]
    
    for i in range(0, len(decision_matrix[0])):
        for j in range(0, len(decision_matrix)):
            mean[i] = mean[i] + decision_matrix[j][i]
        mean[i] = mean[i] / len(decision_matrix)
    
    for i in range(0, len(decision_matrix[0])):
        for j in range(0, len(decision_matrix)):
            std_dev[i] = std_dev[i] +  pow(decision_matrix[j][i] - mean[i], 2)
        std_dev[i] = np.sqrt(std_dev[i] / len(decision_matrix))
    
    return std_dev

def calculate_correlation(decision_matrix):
    corr_matrix = [[0.0 for i in range(0, len(decision_matrix[0]))] for i in range(0, len(decision_matrix[0]))]
    
    mean = [0.0 for i in range(0, len(decision_matrix[0]))]
    
    for i in range(0, len(decision_matrix[0])):
        for j in range(0, len(decision_matrix)):
            mean[i] = mean[i] + decision_matrix[j][i]
        mean[i] = mean[i] / len(decision_matrix)    
    
    for i in range(0, len(decision_matrix[0])):
        for j in range(0, len(decision_matrix[0])):
            numerator_sum = 0.0
            denominator_sum1 = 0.0
            denominator_sum2 = 0.0
            for k in range(0, len(decision_matrix)):
                numerator_sum = numerator_sum + ( (decision_matrix[k][i] - mean[i]) * (decision_matrix[k][j] - mean[j]) ) 
                denominator_sum1 = denominator_sum1 + pow(decision_matrix[k][i] - mean[i], 2)
                denominator_sum2 = denominator_sum2 + pow(decision_matrix[k][j] - mean[j], 2)
            corr_matrix[i][j] = numerator_sum / np.sqrt(denominator_sum1 * denominator_sum2)
    return corr_matrix
            
def calculate_corr_diff_one(correlation):
    for i in range(0, len(correlation)):
        for j in range(0, len(correlation)):
            correlation[i][j] = 1 - correlation[i][j]
    return correlation

def sum_correlation(correlation):
    sums = [0.0 for i in range(0, len(correlation))]
    for i in range(0, len(correlation)):
        for j in range(0, len(correlation)):
            sums[i] = sums[i] + correlation[i][j]
    return sums

def calculate_cj(std_dev, sum_corr):
    cj = [0.0 for i in range(0, len(sum_corr))]
    for i in range(0, len(sum_corr)):
        cj[i] = std_dev[i] * sum_corr[i]
    return cj

def calculate_weights(cj):
    sum = 0.0
    for i in cj:
        sum = sum + i
    weights = [0.0 for i in range(0, len(cj))]
    for j in range(0, len(weights)):
        weights[j] = cj[j] / sum
    return weights


dm = [[1,0.938596491,0.928416486,0.841463415],
[0.977678571,1,0.223427332,0.56097561],
[0.830357143,0.48245614,1,1],
[0.558035714,0.394736842,0.279826464,0.573170732],
[0.915178571,0.807017544,0.789587853,0.987804878],
[0.625,0.00877193,0.160520607,0.207317073],
[0.915178571,0.578947368,0.937093276,1],
[0.723214286,0.429824561,0.687635575,0.768292683],
[0.651785714,0.473684211,0.665943601,0.756097561],
[0.544642857,0.429824561,0.288503254,0.707317073],
[0.821428571,0.745614035,0.169197397,0.43902439],
[0.665178571,0.850877193,0.739696312,0.975609756],
[0.598214286,0.342105263,0.646420824,0.865853659],
[0.558035714,0.692982456,0.197396963,0.475609756],
[0,0,0,0],
[0.883928571,0.263157895,0.718004338,0.756097561]]

d1 = normalize(dm)
std_dev = calculate_std_dev(d1)
corr1 = calculate_correlation(d1)
corr2 = calculate_corr_diff_one(corr1)
sums = sum_correlation(corr2)
cjs = calculate_cj(std_dev, sums)
ws = calculate_weights(cjs)
