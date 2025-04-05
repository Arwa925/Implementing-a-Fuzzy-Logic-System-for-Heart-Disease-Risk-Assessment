import skfuzzy as fuzz
import numpy as np

def define_membership_functions():
    # Define fuzzy sets for age, cholesterol, etc.
    age = np.arange(0, 101, 1)
    cholesterol = np.arange(0, 701, 1)
    risk = np.arange(0, 11, 1)

    # Membership functions for age (Low, Medium, High)
    age_low = fuzz.trimf(age, [0, 0, 50])
    age_medium = fuzz.trimf(age, [30, 50, 70])
    age_high = fuzz.trimf(age, [50, 80, 100])

    # Membership functions for cholesterol (Low, Medium, High)
    chol_low = fuzz.trimf(cholesterol, [0, 0, 200])
    chol_medium = fuzz.trimf(cholesterol, [100, 200, 300])
    chol_high = fuzz.trimf(cholesterol, [200, 400, 700])

    # Risk level (Low, Medium, High)
    risk_low = fuzz.trimf(risk, [0, 0, 5])
    risk_medium = fuzz.trimf(risk, [3, 5, 7])
    risk_high = fuzz.trimf(risk, [6, 10, 10])

    return age, cholesterol, risk, age_low, age_medium, age_high, chol_low, chol_medium, chol_high, risk_low, risk_medium, risk_high

def define_fuzzy_rules(age, cholesterol, risk, age_low, age_medium, age_high, chol_low, chol_medium, chol_high, risk_low, risk_medium, risk_high):
    # Fuzzy rule examples: If cholesterol is high and age is high, risk is high
    risk_chol_age_high = fuzz.relation_product(chol_high, age_high)
    risk_high_level = fuzz.relation_product(risk_chol_age_high, risk_high)

    # Combine rules to get final result
    return risk_high_level

def compute_risk(age_input, cholesterol_input):
    # Get membership functions
    age, cholesterol, risk, age_low, age_medium, age_high, chol_low, chol_medium, chol_high, risk_low, risk_medium, risk_high = define_membership_functions()

    # Apply fuzzy rules
    risk_result = define_fuzzy_rules(age, cholesterol, risk, age_low, age_medium, age_high, chol_low, chol_medium, chol_high, risk_low, risk_medium, risk_high)
    
    # Defuzzify the result to get crisp output
    return np.round(fuzz.defuzz(risk, risk_result, 'centroid'))

