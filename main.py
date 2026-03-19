def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi,1)

def calculate_group_averages(patients):
    total = 0
    count = 0
    for patient in patients:
        total += calculate_bmi(patient["weight"], patient["height"])
        count +=1
    return round((total/count),1)


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

def classify_heart_rate(heart_rate):
    if heart_rate < 60:
        return "Low"
    elif heart_rate < 100:
        return "Normal"
    else:
        return "High"
   

def analyze_patient(patient):
    BMI =  calculate_bmi(patient["weight"], patient["height"])
    classification = classify_bmi(calculate_bmi(patient["weight"], patient["height"]))
    print(f"Patient: {patient["name"]} | Age: {patient["age"]}")
    print(f"BMI: {BMI} - {classification} ")
    print(f"Blood Pressure: {classify_blood_pressure(patient["systolic_bp"],patient["diastolic_bp"])}")
    print(f"Heart rate: {classify_heart_rate(patient["heart_rate"])}")
    

def flag_at_risk(patient):
    abnormal_count = 0
    if classify_bmi(calculate_bmi(patient["weight"], patient["height"])) != "Normal":
        abnormal_count +=1
    if classify_blood_pressure(patient["systolic_bp"],patient["diastolic_bp"]) != "Normal":
        abnormal_count += 1
    if classify_heart_rate(patient["heart_rate"]) != "Normal":
        abnormal_count +=1
    if abnormal_count >= 2:
        return "STATUS: AT RISK"
    else:
        return "STATUS: LOW RISK"
    
def group_summary(patients):
    count = 0
    print(f"Average BMI across all patients: {calculate_group_averages(patients)}")
    for patient in patients:
        if flag_at_risk(patient) == "STATUS: AT RISK":
            count +=1
    print(f"Total number of at-risk patients: {count}")
          
if __name__ == "__main__":
    patients = [
    {
        "name": "Alice",
        "age": 45,
        "weight": 78,
        "height": 1.65,
        "systolic_bp": 145,
        "diastolic_bp": 95,
        "heart_rate": 95
    },
    {
        "name": "Bob",
        "age": 32,
        "weight": 72,
        "height": 1.80,
        "systolic_bp": 118,
        "diastolic_bp": 76,
        "heart_rate": 95
    },
    {
        "name": "Claire",
        "age": 58,
        "weight": 95,
        "height": 1.70,
        "systolic_bp": 155,
        "diastolic_bp": 100,
        "heart_rate": 110
    }]
    for patient in patients:
        analyze_patient(patient)
        print(flag_at_risk(patient))
        print("-" * 40)
    print("\n--- ADD A NEW PATIENT ---")
    name = input("Patient name: ")
    age = int(input("Age: "))
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    heart_rate = int(input("Heart rate (bpm): "))
    systolic_bp = int(input("Systolic blood pressure: "))
    diastolic_bp = int(input("Diastolic blood pressure: "))
    input_patient = {}
    input_patient["name"] = name
    input_patient["age"] = age
    input_patient["weight"] = weight
    input_patient["height"] = height
    input_patient["heart_rate"] = heart_rate
    input_patient["systolic_bp"] = systolic_bp
    input_patient["diastolic_bp"] = diastolic_bp
    patients.append(input_patient)

    analyze_patient(input_patient)
    print(flag_at_risk(input_patient))
    print("-" * 40)
    group_summary(patients)