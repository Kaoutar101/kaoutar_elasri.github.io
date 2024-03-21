# -*- coding: utf-8 -*-
"""Data_analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P4FJKz5hs433nMDB5X2h4f8rx6CSR1Pb

This code cleans data and removes redunudant rows.
The final output is a csv file that is easier to handle for data analysis and
representation.
link to the data used: https://www.kaggle.com/datasets/marslinoedward/disease-prediction-data
"""

import pandas as pd
import numpy as np
training=pd.read_csv('Training.csv')
training

table=pd.DataFrame({"itching":[0],
                                  "skin_rash":[0],
                                              "nodal_skin_eruptions":[0],
                                              "dischromic _patches":[0],
                                              "continous_sneezing":[0],
                                              "shivering":[0],
                                              "chills":[0],
                                              "joint_pain":[0],
                                              "stomach_pain":[0],
                                              "acidity":[0],
                                              "ulcers_on_tongue":[0],
                                              "muscle_wasting":[0],
                                              "vomiting":[0],
                                              "burning_micturition":[0],
                                              "fatigue":[0],
                                              "weight_gain":[0],
                                              "anxiety":[0],
                                              "cold_hands_and_feets":[0],
                                              "mood_swings":[0],
                                              "weight_loss":[0],
                                              "restlesness":[0],
                                              "lethargy":[0],
                                              "patches_in_throat":[0],
                                              "irregular_sugar_level":[0],
                                              "gar_level":[0],
                                              "cough":[0],
                                              "high_fever":[0],
                                              "sunken_eyes":[0],
                                              "breathlessness":[0],
                                              "sweating":[0],
                                              "dehydration":[0],
                                              "indigestion":[0],
                                              "headache":[0],
                                              "yellowish_skin":[0],
                                              "dark_urine":[0],
                                              "nausea":[0],
                                              "loss_of_appetite":[0],
                                              "pain_behind_the_eyes":[0],
                                              "back_pain":[0],
                                              "constipation":[0],
                                              "abdominal_pain":[0],
                                              "diarrhoea":[0],
                                              "mild_fever":[0],
                                              "yellow_urine":[0],
                                              "yellowing_of_eyes":[0],
                                               "acute_liver_failure":[0],
                                              "fluid_overload":[0],
                                 "swelling_of_stomach":[0],
                                "swelled_lymph_nodes":[0],
                                "malaise":[0],
                                "blurred_and_distorted_vision":[0],
                                "phlegm":[0],
                                "throat_irritation":[0],
                                "redness_of_eyes":[0],
                                "sinus_pressure":[0],
                                "runny_nose":[0],
                                "congestion":[0],
                                "chest_pain":[0],
                                "weakness_in_limbs":[0],
                                "fast_heart_rate":[0],
                                "pain_during_bowel_movements":[0],
                                "pain_in_anal_region":[0],
                                "bloody_stool":[0],
                                "irritation_in_anus":[0],
                                "neck_pain":[0],
                                "dizziness":[0],
                                "cramps":[0],
                                "bruising":[0],
                                "obesity":[0],
                                "swollen_legs":[0],
                                "swollen_blood_vessels":[0],
                                "puffy_face_and_eyes":[0],
                                "enlarged_thyroid":[0],
                                "brittle_nails":[0],
                                "swollen_extremeties":[0],
                                "excessive_hunger":[0],
                                "extra_marital_contacts":[0],
                                "drying_and_tingling_lips":[0],
                                "slurred_speech":[0],
                                "knee_pain":[0],
                                "hip_joint_pain":[0],
                                "muscle_weakness":[0],
                                "stiff_neck":[0],
                                "swelling_joints":[0],
                                "movement_stiffness":[0],
                                "spinning_movements":[0],
                                "loss_of_balance":[0],
                                "unsteadiness":[0],
                                "weakness_of_one_body_side":[0],
                                "loss_of_smell":[0],
                                "bladder_discomfort":[0],
                                "foul_smell_of urine":[0],
                                "continuous_feel_of_urine":[0],
                                "passage_of_gases":[0],
                                "internal_itching":[0],
                                "toxic_look_(typhos)":[0],
                                "depression":[0],
                                "irritability":[0],
                                "muscle_pain":[0],
                                "altered_sensorium":[0],
                                "red_spots_over_body":[0],
                                "belly_pain":[0],
                                "abnormal_menstruation":[0],
                                "watering_from_eyes":[0],
                                "increased_appetite":[0],
                                "polyuria":[0],
                                "family_history":[0],
                                "mucoid_sputum":[0],
                                "rusty_sputum":[0],
                                "lack_of_concentration":[0],
                                "visual_disturbances":[0],
                                "receiving_blood_transfusion":[0],
                                "receiving_unsterile_injections":[0],
                                "coma":[0],
                                "stomach_bleeding":[0],
                                "distention_of_abdomen":[0],
                                "history_of_alcohol_consumption":[0],
                                "fluid_overload":[0],
                                'blood_in_sputum':[0],
                                "prominent_veins_on_calf":[0],
                                "palpitations":[0],
                                "painful_walking":[0],
                                "pus_filled_pimples":[0],
                                "blackheads":[0],
                                "scurring":[0],
                                "skin_peeling":[0],
                                "silver_like_dusting":[0],
                                "small_dents_in_nails":[0],
                                "inflammatory_nails":[0],
                                "blister":[0],
                                "red_sore_around_nose":[0],
                                "yellow_crust_ooze":[0],
                                "spotting_ urination":[0]},index=[0])
table

fungal_infection=training[training.prognosis=='Fungal infection']
fungal_infection=fungal_infection.describe()
mean_values = fungal_infection.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
fungal_infection = fungal_infection.drop(columns=columns_to_remove)
fungal_infection

fungal_infection1=table.copy()
fungal_infection1.at[0,'itching']=1
fungal_infection1.at[0,'skin_rash']=1
fungal_infection1.at[0,'nodal_skin_eruptions']=1
fungal_infection1.at[0,'dischromic _patches']=1
fungal_infection1.index.name='fungal_infection'
fungal_infection1

Allergy=training[training.prognosis=='Allergy']
Allergy=Allergy.describe()
mean_values = Allergy.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Allergy = Allergy.drop(columns=columns_to_remove)
Allergy

Allergy1=table.copy()
Allergy1.at[0,'continous_sneezing']=1
Allergy1.at[0,'shivering']=1
Allergy1.at[0,'chills']=1
Allergy1.at[0,'watering_from_eyes']=1
Allergy1.index.name='Allergy'
Allergy1

GERD=training[training.prognosis=='GERD']
GERD=GERD.describe()
mean_values = GERD.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
GERD = GERD.drop(columns=columns_to_remove)
GERD

GERD1=table.copy()
GERD1.at[0,'stomach_pain']=1
GERD1.at[0,'acidity']=1
GERD1.at[0,'ulcers_on_tongue']=1
GERD1.at[0,'vomiting']=1
GERD1.at[0,'cough']=1
GERD1.at[0,'chest_pain']=1
GERD1.index.name='GERD'
GERD1

Chronic_cholestasis=training[training.prognosis=='Chronic cholestasis']
Chronic_cholestasis=Chronic_cholestasis.describe()
mean_values = Chronic_cholestasis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Chronic_cholestasis = Chronic_cholestasis.drop(columns=columns_to_remove)
Chronic_cholestasis

Chronic_cholestasis1=table.copy()
Chronic_cholestasis1.at[0,'yellowing_of_eyes']=1
Chronic_cholestasis1.at[0,'itching']=1
Chronic_cholestasis1.at[0,'yellowish_skin']=1
Chronic_cholestasis1.at[0,'nausea']=1
Chronic_cholestasis1.at[0,'vomiting']=1
Chronic_cholestasis1.at[0,'loss_of_appetite']=1
Chronic_cholestasis1.at[0,'abdominal_pain']=1
Chronic_cholestasis1.index.name='Chronic_cholestasis'
Chronic_cholestasis1

Drug_Reaction=training[training.prognosis=='Drug Reaction']
Drug_Reaction=Drug_Reaction.describe()
mean_values = Drug_Reaction.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Drug_Reaction = Drug_Reaction.drop(columns=columns_to_remove)
Drug_Reaction

Drug_Reaction1=table.copy()
Drug_Reaction1.at[0,'skin_rash']=1
Drug_Reaction1.at[0,'itching']=1
Drug_Reaction1.at[0,'stomach_pain']=1
Drug_Reaction1.at[0,'burning_micturition']=1
Drug_Reaction1.at[0,'spotting_ urination']=1
Drug_Reaction1.index.name='Drug_Reaction'
Drug_Reaction1

Peptic_ulcer_diseae=training[training.prognosis=='Peptic ulcer diseae']
Peptic_ulcer_diseae=Peptic_ulcer_diseae.describe()
mean_values = Peptic_ulcer_diseae.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Peptic_ulcer_diseae = Peptic_ulcer_diseae.drop(columns=columns_to_remove)
Peptic_ulcer_diseae

Peptic_ulcer_diseae1=table.copy()
Peptic_ulcer_diseae1.at[0,'vomiting']=1
Peptic_ulcer_diseae1.at[0,'indigestion']=1
Peptic_ulcer_diseae1.at[0,'loss_of_appetite']=1
Peptic_ulcer_diseae1.at[0,'abdominal_pain']=1
Peptic_ulcer_diseae1.at[0,'passage_of_gases']=1
Peptic_ulcer_diseae1.at[0,'internal_itching']=1
Peptic_ulcer_diseae1.index.name='Peptic_ulcer_diseae'
Peptic_ulcer_diseae1

AIDS=training[training.prognosis=='AIDS']
AIDS=AIDS.describe()
mean_values = AIDS.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
AIDS = AIDS.drop(columns=columns_to_remove)
AIDS

AIDS1=table.copy()
AIDS1.at[0,'muscle_wasting']=1
AIDS1.at[0,'patches_in_throat']=1
AIDS1.at[0,'high_fever']=1
AIDS1.at[0,'extra_marital_contacts']=1
AIDS1.index.name='AIDS'
AIDS1

Diabetes=training[training.prognosis=='Diabetes ']
Diabetes=Diabetes.describe()
mean_values = Diabetes.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Diabetes = Diabetes.drop(columns=columns_to_remove)
Diabetes

Diabetes1=table.copy()
Diabetes1.at[0,'fatigue']=1
Diabetes1.at[0,'weight_loss']=1
Diabetes1.at[0,'restlesness']=1
Diabetes1.at[0,'lethargy']=1
Diabetes1.at[0,'irregular_sugar_level']=1
Diabetes1.at[0,'blurred_and_distorted_vision']=1
Diabetes1.at[0,'obesity']=1
Diabetes1.at[0,'excessive_hunger']=1
Diabetes1.at[0,'increased_appetite']=1
Diabetes1.at[0,'polyuria']=1
Diabetes1.index.name='Diabetes'
Diabetes1

Gastroenteritis=training[training.prognosis=='Gastroenteritis']
Gastroenteritis=Gastroenteritis.describe()
mean_values = Gastroenteritis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Gastroenteritis = Gastroenteritis.drop(columns=columns_to_remove)
Gastroenteritis

Gastroenteritis1=table.copy()
Gastroenteritis1.at[0,'vomiting']=1
Gastroenteritis1.at[0,'sunken_eyes']=1
Gastroenteritis1.at[0,'dehydration']=1
Gastroenteritis1.at[0,'diarrhoea']=1
Gastroenteritis1.index.name='Gastroenteritis'
Gastroenteritis1

Bronchial_Asthma=training[training.prognosis=='Bronchial Asthma']
Bronchial_Asthma=Bronchial_Asthma.describe()
mean_values = Bronchial_Asthma.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Bronchial_Asthma = Bronchial_Asthma.drop(columns=columns_to_remove)
Bronchial_Asthma

Bronchial_Asthma1=table.copy()
Bronchial_Asthma1.at[0,'fatigue']=1
Bronchial_Asthma1.at[0,'cough']=1
Bronchial_Asthma1.at[0,'high_fever']=1
Bronchial_Asthma1.at[0,'family_history']=1
Bronchial_Asthma1.at[0,'mucoid_sputum']=1
Bronchial_Asthma1.index.name='Bronchial_Asthma'
Bronchial_Asthma1

Hypertension=training[training.prognosis=='Hypertension ']
Hypertension=Hypertension.describe()
mean_values = Hypertension.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Hypertension = Hypertension.drop(columns=columns_to_remove)
Hypertension

Hypertension1=table.copy()
Hypertension1.at[0,'headache']=1
Hypertension1.at[0,'chest_pain']=1
Hypertension1.at[0,'dizziness']=1
Hypertension1.at[0,'loss_of_balance']=1
Hypertension1.at[0,'lack_of_concentration']=1
Hypertension1.index.name='Hypertension'
Hypertension1

Migraine=training[training.prognosis=='Migraine']
Migraine=Migraine.describe()
mean_values = Migraine.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Migraine = Migraine.drop(columns=columns_to_remove)
Migraine

Migraine1=table.copy()
Migraine1.at[0,'visual_disturbances']=1
Migraine1.at[0,'irritability']=1
Migraine1.at[0,'depression']=1
Migraine1.at[0,'stiff_neck']=1
Migraine1.at[0,'acidity']=1
Migraine1.at[0,'indigestion']=1
Migraine1.at[0,'headache']=1
Migraine1.at[0,'blurred_and_distorted_vision']=1
Migraine1.at[0,'excessive_hunger']=1
Migraine1.index.name='Migraine'
Migraine1

Cervical_spondylosis=training[training.prognosis=='Cervical spondylosis']
Cervical_spondylosis=Cervical_spondylosis.describe()
mean_values = Cervical_spondylosis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Cervical_spondylosis = Cervical_spondylosis.drop(columns=columns_to_remove)
Cervical_spondylosis

Cervical_spondylosis1=table.copy()
Cervical_spondylosis1.at[0,'back_pain']=1
Cervical_spondylosis1.at[0,'weakness_in_limbs']=1
Cervical_spondylosis1.at[0,'neck_pain']=1
Cervical_spondylosis1.at[0,'dizziness']=1
Cervical_spondylosis1.at[0,'loss_of_balance']=1
Cervical_spondylosis1.index.name='Cervical_spondylosis'
Cervical_spondylosis1

Paralysis=training[training.prognosis=='Paralysis (brain hemorrhage)']
Paralysis=Paralysis.describe()
mean_values = Paralysis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Paralysis = Paralysis.drop(columns=columns_to_remove)
Paralysis

Paralysis1=table.copy()
Paralysis1.at[0,'vomiting']=1
Paralysis1.at[0,'headache']=1
Paralysis1.at[0,'weakness_of_one_body_side']=1
Paralysis1.at[0,'altered_sensorium']=1
Paralysis1.index.name='Paralysis (brain hemorrhage)'
Paralysis1

Jaundice=training[training.prognosis=='Jaundice']
Jaundice=Jaundice.describe()
mean_values = Jaundice.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Jaundice = Jaundice.drop(columns=columns_to_remove)
Jaundice

Jaundice1=table.copy()
Jaundice1.at[0,'abdominal_pain']=1
Jaundice1.at[0,'dark_urine']=1
Jaundice1.at[0,'yellowish_skin']=1
Jaundice1.at[0,'high_fever']=1
Jaundice1.at[0,'vomiting']=1
Jaundice1.at[0,'itching']=1
Jaundice1.at[0,'fatigue']=1
Jaundice1.at[0,'weight_loss']=1
Jaundice1.index.name='Jaundice'
Jaundice1

Malaria=training[training.prognosis=='Malaria']
Malaria=Malaria.describe()
mean_values = Malaria.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Malaria = Malaria.drop(columns=columns_to_remove)
Malaria

Malaria1=table.copy()
Malaria1.at[0,'chills']=1
Malaria1.at[0,'vomiting']=1
Malaria1.at[0,'sweating']=1
Malaria1.at[0,'high_fever']=1
Malaria1.at[0,'headache']=1
Malaria1.at[0,'nausea']=1
Malaria1.at[0,'muscle_pain']=1
Malaria1.at[0,'diarrhoea']=1
Malaria1.index.name='Malaria'
Malaria1

Chicken_pox=training[training.prognosis=='Chicken pox']
Chicken_pox=Chicken_pox.describe()
mean_values = Chicken_pox.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Chicken_pox = Chicken_pox.drop(columns=columns_to_remove)
Chicken_pox

Chicken_pox1=table.copy()
Chicken_pox1.at[0,'swelled_lymph_nodes']=1
Chicken_pox1.at[0,'malaise']=1
Chicken_pox1.at[0,'red_spots_over_body']=1
Chicken_pox1.at[0,'itching']=1
Chicken_pox1.at[0,'skin_rash']=1
Chicken_pox1.at[0,'fatigue']=1
Chicken_pox1.at[0,'lethargy']=1
Chicken_pox1.at[0,'high_fever']=1
Chicken_pox1.at[0,'headache']=1
Chicken_pox1.at[0,'loss_of_appetite']=1
Chicken_pox1.at[0,'mild_fever']=1
Chicken_pox1.index.name='Chicken_pox'
Chicken_pox1

Dengue=training[training.prognosis=='Dengue']
Dengue=Dengue.describe()
mean_values = Dengue.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Dengue = Dengue.drop(columns=columns_to_remove)
Dengue

Dengue1=table.copy()
Dengue1.at[0,'red_spots_over_body']=1
Dengue1.at[0,'muscle_pain']=1
Dengue1.at[0,'malaise']=1
Dengue1.at[0,'skin_rash']=1
Dengue1.at[0,'chills']=1
Dengue1.at[0,'joint_pain']=1
Dengue1.at[0,'vomiting']=1
Dengue1.at[0,'high_fever']=1
Dengue1.at[0,'fatigue']=1
Dengue1.at[0,'headache']=1
Dengue1.at[0,'nausea']=1
Dengue1.at[0,'loss_of_appetite']=1
Dengue1.at[0,'pain_behind_the_eyes']=1
Dengue1.at[0,'back_pain']=1
Dengue1.index.name='Dengue'
Dengue1

Typhoid=training[training.prognosis=='Typhoid']
Typhoid=Typhoid.describe()
mean_values = Typhoid.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Typhoid = Typhoid.drop(columns=columns_to_remove)
Typhoid

Typhoid1=table.copy()
Typhoid1.at[0,'chills']=1
Typhoid1.at[0,'vomiting']=1
Typhoid1.at[0,'fatigue']=1
Typhoid1.at[0,'high_fever']=1
Typhoid1.at[0,'headache']=1
Typhoid1.at[0,'nausea']=1
Typhoid1.at[0,'constipation']=1
Typhoid1.at[0,'abdominal_pain']=1
Typhoid1.at[0,'diarrhoea']=1
Typhoid1.at[0,'toxic_look_(typhos)']=1
Typhoid1.at[0,'belly_pain']=1
Typhoid1.index.name='Typhoid'
Typhoid1

hepatitisA=training[training.prognosis=='hepatitis A']
hepatitisA=hepatitisA.describe()
mean_values = hepatitisA.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
hepatitisA = hepatitisA.drop(columns=columns_to_remove)
hepatitisA

hepatitisA1=table.copy()
hepatitisA1.at[0,'joint_pain']=1
hepatitisA1.at[0,'vomiting']=1
hepatitisA1.at[0,'yellowish_skin']=1
hepatitisA1.at[0,'dark_urine']=1
hepatitisA1.at[0,'nausea']=1
hepatitisA1.at[0,'loss_of_appetite']=1
hepatitisA1.at[0,'abdominal_pain']=1
hepatitisA1.at[0,'diarrhoea']=1
hepatitisA1.at[0,'mild_fever']=1
hepatitisA1.at[0,'yellowing_of_eyes']=1
hepatitisA1.at[0,'belly_pain']=1
hepatitisA1.index.name='hepatitis A'
hepatitisA1

HepatitisB=training[training.prognosis=='Hepatitis B']
HepatitisB=HepatitisB.describe()
mean_values = HepatitisB.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
HepatitisB = HepatitisB.drop(columns=columns_to_remove)
HepatitisB

HepatitisB1=table.copy()
HepatitisB1.at[0,'receiving_unsterile_injections']=1
HepatitisB1.at[0,'itching']=1
HepatitisB1.at[0,'fatigue']=1
HepatitisB1.at[0,'lethargy']=1
HepatitisB1.at[0,'yellowish_skin']=1
HepatitisB1.at[0,'dark_urine']=1
HepatitisB1.at[0,'loss_of_appetite']=1
HepatitisB1.at[0,'abdominal_pain']=1
HepatitisB1.at[0,'yellow_urine']=1
HepatitisB1.at[0,'yellowing_of_eyes']=1
HepatitisB1.at[0,'malaise']=1
HepatitisB1.at[0,'receiving_blood_transfusion']=1
HepatitisB1.index.name='Hepatitis B'
HepatitisB1

HepatitisC=training[training.prognosis=='Hepatitis C']
HepatitisC=HepatitisC.describe()
mean_values = HepatitisC.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
HepatitisC = HepatitisC.drop(columns=columns_to_remove)
HepatitisC

HepatitisC1=table.copy()
HepatitisC1.at[0,'fatigue']=1
HepatitisC1.at[0,'yellowish_skin']=1
HepatitisC1.at[0,'nausea']=1
HepatitisC1.at[0,'loss_of_appetite']=1
HepatitisC1.at[0,'yellowing_of_eyes']=1
HepatitisC1.at[0,'family_history']=1
HepatitisC1.index.name='Hepatitis C'
HepatitisC1

HepatitisD=training[training.prognosis=='Hepatitis D']
HepatitisD=HepatitisD.describe()
mean_values = HepatitisD.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
HepatitisD = HepatitisD.drop(columns=columns_to_remove)
HepatitisD

HepatitisD1=table.copy()
HepatitisD1.at[0,'loss_of_appetite']=1
HepatitisD1.at[0,'abdominal_pain']=1
HepatitisD1.at[0,'yellowing_of_eyes']=1
HepatitisD1.at[0,'fatigue']=1
HepatitisD1.at[0,'joint_pain']=1
HepatitisD1.at[0,'vomiting']=1
HepatitisD1.at[0,'yellowish_skin']=1
HepatitisD1.at[0,'dark_urine']=1
HepatitisD1.at[0,'nausea']=1
HepatitisD1.index.name='Hepatitis D'
HepatitisD1

HepatitisE=training[training.prognosis=='Hepatitis E']
HepatitisE=HepatitisE.describe()
mean_values = HepatitisE.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
HepatitisE = HepatitisE.drop(columns=columns_to_remove)
HepatitisE

HepatitisE1=table.copy()
HepatitisE1.at[0,'stomach_bleeding']=1
HepatitisE1.at[0,'yellowing_of_eyes']=1
HepatitisE1.at[0,'acute_liver_failure']=1
HepatitisE1.at[0,'coma']=1
HepatitisE1.at[0,'dark_urine']=1
HepatitisE1.at[0,'yellowish_skin']=1
HepatitisE1.at[0,'high_fever']=1
HepatitisE1.at[0,'fatigue']=1
HepatitisE1.at[0,'joint_pain']=1
HepatitisE1.at[0,'vomiting']=1
HepatitisE1.at[0,'nausea']=1
HepatitisE1.at[0,'loss_of_appetite']=1
HepatitisE1.at[0,'abdominal_pain']=1
HepatitisE1.index.name='Hepatitis E'
HepatitisE1

Alcoholic_hepatitis=training[training.prognosis=='Alcoholic hepatitis']
Alcoholic_hepatitis=Alcoholic_hepatitis.describe()
mean_values = Alcoholic_hepatitis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Alcoholic_hepatitis = Alcoholic_hepatitis.drop(columns=columns_to_remove)
Alcoholic_hepatitis

Alcoholic_hepatitis1=table.copy()
Alcoholic_hepatitis1.at[0,'vomiting']=1
Alcoholic_hepatitis1.at[0,'yellowish_skin']=1
Alcoholic_hepatitis1.at[0,'abdominal_pain']=1
Alcoholic_hepatitis1.at[0,'swelling_of_stomach']=1
Alcoholic_hepatitis1.at[0,'distention_of_abdomen']=1
Alcoholic_hepatitis1.at[0,'history_of_alcohol_consumption']=1
Alcoholic_hepatitis1.at[0,'fluid_overload']=1
Alcoholic_hepatitis1.index.name='Alcoholic hepatitis'
Alcoholic_hepatitis1

Tuberculosis=training[training.prognosis=='Tuberculosis']
Tuberculosis=Tuberculosis.describe()
mean_values = Tuberculosis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Tuberculosis = Tuberculosis.drop(columns=columns_to_remove)
Tuberculosis

Tuberculosis1=table.copy()
Tuberculosis1.at[0,'blood_in_sputum']=1
Tuberculosis1.at[0,'chest_pain']=1
Tuberculosis1.at[0,'phlegm']=1
Tuberculosis1.at[0,'malaise']=1
Tuberculosis1.at[0,'sweating']=1
Tuberculosis1.at[0,'loss_of_appetite']=1
Tuberculosis1.at[0,'mild_fever']=1
Tuberculosis1.at[0,'yellowing_of_eyes']=1
Tuberculosis1.at[0,'swelled_lymph_nodes']=1
Tuberculosis1.at[0,'vomiting']=1
Tuberculosis1.at[0,'chills']=1
Tuberculosis1.at[0,'fatigue']=1
Tuberculosis1.at[0,'weight_loss']=1
Tuberculosis1.at[0,'cough']=1
Tuberculosis1.at[0,'high_fever']=1
Tuberculosis1.at[0,'breathlessness']=1
Tuberculosis1.index.name='Tuberculosis'
Tuberculosis1

Common_Cold=training[training.prognosis=='Common Cold']
Common_Cold=Common_Cold.describe()
mean_values = Common_Cold.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Common_Cold = Common_Cold.drop(columns=columns_to_remove)
Common_Cold

Common_Cold1=table.copy()
Common_Cold1.at[0,'loss_of_smell']=1
Common_Cold1.at[0,'muscle_pain']=1
Common_Cold1.at[0,'chest_pain']=1
Common_Cold1.at[0,'continous_sneezing']=1
Common_Cold1.at[0,'chills']=1
Common_Cold1.at[0,'fatigue']=1
Common_Cold1.at[0,'cough']=1
Common_Cold1.at[0,'high_fever']=1
Common_Cold1.at[0,'headache']=1
Common_Cold1.at[0,'swelled_lymph_nodes']=1
Common_Cold1.at[0,'yellowing_of_eyes']=1
Common_Cold1.at[0,'swelled_lymph_nodes']=1
Common_Cold1.at[0,'malaise']=1
Common_Cold1.at[0,'phlegm']=1
Common_Cold1.at[0,'throat_irritation']=1
Common_Cold1.at[0,'redness_of_eyes']=1
Common_Cold1.at[0,'sinus_pressure']=1
Common_Cold1.at[0,'runny_nose']=1
Common_Cold1.at[0,'congestion']=1
Common_Cold1.index.name='Common Cold'
Common_Cold1

Pneumonia=training[training.prognosis=='Pneumonia']
Pneumonia=Pneumonia.describe()
mean_values = Pneumonia.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Pneumonia = Pneumonia.drop(columns=columns_to_remove)
Pneumonia

Pneumonia1=table.copy()
Pneumonia1.at[0,'chills']=1
Pneumonia1.at[0,'fatigue']=1
Pneumonia1.at[0,'cough']=1
Pneumonia1.at[0,'high_fever']=1
Pneumonia1.at[0,'breathlessness']=1
Pneumonia1.at[0,'sweating']=1
Pneumonia1.at[0,'malaise']=1
Pneumonia1.at[0,'phlegm']=1
Pneumonia1.at[0,'chest_pain']=1
Pneumonia1.at[0,'fast_heart_rate']=1
Pneumonia1.at[0,'rusty_sputum']=1
Pneumonia1.index.name='Pneumonia'
Pneumonia1

Dimorphic=training[training.prognosis=='Dimorphic hemmorhoids(piles)']
Dimorphic=Dimorphic.describe()
mean_values = Dimorphic.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Dimorphic = Dimorphic.drop(columns=columns_to_remove)
Dimorphic

Dimorphic1=table.copy()
Dimorphic1.at[0,'constipation']=1
Dimorphic1.at[0,'pain_during_bowel_movements']=1
Dimorphic1.at[0,'pain_in_anal_region']=1
Dimorphic1.at[0,'bloody_stool']=1
Dimorphic1.at[0,'irritation_in_anus']=1
Dimorphic1.index.name='Dimorphic'
Dimorphic1

Heart_attack=training[training.prognosis=='Heart attack']
Heart_attack=Heart_attack.describe()
mean_values = Heart_attack.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Heart_attack = Heart_attack.drop(columns=columns_to_remove)
Heart_attack

Heart_attack1=table.copy()
Heart_attack1.at[0,'vomiting']=1
Heart_attack1.at[0,'breathlessness']=1
Heart_attack1.at[0,'sweating']=1
Heart_attack1.at[0,'chest_pain']=1
Heart_attack1.index.name='Heart attack'
Heart_attack1

Hypothyroidism=training[training.prognosis=='Hypothyroidism']
Hypothyroidism=Hypothyroidism.describe()
mean_values = Hypothyroidism.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Hypothyroidism = Hypothyroidism.drop(columns=columns_to_remove)
Hypothyroidism

Hypothyroidism1=table.copy()
Hypothyroidism1.at[0,'enlarged_thyroid']=1
Hypothyroidism1.at[0,'brittle_nails']=1
Hypothyroidism1.at[0,'swollen_extremeties']=1
Hypothyroidism1.at[0,'depression']=1
Hypothyroidism1.at[0,'irritability']=1
Hypothyroidism1.at[0,'abnormal_menstruation']=1
Hypothyroidism1.at[0,'lethargy']=1
Hypothyroidism1.at[0,'dizziness']=1
Hypothyroidism1.at[0,'puffy_face_and_eyes']=1
Hypothyroidism1.at[0,'fatigue']=1
Hypothyroidism1.at[0,'weight_gain']=1
Hypothyroidism1.at[0,'cold_hands_and_feets']=1
Hypothyroidism1.at[0,'mood_swings']=1
Hypothyroidism1.index.name='Hypothyroidism'
Hypothyroidism1

Hyperthyroidism=training[training.prognosis=='Hyperthyroidism']
Hyperthyroidism=Hyperthyroidism.describe()
mean_values = Hyperthyroidism.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Hyperthyroidism = Hyperthyroidism.drop(columns=columns_to_remove)
Hyperthyroidism

Hyperthyroidism1=table.copy()
Hyperthyroidism1.at[0,'fatigue']=1
Hyperthyroidism1.at[0,'mood_swings']=1
Hyperthyroidism1.at[0,'weight_loss']=1
Hyperthyroidism1.at[0,'restlesness']=1
Hyperthyroidism1.at[0,'sweating']=1
Hyperthyroidism1.at[0,'diarrhoea']=1
Hyperthyroidism1.at[0,'fast_heart_rate']=1
Hyperthyroidism1.at[0,'excessive_hunger']=1
Hyperthyroidism1.at[0,'muscle_weakness']=1
Hyperthyroidism1.at[0,'irritability']=1
Hyperthyroidism1.at[0,'abnormal_menstruation']=1
Hyperthyroidism1.index.name='Hyperthyroidism'
Hyperthyroidism1

Hypoglycemia=training[training.prognosis=='Hypoglycemia']
Hypoglycemia=Hypoglycemia.describe()
mean_values = Hypoglycemia.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Hypoglycemia = Hypoglycemia.drop(columns=columns_to_remove)
Hypoglycemia

Hypoglycemia1=table.copy()
Hypoglycemia1.at[0,'palpitations']=1
Hypoglycemia1.at[0,'fatigue']=1
Hypoglycemia1.at[0,'vomiting']=1
Hypoglycemia1.at[0,'anxiety']=1
Hypoglycemia1.at[0,'headache']=1
Hypoglycemia1.at[0,'sweating']=1
Hypoglycemia1.at[0,'nausea']=1
Hypoglycemia1.at[0,'blurred_and_distorted_vision']=1
Hypoglycemia1.at[0,'excessive_hunger']=1
Hypoglycemia1.at[0,'drying_and_tingling_lips']=1
Hypoglycemia1.at[0,'slurred_speech']=1
Hypoglycemia1.at[0,'irritability']=1
Hypoglycemia1.index.name='Hypoglycemia'
Hypoglycemia1

Osteoarthristis=training[training.prognosis=='Osteoarthristis']
Osteoarthristis=Osteoarthristis.describe()
mean_values = Osteoarthristis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Osteoarthristis = Osteoarthristis.drop(columns=columns_to_remove)
Osteoarthristis

Osteoarthristis1=table.copy()
Osteoarthristis1.at[0,'joint_pain']=1
Osteoarthristis1.at[0,'neck_pain']=1
Osteoarthristis1.at[0,'knee_pain']=1
Osteoarthristis1.at[0,'hip_joint_pain']=1
Osteoarthristis1.at[0,'swelling_joints']=1
Osteoarthristis1.at[0,'painful_walking']=1
Osteoarthristis1.index.name='Osteoarthristis'
Osteoarthristis1

Arthritis=training[training.prognosis=='Arthritis']
Arthritis=Arthritis.describe()
mean_values = Arthritis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Arthritis = Arthritis.drop(columns=columns_to_remove)
Arthritis

Arthritis1=table.copy()
Arthritis1.at[0,'muscle_weakness']=1
Arthritis1.at[0,'stiff_neck']=1
Arthritis1.at[0,'swelling_joints']=1
Arthritis1.at[0,'movement_stiffness']=1
Arthritis1.at[0,'painful_walking']=1
Arthritis1.index.name='Arthritis'
Arthritis1

vertigo=training[training.prognosis=='(vertigo) Paroymsal  Positional Vertigo']
vertigo=vertigo.describe()
mean_values = vertigo.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
vertigo = vertigo.drop(columns=columns_to_remove)
vertigo

vertigo1=table.copy()
vertigo1.at[0,'unsteadiness']=1
vertigo1.at[0,'vomiting']=1
vertigo1.at[0,'headache']=1
vertigo1.at[0,'nausea']=1
vertigo1.at[0,'spinning_movements']=1
vertigo1.at[0,'loss_of_balance']=1
vertigo1.index.name='vertigo'
vertigo1

Acne=training[training.prognosis=='Acne']
Acne=Acne.describe()
mean_values = Acne.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Acne = Acne.drop(columns=columns_to_remove)
Acne

Acne1=table.copy()
Acne1.at[0,'skin_rash']=1
Acne1.at[0,'pus_filled_pimples']=1
Acne1.at[0,'blackheads']=1
Acne1.at[0,'scurring']=1
Acne1.index.name='Acne'
Acne1

Urinary_tract_infection=training[training.prognosis=='Urinary tract infection']
Urinary_tract_infection=Urinary_tract_infection.describe()
mean_values = Urinary_tract_infection.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Urinary_tract_infection = Urinary_tract_infection.drop(columns=columns_to_remove)
Urinary_tract_infection

Urinary_tract_infection1=table.copy()
Urinary_tract_infection1.at[0,'burning_micturition']=1
Urinary_tract_infection1.at[0,'bladder_discomfort']=1
Urinary_tract_infection1.at[0,'foul_smell_of urine']=1
Urinary_tract_infection1.at[0,'continuous_feel_of_urine']=1
Urinary_tract_infection1.index.name='Urinary tract infection'
Urinary_tract_infection1

Psoriasis=training[training.prognosis=='Psoriasis']
Psoriasis=Psoriasis.describe()
mean_values = Psoriasis.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Psoriasis = Psoriasis.drop(columns=columns_to_remove)
Psoriasis

Psoriasis1=table.copy()
Psoriasis1.at[0,'small_dents_in_nails']=1
Psoriasis1.at[0,'inflammatory_nails']=1
Psoriasis1.at[0,'skin_rash']=1
Psoriasis1.at[0,'joint_pain']=1
Psoriasis1.at[0,'skin_peeling']=1
Psoriasis1.at[0,'silver_like_dusting']=1
Psoriasis1.index.name='Psoriasis'
Psoriasis1

Impetigo=training[training.prognosis=='Impetigo']
Impetigo=Impetigo.describe()
mean_values = Impetigo.loc['mean']
columns_to_remove = mean_values[mean_values == 0].index
Impetigo = Impetigo.drop(columns=columns_to_remove)
Impetigo

Impetigo1=table.copy()
Impetigo1.at[0,'skin_rash']=1
Impetigo1.at[0,'high_fever']=1
Impetigo1.at[0,'blister']=1
Impetigo1.at[0,'red_sore_around_nose']=1
Impetigo1.at[0,'yellow_crust_ooze']=1
Impetigo1.index.name='Impetigo'
Impetigo1

test=pd.concat([fungal_infection1, Allergy1, GERD1,Chronic_cholestasis1, Drug_Reaction1,Peptic_ulcer_diseae1, AIDS1,Diabetes1,Gastroenteritis1,Bronchial_Asthma1,Hypertension1, Migraine1, Cervical_spondylosis1, Paralysis1,Jaundice1
, Malaria1,Chicken_pox1,Dengue1,Typhoid1,hepatitisA1,HepatitisB1, HepatitisC1, HepatitisD1, HepatitisE1, Alcoholic_hepatitis1,Tuberculosis1, Common_Cold1, Pneumonia1,Dimorphic1,Heart_attack1,Hypothyroidism1
, Hyperthyroidism1,Hypoglycemia1,Osteoarthristis1,Arthritis1, vertigo1,Acne1,Urinary_tract_infection1,Psoriasis1,Impetigo1])
test.index = ['fungal_infection'] * len(fungal_infection1) + ['Allergy'] * len(Allergy1) + ['GERD'] * len(GERD1) + ['Chronic_cholestasis'] *len(Chronic_cholestasis1)+['Drug_Reaction']*len(Drug_Reaction1)+['Peptic_ulcer_diseae']*len(Peptic_ulcer_diseae1)+ ['AIDS']*len(AIDS1)+['Diabetes']*len(Diabetes1) +['Gastroenteritis']*len(Gastroenteritis1)+['Bronchial_Asthma']*len(Bronchial_Asthma1) + ['Hypertension']*len(Hypertension1)+['Migraine']*len(Migraine1)+['Cervical_spondylosis']*len(Cervical_spondylosis1)+['Paralysis']*len(Paralysis1)+['Jaundice']*len(Jaundice1)+['Malaria']*len(Malaria1)+['Chicken_pox']*len(Chicken_pox1)+['Dengue']*len(Dengue1)+['Typhoid']*len(Typhoid1)+['hepatitis A']*len(hepatitisA1)+['hepatitis B']*len(HepatitisB1)+['Hepatitis C']*len(HepatitisC1)+['Hepatitis D']*len(HepatitisD1)+['Hepatitis E']*len(HepatitisE1)+['Alcoholic_hepatitis']*len(Alcoholic_hepatitis1)+['Tuberculosis']*len(Tuberculosis1)+['Common_Cold']*len(Common_Cold1)+['Pneumonia']*len(Pneumonia1)+['Dimorphic']*len(Dimorphic1)+['Heart_attack']*len(Heart_attack1)+['Hypothyroidism']*len(Hypothyroidism1)+['Hyperthyroidism']*len(Hyperthyroidism1)+['Hypoglycemia']*len(Hypoglycemia1)+['Osteoarthristis']*len(Osteoarthristis1)+['Arthritis']*len(Arthritis1)+['vertigo']*len(vertigo1)+['Acne']*len(Acne1)+['Urinary_tract_infection']*len(Urinary_tract_infection1)+['Psoriasis']*len(Psoriasis1)+['Impetigo']*len(Impetigo1)
test

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import psycopg2
import seaborn as sbn
from altair import Chart, X, Y, Color, Scale
import altair as alt
from vega_datasets import data
import requests
from bs4 import BeautifulSoup
matplotlib.style.use('ggplot')
new_table=pd.read_csv('new_table.csv')
new_table.head()