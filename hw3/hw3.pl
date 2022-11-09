/*
Assignment 3 Sorting algorithms in Prolog

Dieudonne Muhirwa M14185704
Allen Detmer M15216736
JiaBin Chang M13782945
Joseph Matawaran M15228497
*/

:- dynamic(myList/1).


/* randomList is a predicate to generate a random list of a given number 
 * of elements to the list size N. Each element is a number between 1 and 100*/
randomList(0, []).
randomList(N,[NUMBER|T]) :-
    N1 is N-1,
	random(1, 100, NUMBER),
	randomList(N1, T).

/* Adds/updates the dynamic myList value temp as last clause in the predicate.
 * This allows for the same generated list to be ran against all sorts */
update_list(Temp) :-
    retractall(myList(_)),
    assertz(myList(Temp)),
    !.

/* generates the random list of 50 and adds it to the predicate for use 
 * by all the sorts */
:- randomList(50,L),
update_list(L).

/*swap the first two elements if they are not in order*/ 
 swap([X, Y|T], [Y, X | T]):- 
            Y < X. 
/*swap elements in the tail*/ 
 swap([H|T], [H|T1]):- 
              swap(T, T1). 


/* bubbleSort repeatedly steps through the input list L comparing
 * the current element with the one after it, 
 * swapping the elements is the values are not in the correct order.
 * Stop when no more swaps are done, thus the list L is sorted */
bubbleSort(L,SL):- 
            swap(L, L1), % at least one swap is needed 
             !, 
             bubbleSort(L1, SL). 
bubbleSort(L, L). % here, the list is already sorted


/* Utilizes recursive calls to separate and verify the remaining elements in the list 
 * after checking the first two elements
 * Indicates whether the list is arranged in ascending or descending order*/
ordered([]).
ordered([_X]).
ordered([H1, H2|T]):-
    H1 =< H2, 
    ordered([H2|T]).

/* This ensures that the list is ordered in ascending order 
 * added this line for insertion sort*/
ascending(X,Y):- X=<Y. 

/* The program below make sure that the list is sorted correctly, 
 * the predicate describes the insertion of element E to the list*/

/* If E is smaller and X is being added into an empty list, 
 * then return a list that contains X*/
insert(X, [],[X]). 
insert(E, [H|T], [E,H|T]):- 
      ordered(T),
      ascending(E, H), 
                     !. 
                     
/* If the list's tail is sorted, add E to T,
 * add the H to the new T1, and then return the result
 * This ensures that the list is ordered*/

insert(E, [H|T], [H|T1]):- 
      ordered(T),
      insert(E, T, T1). 
      

/* utilizes insertion sort,
 * which sorts a list by repeatedly dividing it into sorted and unsorted portions.
 * it maintain a sorted list and iteratively it take one element from the unsorted list
 * and it insert it in the correct position in the sorted list.
 * by splitting it.*/
insertionSort([], []). 
insertionSort([H|T], SORTED) :- 
          insertionSort(T, T1), 
          insert(H, T1, SORTED). 

/* Split the list into half until all of the sublist has only one item
 * Compare every two sublists and merge them in increasing order 
 * Merge all the sublist as the final sorted list*/
mergeSort([], []).    %the empty list is sorted 
mergeSort([X], [X]):-!.
mergeSort(L, SL):- 
             split_in_half(L, L1, L2), 
             mergeSort(L1, S1), 
             mergeSort(L2, S2),
             merge(S1, S2, SL). 


/* If the list is empty, then it fails
 * If the list only has one item, then reutrn itself
 * If the list has more than one item, then find the middle position and split the list into two half*/
intDiv(N,N1, R):- R is div(N,N1).
split_in_half([], _, _):-!, fail.
split_in_half([X],[],[X]). 
split_in_half(L, L1, L2):- 
             length(L,N), 
             intDiv(N,2,N1),
             length(L1, N1), 
             append(L1, L2, L). 

 /* Merge S1 and S2 and return S as the merged list
 * If left sublist is empty then return right sublist
 * If right sublist is empty then return left sublist*/
merge([], L, L). % comment
merge(L, [],L).  % comment 
merge([H1|T1], [H2|T2], [H1|T]):-
	H1 < H2,
	merge(T1,[H2|T2],T).

merge([H1|T1], [H2|T2], [H2|T]):-
	H2 =< H1,
	merge([H1|T1], T2, T).
   

/* QuickSort divides the items into two sub-arrays based on whether they are less than or greater than the
 * pivot element, which is chosen from the array*/

split(_, [],[],[]). 
 split(X, [H|T], [H|SMALL], BIG):- 
	H =< X, 
    split(X, T, SMALL, BIG).    

 split(X, [H|T], SMALL, [H|BIG]):-
    X =< H,
    split(X, T, SMALL, BIG). 

/* Uses a pivot to apply the quicksort algorithm, then partitions the array around the pivot*/

quickSort([], []).
quickSort([H|T], LS):-
	split(H, T, SMALL,BIG), 
	quickSort(SMALL, S), 
	quickSort(BIG, B), 
	append(S, [H|B], LS). 


/* When the length of the list is smaller than the entered THRESHOLD, 
 * hybridSort behaves like SMALL sorts (bubble or insertion sort) instead of choosing a sorting algorithm 
 * based on the list size
 * When the length of the list LIST is larger than or equal to THRESHOLD, 
 * hybridSort behaves like one of the BIG sorts (merge or quick sort)*/

hybridSort(LIST, bubbleSort, BIGALG, THRESHOLD, SLIST):-
	length(LIST, N), N=< THRESHOLD,      
      bubbleSort(LIST, SLIST).

hybridSort(LIST, insertionSort, BIGALG, THRESHOLD, SLIST):-
	length(LIST, N), N=<THRESHOLD,
      insertionSort(LIST, SLIST).

hybridSort(LIST, SMALL, mergeSort, THRESHOLD, SLIST):-
	length(LIST, N), N> THRESHOLD,      
	split_in_half(LIST, L1, L2),
    	hybridSort(L1, SMALL, mergeSort, THRESHOLD, S1),
    	hybridSort(L2, SMALL, mergeSort, THRESHOLD, S2),
    	merge(S1,S2, SLIST).       

hybridSort([H|T], SMALL, quickSort, THRESHOLD, SLIST):-
	length(LIST, N), N > THRESHOLD,      
	split(H, T, L1, L2),
      hybridSort(L1, SMALL, quickSort, THRESHOLD, SL1),
      hybridSort(L2, SMALL, quickSort, THRESHOLD, SL2),
      append(SL1, [H|SL2], SLIST).

hybridSort([H|T], SMALL, quickSort, THRESHOLD, SLIST):-
	length(LIST, N), N =< THRESHOLD,
    SMALL == bubbleSort ->  
    	bubbleSort(LIST, SLIST),
	SMALL == insertionSort ->  
		insertionSort(LIST, SLIST).


/* Test Command

myList(L),
bubbleSort(L, B_SL),
length(B_SL, B_SN),
insertionSort(L, I_SL),
length(I_SL, I_SN),
mergeSort(L, M_SL),
length(M_SL, M_SN),
quickSort(L, Q_SL),
length(Q_SL, Q_SN),
hybridSort(L, bubbleSort, mergeSort, 5, BM_SL),
length(BM_SL, BM_SN),
hybridSort(L, bubbleSort, mergeSort, 55, BM_SL_NE),
length(BM_SL_NE, BM_SN_NE),
hybridSort(L, bubbleSort, quickSort, 5, BQ_SL),
length(BQ_SL, BQ_SN),
hybridSort(L, bubbleSort, quickSort, 55, BQ_SL_NE),
length(BQ_SL_NE, BQ_SN_NE),
hybridSort(L, insertionSort, mergeSort, 5, IM_SL),
length(IM_SL, IM_SN),
hybridSort(L, insertionSort, mergeSort, 55, IM_SL_NE),
length(IM_SL_NE, IM_SN_NE),
hybridSort(L, insertionSort, quickSort, 5, IQ_SL),
length(IQ_SL, IQ_SN),
hybridSort(L, insertionSort, quickSort, 55, IQ_SL_NE),
length(IQ_SL_NE, IQ_SN_NE).

Parameter Description:

L: The initial random list with the length of 50

B_SL: Sorted list using bubbleSort
I_SL: Sorted list using insertionSort
M_SL: Sorted list using mergeSort
Q_SL: Sorted list using quickSort

BM_SL: Sorted list using hybridSort(bubbleSort, mergeSort) and threshold < list length
BQ_SL: Sorted list using hybridSort(bubbleSort, quickSort) and threshold < list length
IM_SL: Sorted list using hybridSort(insertionSort, mergeSort) and threshold < list length
IQ_SL: Sorted list using hybridSort(insertionSort, quickSort) and threshold < list length

BM_SL_NE: Sorted list using hybridSort(bubbleSort, mergeSort) and threshold > list length
BQ_SL_NE: Sorted list using hybridSort(bubbleSort, quickSort) and threshold > list length
IM_SL_NE: Sorted list using hybridSort(insertionSort, mergeSort) and threshold > list length
IQ_SL_NE: Sorted list using hybridSort(insertionSort, quickSort) and threshold > list length

B_SN: The length of sorted list using bubbleSort
I_SN: The length of sorted list using insertionSort
M_SN: The length of sorted list using mergeSort
Q_SN: The length of sorted list using quickSort

BM_SN: The length of sorted list using hybridSort(bubbleSort, mergeSort) and threshold < list length
BQ_SN: The length of sorted list using hybridSort(bubbleSort, quickSort) and threshold < list length
IM_SN: The length of sorted list using hybridSort(insertionSort, mergeSort) and threshold < list length
IQ_SN: The length of sorted list using hybridSort(insertionSort, quickSort) and threshold < list length

BM_SN_NE: The length of sorted list using hybridSort(bubbleSort, mergeSort) and threshold > list length
BQ_SN_NE: The length of sorted list using hybridSort(bubbleSort, quickSort) and threshold > list length
IM_SN_NE: The length of sorted list using hybridSort(insertionSort, mergeSort) and threshold > list length
IQ_SN_NE: The length of sorted list using hybridSort(insertionSort, quickSort) and threshold > list length

Test Result:

Run Number 1:

BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
4,
4,
9,
11,
11,
12,
12,
13,
13,
13,
14,
16,
17,
24,
25,
25,
26,
26,
35,
36,
37,
38,
39,
48,
49,
51,
52,
53,
55,
56,
59,
60,
61,
63,
64,
65,
72,
73,
73,
76,
81,
81,
82,
83,
83,
85,
87,
94,
96,
98
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
87,
61,
81,
13,
53,
49,
51,
81,
94,
73,
13,
52,
38,
12,
83,
25,
14,
60,
11,
36,
64,
11,
24,
59,
96,
56,
83,
12,
4,
16,
4,
48,
37,
26,
17,
98,
72,
85,
13,
76,
73,
35,
65,
82,
25,
39,
26,
55,
63,
9
]


Run Number 2:

BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
1,
5,
8,
9,
10,
17,
17,
18,
18,
18,
21,
21,
22,
23,
25,
25,
36,
36,
38,
38,
44,
45,
47,
50,
50,
56,
57,
57,
58,
59,
61,
64,
64,
66,
67,
68,
69,
72,
75,
79,
81,
83,
85,
86,
86,
87,
89,
97,
99,
99
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
23,
75,
21,
61,
44,
36,
50,
86,
36,
17,
38,
85,
21,
10,
25,
99,
64,
8,
1,
89,
22,
18,
17,
56,
38,
64,
81,
47,
57,
83,
9,
99,
50,
72,
18,
45,
57,
69,
87,
59,
66,
67,
86,
18,
58,
97,
25,
5,
79,
68
]


Run Number 3:

BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
3,
3,
3,
7,
10,
11,
11,
14,
23,
25,
26,
28,
29,
34,
35,
35,
36,
37,
37,
37,
40,
42,
43,
44,
44,
48,
49,
50,
56,
58,
59,
60,
65,
66,
68,
71,
74,
74,
77,
80,
81,
84,
84,
85,
86,
87,
89,
91,
92,
98
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
29,
44,
35,
68,
37,
71,
87,
11,
3,
85,
81,
89,
14,
60,
44,
28,
48,
56,
91,
25,
34,
84,
23,
35,
59,
98,
36,
3,
26,
37,
37,
42,
66,
3,
77,
40,
84,
92,
10,
7,
65,
74,
58,
50,
11,
74,
80,
49,
86,
43
]


Run Number 4:

BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
5,
6,
6,
7,
8,
10,
14,
16,
17,
19,
20,
29,
30,
31,
34,
35,
41,
42,
43,
43,
44,
53,
53,
54,
54,
56,
56,
57,
58,
58,
63,
64,
65,
69,
71,
71,
73,
73,
74,
74,
82,
85,
86,
88,
88,
89,
90,
90,
93,
97
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
53,
88,
7,
71,
8,
34,
43,
58,
17,
90,
89,
82,
56,
16,
5,
74,
20,
97,
30,
56,
44,
73,
19,
85,
6,
35,
65,
54,
74,
69,
58,
90,
88,
86,
6,
41,
14,
31,
10,
93,
73,
43,
54,
29,
42,
71,
63,
64,
53,
57
]



Run Number 5:

BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
1,
7,
8,
10,
12,
12,
13,
13,
16,
17,
18,
19,
32,
32,
35,
36,
38,
40,
43,
44,
47,
49,
49,
50,
58,
59,
59,
61,
61,
65,
69,
70,
72,
73,
74,
75,
77,
80,
82,
84,
84,
89,
89,
90,
92,
94,
96,
98,
98,
98
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
73,
94,
13,
50,
89,
74,
10,
98,
16,
47,
7,
12,
96,
12,
40,
32,
43,
92,
59,
84,
35,
75,
98,
69,
90,
61,
13,
32,
84,
98,
58,
17,
49,
82,
49,
89,
1,
65,
72,
36,
8,
59,
70,
80,
38,
61,
44,
77,
18,
19
]



Run Number 6:

BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
4,
5,
6,
7,
8,
9,
12,
13,
14,
15,
15,
17,
18,
18,
19,
19,
20,
22,
22,
25,
26,
27,
28,
29,
29,
31,
40,
47,
57,
63,
63,
66,
68,
72,
73,
74,
75,
79,
83,
84,
85,
85,
89,
91,
92,
94,
95,
96,
97,
97
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
96,
63,
63,
4,
83,
15,
12,
31,
66,
18,
73,
94,
26,
9,
89,
75,
5,
97,
15,
18,
22,
22,
79,
91,
47,
29,
92,
95,
28,
14,
8,
7,
85,
13,
40,
68,
17,
19,
84,
6,
27,
19,
29,
72,
74,
20,
57,
85,
25,
97
]



Run Number 7:

BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
1,
5,
8,
8,
10,
12,
12,
14,
14,
14,
15,
16,
22,
25,
27,
28,
28,
33,
35,
38,
43,
43,
44,
44,
45,
46,
47,
49,
50,
55,
56,
59,
66,
68,
70,
73,
74,
75,
76,
79,
79,
79,
80,
80,
80,
83,
88,
88,
95,
98
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
70,
75,
5,
14,
83,
74,
79,
14,
12,
15,
88,
22,
95,
38,
28,
80,
59,
43,
33,
28,
8,
56,
49,
44,
44,
46,
80,
80,
50,
47,
68,
55,
27,
14,
35,
12,
79,
66,
43,
76,
88,
45,
79,
10,
1,
16,
25,
98,
8,
73
]


Run Number 8:



BM_SL = BM_SL_NE, BM_SL_NE = BQ_SL, BQ_SL = BQ_SL_NE, BQ_SL_NE = B_SL, B_SL = IM_SL, IM_SL = IM_SL_NE, IM_SL_NE = IQ_SL, IQ_SL = IQ_SL_NE, IQ_SL_NE = I_SL, I_SL = M_SL, M_SL = Q_SL, Q_SL = [
6,
7,
8,
9,
9,
10,
11,
12,
14,
19,
22,
25,
26,
27,
30,
35,
38,
42,
42,
42,
44,
46,
46,
46,
50,
52,
56,
57,
57,
63,
66,
68,
68,
69,
69,
70,
71,
76,
79,
84,
87,
88,
89,
90,
90,
91,
94,
98,
98,
98
],
BM_SN = BM_SN_NE, BM_SN_NE = BQ_SN, BQ_SN = BQ_SN_NE, BQ_SN_NE = B_SN, B_SN = IM_SN, IM_SN = IM_SN_NE, IM_SN_NE = IQ_SN, IQ_SN = IQ_SN_NE, IQ_SN_NE = I_SN, I_SN = M_SN, M_SN = Q_SN, Q_SN = 50,
L = [
66,
87,
69,
12,
42,
42,
84,
46,
26,
89,
98,
46,
30,
98,
10,
35,
91,
38,
98,
52,
68,
9,
14,
6,
69,
68,
90,
11,
9,
22,
42,
56,
27,
94,
19,
90,
63,
71,
76,
88,
79,
57,
46,
7,
44,
70,
8,
25,
57,
50
]


CONCLUSION

Prolog as logical programming language it deals with objects and their relationships, the implementations of the insert sort and bubble sort are based on the concept of accumulation. And for merge sort and quick sort, the implementations are based on the concept of recursion. It accumulates the subresults throughout recursive computation. The pivot that is used to divide the list into two lists will have an impact on how efficiently the quick sort works while large lists are often sorted using merge sort. Also, in Prolog list explicitly supports with operations for head and tail access. For the hybrid sort, it is called recursively and behaves differently based on the relationship between the length of list and the threshold. When the list is larger than the threshold, it behaves like the big algorithms (merge or quick sort). Otherwise, it behaves like the small algorithms (bubble or insertion sort). In this way, the hybrid sort will be more efficient while solving large lists. 

*/
