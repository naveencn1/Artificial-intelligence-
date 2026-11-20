% CSA17 - Artificial Intelligence | Experiment 24 (Manual Ex. 3.4): Prolog: Diet Suggestion System Based on Disease
% Name            : V V Naveen Kumar
% Register Number : 192321018

patient(ravi, diabetes).
patient(meena, hypertension).
patient(kumar, anaemia).
patient(divya, obesity).
patient(arun, diabetes).

diet(diabetes, 'whole grains, oats, green vegetables, pulses, nuts').
diet(hypertension, 'fruits, vegetables, low-fat dairy, banana, low-salt meals').
diet(anaemia, 'spinach, beetroot, dates, jaggery, pulses, citrus fruits').
diet(obesity, 'salads, sprouts, fibre-rich foods, plenty of water, fruits').

avoid(diabetes, 'sweets, sugary drinks, white rice in excess').
avoid(hypertension, 'pickles, papad, processed food, excess salt').
avoid(anaemia, 'tea or coffee immediately after meals').
avoid(obesity, 'fried food, fast food, sugary beverages').

suggest(P, Diet) :- patient(P, D), diet(D, Diet).
advice(P, Eat, Avoid) :- patient(P, D), diet(D, Eat), avoid(D, Avoid).
with_disease(D, P) :- patient(P, D).


/* ============================================================
   OUTPUT (queries and answers)
   ============================================================
?- suggest(ravi, D).
D = 'whole grains, oats, green vegetables, pulses, nuts'.

?- advice(meena, E, A).
E = 'fruits, vegetables, low-fat dairy, banana, low-salt meals',
A = 'pickles, papad, processed food, excess salt'.

?- with_disease(diabetes, P).
P = ravi ;
P = arun.

?- suggest(divya, D).
D = 'salads, sprouts, fibre-rich foods, plenty of water, fruits'.
*/
