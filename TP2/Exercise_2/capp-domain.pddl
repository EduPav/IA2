(define (domain capp_tp2)
(:requirements :equality :strips)
; STRIPS = Allows the usage of basic add and delete effects as specified in STRIPS.
; EQUALITY = Allows the usage of = to compare objects. 
;   For example if we have two objects as arguments ?s1 and ?s2 we can compare them to see if they’re the same.
(:predicates
    (orientation ?o) ;type predicate
	(feature ?f) ;type predicate (S1, S2, S3, etc)
    (type ?t) ;type predicate  (Slot, Through-Hole, Blind-Hole)
    (operation ?op) ;type predicate  (Fresado, Torneado, Taladrado)
    (feature-type ?f ?feat-type) ; Relates an F featurewith a type 
    (piece-orientation ?oa) ;Defines piece orientation
    (orientation-feature ?f ?oa) ;Defines the feature orientation
    (craftable ?feat-type ?operation) ;Relation between "feature type" and the manufacturing operations that can be used with those features
    (crafted ?feat) ;Indicates a crafted feature
    
) 

(:action setup-orientation ;With this we change the piece orientation
 :parameters ( ?orientation-inicial ?orientation-final )
 :precondition
	(and 
        (piece-orientation ?orientation-inicial) ;Precondition
        (orientation ?orientation-inicial) 
        (orientation ?orientation-final)
    )
 :effect
	(and 
		(piece-orientation ?orientation-final) ;Effect
		(not (piece-orientation ?orientation-inicial))
	)
)

(:action op-milling ;Fresado
 :parameters ( ?o ?f ?ft ?oper ) ; o = operation, f = feature, ft = feature type, oper = operation
 ;We have "opper" as a variable to relate the "feature type" with the craftable predicate
 :precondition
	(and 
        (piece-orientation ?o)
        (orientation-feature ?f ?o) ;We force the feature and the piece to have the same orientation
        (orientation ?o) 
        (feature ?f)
        (type ?ft)
        (feature-type ?f ?ft) ;We relate the feature with the type
        (craftable ?ft ?oper)
        (operation ?oper)
        (= ?oper milling) ;We use equality for this
    )
 :effect
    (crafted ?f)
)
(:action op-drilled ;Taladrado
 :parameters ( ?o ?f ?ft ?oper )
 :precondition
	(and 
        (piece-orientation ?o)
        (orientation-feature ?f ?o)
        (orientation ?o) 
        (feature ?f)
        (type ?ft)
        (feature-type ?f ?ft)
        (craftable ?ft ?oper)
        (operation ?oper)
        (= ?oper drilled)
    )
 :effect
    (crafted ?f)
)
(:action op-polished ;Taladrado
 :parameters ( ?o ?f ?ft ?oper )
 :precondition
	(and 
        (piece-orientation ?o)
        (orientation-feature ?f ?o)
        (orientation ?o) 
        (feature ?f)
        (type ?ft)
        (feature-type ?f ?ft)
        (craftable ?ft ?oper)
        (operation ?oper)
        (= ?oper polished)
    )
 :effect
    (crafted ?f)
)
)