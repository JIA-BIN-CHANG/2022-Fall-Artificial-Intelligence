/*
Assignment 5 Blocks World Problem

Dieudonne Muhirwa M14185704
Allen Detmer M15216736
JiaBin Chang M13782945
Joseph Matawaran M15228497
*/

% predicate which lists all the blocks and table in your world
blocks([a, b, c, d]).
table("table").

% block, say X, is a member of the list of block
block(X):-
	blocks(BLOCKS),  % this extracts the list BLOCKS
	member(X, BLOCKS).

% move block X to be on block Z
move(X, Y, Z, S1, S2):-
	member([clear, X], S1), %find a clear block X in S1
	member([on, X, Y], S1), block(Y), %find a block on which X sits
	member([clear, Z], S1), notequal(X, Z), %find another clear block, Z
	substitute([on, X, Y], [on, X, Z], S1, INT), %remove X from Y, place it on Z
	substitute([clear, Z], [clear, Y], INT, S2). %Z is no longer clear; Y is now clear

% move block X from table Y to be on block Z
moveTableBlock(X, Y, Z, S1, S2):-%from table to block
	member([clear, X], S1), %find a clear block X in S1
	member([on, X, Y], S1), table(Y),%find a block X which sits on table
	member([clear, Z], S1), notequal(X, Z), %find another clear block, Z
	substitute([on, X, Y], [on, X, Z], S1, INT), %remove X from Y, place it on Z
	delete([clear, Z], INT, S2). %Z is no longer clear; remove from list
	
% move block X from block Y to be on table Z
moveBlockTable(X, Y, Z, S1, [[clear, Y]|INT]):-%form block to table
	member([clear, X], S1), %find a clear block X in S1
	member([on, X, Y], S1), block(Y), table(Z),%find a block on which X sits
	substitute([on, X, Y], [on, X, Z], S1, INT).

%notequal(X1, X2) holds when X1 and X2 are not equal
notequal(X,X):-!, fail.
notequal(_, _).

% substitute(E, E1, OLD, NEW) holds when NEW is the list OLD in which E is substituted by E1.  There are no duplicates in OLD or NEW.
substitute(X, Y, [X|T1], [Y|T1]).
substitute(X, Y, [H|T], [H|T1]):- 
    substitute(X, Y, T, T1).

/*
path contains three conditions:
1.move block to block
2.move block from table to block
3.move block from block to table
*/
path(S1, S2):-
	move(_, _, _, S1, S2).

path(S1, S2):-
	moveTableBlock(_, "table", _, S1, S2).

path(S1, S2):-
	moveBlockTable(_, _, "table", S1, S2).

%delete(E, OLD, NEW)
delete( H, [H|T], T).
delete( E, [H|T], [H|T1]):-
    delete( E, T, T1).

% permutation here is a default predicate. It deletes the head of list and return the shorter list to itself
nyv(X, L):- member(X,L),!,fail.  % if X is a member, it has already been visited, and hence nye fails
nyv(X,L):- permutation(X,XP), member(XP,L),!,fail. % same for any permutation of X
nyv(_,_). % otherwise it succeeds

%dfs(State, Path, PathSoFar): returns the Path from the start to the goal states.
% Trivial: if X is the goal return X as the path from X to X, also check it's permutation.
dfs(X, [X],_):- goal(Y), permutation(X,Y).

% else expand X by Y and find path from Y
dfs(X, [X|Ypath], VISITED):-
 	path(X, Y),
  	nyv(Y, VISITED),
  	dfs(Y, Ypath, [Y|VISITED]), !.

% Test case 1 - valid start state with goal state in a different sequence in the array
%start([[on, b, a], [clear, b], [on, a, "table"]]).
%goal([[on, b, a], [on, a, "table"], [clear, b]]).

% Test case 2 - 2 block problem
%start([[on, a, "table"], [on, b, "table"], [clear, a], [clear, b]]).
%goal([[on, b, a], [on, a, "table"], [clear, b]]).

% Test case 3 - 3 block problem
%start([[on, c, a], [on, a, "table"], [on, b, "table"], [clear, c], [clear, b]]).
%goal([[on, c, b], [on, b, a], [on, a, "table"], [clear, c]]).

% Test case 4 - 4 block problem
start([[on, a, b],[on, b, "table"], [on, c, d], [clear, c], [clear, a], [on, d, "table"]]).
goal([[on, d, a], [on, a, c], [on, c, b], [on, b, "table"], [clear, d]]).

% Run the code by typing the following command:
%start(S), dfs(S, P, [S]).