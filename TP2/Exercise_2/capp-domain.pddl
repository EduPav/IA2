(define (domain capp_tp2)
(:requirements :equality :strips)
; STRIPS = Allows the usage of basic add and delete effects as specified in STRIPS.
; EQUALITY = Allows the usage of = to compare objects. 
;   For example if we have two objects as arguments ?s1 and ?s2 we can compare them to see if they’re the same.
(:predicates
    (orientation ?o) ;predicado de type
	(feature ?f) ;predicado de type (S1, S2, S3, etc)
    (type ?t) ;predicado de type (Slot, Through-Hole, Blind-Hole)
    (operation ?op) ;predicado de type (Fresado, Torneado, Taladrado)
    (feature-type ?f ?feat-type) ; Relaciona una feature F con un type 
    (piece-orientation ?oa) ;Define la orientación d ela pieza
    (orientation-feature ?f ?oa) ;Define la orientación de cada feature
    (craftable ?feat-type ?operation) ;Relacion entre type de feature y operationes de fabricación que se pueden usar para esas features
    (crafted ?feat) ;Indica cuando una feature ha sido crafted
    
) 

(:action setup-orientation
 :parameters ( ?orientation-inicial ?orientation-final )
 :precondition
	(and 
        (piece-orientation ?orientation-inicial) 
        (orientation ?orientation-inicial) 
        (orientation ?orientation-final)
    )
 :effect
	(and 
		(piece-orientation ?orientation-final)
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