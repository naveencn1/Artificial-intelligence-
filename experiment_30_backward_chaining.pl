% CSA17 - Artificial Intelligence | Experiment 30 (Manual Ex. 3.10): Prolog: Backward Chaining
% Name            : V V Naveen Kumar
% Register Number : 192321018

fact(has_hair).
fact(eats_meat).
fact(tawny_colour).
fact(black_stripes).

rule(r1, [has_hair], mammal).
rule(r2, [gives_milk], mammal).
rule(r3, [mammal, eats_meat], carnivore).
rule(r4, [carnivore, tawny_colour, dark_spots], cheetah).
rule(r5, [carnivore, tawny_colour, black_stripes], tiger).

bc(Goal) :- fact(Goal).
bc(Goal) :- rule(_, Conditions, Goal), bc_all(Conditions).

bc_all([]).
bc_all([G|Rest]) :- bc(G), bc_all(Rest).

% version that prints the reasoning
prove(Goal, Depth) :-
  tab(Depth), format('Proving ~w~n', [Goal]),
  ( fact(Goal)
  -> tab(Depth), format(' ~w is a known fact~n', [Goal])
  ; rule(Id, Conditions, Goal),
    tab(Depth), format(' using rule ~w~n', [Id]),
    D1 is Depth + 2,
    prove_all(Conditions, D1),
    !
  ).

prove_all([], _).
prove_all([G|Rest], D) :- prove(G, D), prove_all(Rest, D).


/* ============================================================
   OUTPUT (queries and answers)
   ============================================================
?- bc(tiger).
true.

?- bc(cheetah).
false.

?- bc(mammal).
true.

?- prove(tiger, 0).
Proving tiger
 using rule r5
  Proving carnivore
   using rule r3
    Proving mammal
     using rule r1
      Proving has_hair
       has_hair is a known fact
    Proving eats_meat
     eats_meat is a known fact
  Proving tawny_colour
   tawny_colour is a known fact
  Proving black_stripes
   black_stripes is a known fact
true.
*/
