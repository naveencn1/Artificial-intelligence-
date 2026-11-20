% CSA17 - Artificial Intelligence | Experiment 26 (Manual Ex. 3.6): Prolog: Fruits and Colours using Backtracking
% Name            : V V Naveen Kumar
% Register Number : 192321018

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(cherry, red).
fruit_color(grapes, green).
fruit_color(guava, green).
fruit_color(lemon, yellow).
fruit_color(orange, orange).
fruit_color(strawberry, red).

same_colour(F1, F2) :- fruit_color(F1, C), fruit_color(F2, C), F1 @< F2.
all_of_colour(C, L) :- findall(F, fruit_color(F, C), L).
show_all :- forall(fruit_color(F, C), format('~w is ~w~n', [F, C])).


/* ============================================================
   OUTPUT (queries and answers)
   ============================================================
?- fruit_color(F, red).
F = apple ;
F = cherry ;
F = strawberry.

?- fruit_color(banana, C).
C = yellow.

?- same_colour(F1, F2).
F1 = apple,
F2 = cherry ;
F1 = apple,
F2 = strawberry ;
F1 = banana,
F2 = lemon ;
F1 = cherry,
F2 = strawberry ;
F1 = grapes,
F2 = guava.

?- all_of_colour(green, L).
L = [grapes,guava].

?- show_all.
apple is red
banana is yellow
cherry is red
grapes is green
guava is green
lemon is yellow
orange is orange
strawberry is red
true.
*/
