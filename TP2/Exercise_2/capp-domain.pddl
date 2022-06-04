(define (domain capp)
(:requirements :equality :strips)
(:predicates
	(orientacion ?o)
	(feature ?f)
    (tipo ?t)
    (operacion ?op)
    (feature-tipo ?f ?feat-tipo)
    (orientacion-pieza ?oa)
    (orientacion-feature ?f ?oa)
    (fabricable ?feat-tipo ?operacion)
    (fabricada ?feat)
) 

(:action setup-orientacion
 :parameters ( ?orientacion-inicial ?orientacion-final )
 :precondition
	(and 
        (orientacion-pieza ?orientacion-inicial) 
        (orientacion ?orientacion-inicial) 
        (orientacion ?orientacion-final)
    )
 :effect
	(and 
		(orientacion-pieza ?orientacion-final)
		(not (orientacion-pieza ?orientacion-inicial))
	)
)

(:action op-fresado
 :parameters ( ?o ?f ?ft ?oper )
 :precondition
	(and 
        (orientacion-pieza ?o)
        (orientacion-feature ?f ?o)
        (orientacion ?o) 
        (feature ?f)
        (tipo ?ft)
        (feature-tipo ?f ?ft)
        (fabricable ?ft ?oper)
        (operacion ?oper)
        (= ?oper fresado)
    )
 :effect
    (fabricada ?f)
)
)
