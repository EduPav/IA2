(define (domain aviones)
(:requirements :strips)
(:predicates
	(en ?a ?b) 
	(avion ?a)
	(tanque_lleno ?a)
	(carga ?c)
	(aeropuerto ?a)
	(mantenimiento_ok ?a)
) 
(:action cargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?ap) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?a) 
		(not (en ?c ?ap))
	)
)
(:action descargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?a) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?ap) 
		(not (en ?c ?a))
	)
)
(:action volar
 :parameters ( ?a ?origen ?destino)
 :precondition
	(and (en ?a ?origen) (avion ?a) (tanque_lleno ?a) (aeropuerto ?origen) (aeropuerto ?destino) (mantenimiento_ok ?a))
 :effect
	(and 
		(en ?a ?destino) 
		(not (en ?a ?origen))
		(not (tanque_lleno ?a))
		(not (mantenimiento_ok ?a))
	)
)
(:action cargar-combustible
 :parameters (?a)
 :precondition
	 (avion ?a)
 :effect 
	(tanque_lleno ?a 
	)
)
(:action revisar
 :parameters (?a)
 :precondition
	(avion ?a)
 :effect 
	(mantenimiento_ok ?a)
)
)
