(define (problem capp-pieza)
    (:domain capp)
    (:objects 
        orientacion_pos_x
        orientacion_pos_y
        orientacion_pos_z
        orientacion_neg_x
        orientacion_neg_y
        orientacion_neg_z
        s2
        s4
        s6
        s9
        s10
        slot
        through-hole
        blind-hole
        fresado
        taladrado
        torneado
    )
    (:init 
        (orientacion orientacion_pos_x)
        (orientacion orientacion_pos_y)
        (orientacion orientacion_pos_z)
        (orientacion orientacion_neg_x)
        (orientacion orientacion_neg_y)
        (orientacion orientacion_neg_z)
        (feature s2)
        (feature s4)
        (feature s6)
        (feature s9)
        (feature s10)
        (tipo slot)
        (tipo through-hole)
        (tipo blind-hole)
        (operacion fresado)
        (operacion taladrado)
        (operacion torneado)
        (feature-tipo s2 slot)
        (feature-tipo s4 slot)
        (feature-tipo s6 slot)
        (feature-tipo s9 slot)
        (feature-tipo s10 slot)
        (orientacion-pieza orientacion_neg_x)
        (orientacion-feature s2 orientacion_pos_x)
        (orientacion-feature s4 orientacion_neg_x)
        (orientacion-feature s6 orientacion_pos_x)
        (orientacion-feature s9 orientacion_pos_z)
        (orientacion-feature s10 orientacion_pos_z)
        (fabricable slot fresado)
    )
    (:goal 
        (and
            (fabricada s2)
            (fabricada s4)
            (fabricada s6)
            (fabricada s9)
            (fabricada s10)
        )
    )
)