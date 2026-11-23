% CSA17 - Artificial Intelligence | Experiment 25 (Manual Ex. 3.5): Prolog: Monkey and Banana Problem
% Name            : V V Naveen Kumar
% Register Number : 192321018

pos(atdoor).
pos(atwindow).
pos(middle).

% move(StateBefore, Action, StateAfter)
move(state(middle, onbox, middle, hasnot), grasp, state(middle, onbox, middle, has)).
move(state(P, onfloor, P, H), climb, state(P, onbox, P, H)).
move(state(P1, onfloor, P1, H), push(P1, P2), state(P2, onfloor, P2, H)) :-
  pos(P2), P1 \= P2.
move(state(P1, onfloor, B, H), walk(P1, P2), state(P2, onfloor, B, H)) :-
  pos(P2), P1 \= P2.

plan(state(_, _, _, has), []).
plan(S1, [Action|Rest]) :-
  move(S1, Action, S2),
  plan(S2, Rest).

solve(Start, Plan) :-
  length(Plan, _),
  plan(Start, Plan), !.
