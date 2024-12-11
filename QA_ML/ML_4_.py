def probability_of_disease(accuracy, prevalence):
    # Calculate sensitivity and specificity
    sensitivity = accuracy
    specificity = accuracy
    
    # Calculate Positive Predictive Value (PPV)
    ppv = (sensitivity * prevalence) / ((sensitivity * prevalence) + ((1 - specificity) * (1 - prevalence)))
    
    # Calculate Negative Predictive Value (NPV)
    npv = (specificity * (1 - prevalence)) / (((1 - sensitivity) * prevalence) + (specificity * (1 - prevalence)))
    return [100*ppv, 100*npv]



# # Sample input
# accuracy = 0.95
# prevalence = 0.03

# # Calculate and print the probabilities
# probabilities = calculate_probabilities(accuracy, prevalence)
# print(probabilities)