from fuzzy_logic import compute_risk

def get_user_input():
    # Prompt user for inputs
    age = int(input("Enter age: "))
    sex = int(input("Enter sex (0 = female, 1 = male): "))
    cholesterol = int(input("Enter cholesterol level: "))
    # Continue with other parameters...
    
    # Call fuzzy logic to compute risk
    risk_level = compute_risk(age, cholesterol)
    
    # Display the risk level
    print(f"Heart Disease Risk Level: {risk_level}")

if __name__ == "__main__":
    get_user_input()
