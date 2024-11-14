import random
import time

# Display the stages in the hospital process
stages = ["Reception", "Triage", "Doctor", "Hospitalization Decision"]
print("Hospital Elevator Simulation: Moving a patient through the stages")

# Simulate each stage with a delay
for stage in stages:
    print(f"Patient is at the {stage} stage.")
    time.sleep(1)  # simulate processing time with a 1-second delay

# Random outcome for the patient
outcome = random.choice(["Discharged", "Hospitalized"])
time.sleep(1)
if outcome == "Discharged":
    print("Outcome: Patient has been Discharged from the hospital.")
else:
    print("Outcome: Patient has been Hospitalized for further treatment.")
