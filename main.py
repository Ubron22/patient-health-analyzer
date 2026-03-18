def calculate_bmi(weight, height):
  bmi = weight / (height ** 2)
  return round(bmi,1)

def classify_bmi(bmi):
    if bmi < 18.5:
      return "Underweight"
    elif bmi <= 25:
      return "Normal"
    elif bmi <= 30:
      return "Overweight"
    else:
      return "Obese"
    
def classify_blood_pressure(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif systolic < 130:
        return "Elevated"
    elif systolic < 140:
        return "High Stage 1"
    else:
        return "High Stage 2"
   
def analyze_patient(patient):
    BMI =  calculate_bmi(patient["weight"], patient["height"])
    classification = classify_bmi(calculate_bmi(patient["weight"], patient["height"]))
    print(f"Patient: {patient["name"]} | Age: {patient["age"]}")
    print(f"BMI: {BMI} - {classification} ")
    print(f"Blood Pressure: {classify_blood_pressure(patient["systolic_bp"],patient["diastolic_bp"])}")
    

def flag_at_risk(patient):
    abnormal_count = 0
    if classify_bmi(calculate_bmi(patient["weight"], patient["height"])) != "Normal":
       abnormal_count +=1
    if classify_blood_pressure(patient["systolic_bp"],patient["diastolic_bp"]) != "Normal":
       abnormal_count +=1
    if abnormal_count >= 2:
       return "STATUS: AT RISK"
    else:
       return "STATUS: LOW RISK"


if __name__ == "__main__":
    patients = [
    {
        "name": "Alice",
        "age": 45,
        "weight": 78,
        "height": 1.65,
        "systolic_bp": 145,
        "diastolic_bp": 95
    },
    {
        "name": "Bob",
        "age": 32,
        "weight": 72,
        "height": 1.80,
        "systolic_bp": 118,
        "diastolic_bp": 76
    },
    {
        "name": "Claire",
        "age": 58,
        "weight": 95,
        "height": 1.70,
        "systolic_bp": 155,
        "diastolic_bp": 100
    }]
    for patient in patients:
        analyze_patient(patient)
        print(flag_at_risk(patient))
        print("-" * 40)
