% CSA17 - Artificial Intelligence | Experiment 29 (Manual Ex. 3.9): Prolog: Forward Chaining
% Name            : V V Naveen Kumar
% Register Number : 192321018

:- dynamic fact/1.

fact(has_hair).
fact(eats_meat).
fact(tawny_colour).
fact(dark_spots).

rule(r1, [has_hair], mammal).
rule(r2, [gives_milk], mammal).
rule(r3, [mammal, eats_meat], carnivore).
rule(r4, [carnivore, tawny_colour, dark_spots], cheetah).
rule(r5, [carnivore, tawny_colour, black_stripes], tiger).

forward :-
  rule(Id, Conditions, Conclusion),
  \+ fact(Conclusion),
  forall(member(C, Conditions), fact(C)),
  !,
  assertz(fact(Conclusion)),
  format('Rule ~w fired: derived ~w~n', [Id, Conclusion]),
  forward.
forward.


/* ============================================================
   OUTPUT (queries and answers)
   ============================================================
?- forward.
Rule r1 fired: derived mammal
Rule r3 fired: derived carnivore
Rule r4 fired: derived cheetah
true.

?- fact(cheetah).
true.

?- fact(tiger).
false.

?- findall(F, fact(F), L).
L = [has_hair,eats_meat,tawny_colour,dark_spots,mammal,carnivore,cheetah].
*/
