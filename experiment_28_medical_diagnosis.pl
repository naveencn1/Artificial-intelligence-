% CSA17 - Artificial Intelligence | Experiment 28 (Manual Ex. 3.8): Prolog: Medical Diagnosis
% Name            : V V Naveen Kumar
% Register Number : 192321018

symptom(ravi, fever). symptom(ravi, cough). symptom(ravi, body_pain).
symptom(meena, sneezing). symptom(meena, runny_nose). symptom(meena, sore_throat).
symptom(kumar, fever). symptom(kumar, chills). symptom(kumar, sweating).
symptom(kumar, headache).

disease(flu, [fever, cough, body_pain]).
disease(common_cold, [sneezing, runny_nose, sore_throat]).
disease(malaria, [fever, chills, sweating]).
disease(typhoid, [fever, headache, stomach_pain]).

advice(flu, 'rest, fluids and consult a doctor if fever persists').
advice(common_cold, 'rest, warm fluids and steam inhalation').
advice(malaria, 'consult a doctor immediately for a blood test').
advice(typhoid, 'consult a doctor immediately for a Widal test').

has_all(_, []).
has_all(P, [S|T]) :- symptom(P, S), has_all(P, T).

diagnose(P, D) :- disease(D, Symptoms), has_all(P, Symptoms).
report(P) :- diagnose(P, D), advice(D, A), format('~w may have ~w. Advice: ~w~n', [P, D, A]).
