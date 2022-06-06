(define (problem capp-pieza)
    (:domain capp_tp2)
    (:objects 
    ;Orientation
        orientation-xp
        orientation-yp
        orientation-zp
        orientation-xn
        orientation-yn
        orientation-zn
    ;Features
        s2
        s4
        s6
        s9
        s10
        h1
        h3
        h5
        h7
        h9
        h11
        h12
    ;Type
        slot
        through-hole
        blind-hole
    ;Operation
        milling
        drilled
        polished
    )
    (:init 
    ;Orientation
        (orientation orientation-xp)
        (orientation orientation-yp)
        (orientation orientation-zp)
        (orientation orientation-xn)
        (orientation orientation-yn)
        (orientation orientation-zn)
    ;Features
        (feature s2)
        (feature s4)
        (feature s6)
        (feature s9)
        (feature s10)
        (feature h1)
        (feature h3)
        (feature h5)
        (feature h7)
        (feature h9)
        (feature h11)
        (feature h12)
    ;Type
        (type slot)
        (type through-hole)
        (type blind-hole)
    ;Operations
        (operation milling)
        (operation drilled)
        (operation polished)
    ;Features Types
        ;slot
        (feature-type s2 slot)
        (feature-type s4 slot)
        (feature-type s6 slot)
        (feature-type s9 slot)
        (feature-type s10 slot)
        
        ;through-hole
        (feature-type h1 through-hole)
        (feature-type h3 through-hole)
        (feature-type h5 through-hole)
        (feature-type h7 through-hole)
        ;blind-hole
        (feature-type h9 blind-hole)
        (feature-type h11 blind-hole)
        (feature-type h12 blind-hole)
    ;Piece Orientation
        (piece-orientation orientation-xn)  ;initial orientation
    ;Features Orientation (defines the orientation in which the operation should be performed)
        ;slot
        (orientation-feature s2 orientation-xp)
        (orientation-feature s4 orientation-xn)
        (orientation-feature s6 orientation-xp)
        (orientation-feature s9 orientation-zp)
        (orientation-feature s10 orientation-zp)
        ;through-hole
        (orientation-feature h1 orientation-xp)
        (orientation-feature h3 orientation-xn)
        (orientation-feature h5 orientation-xp)
        (orientation-feature h7 orientation-zp)
        ;blind-hole
        (orientation-feature h9 orientation-xp)
        (orientation-feature h11 orientation-xn)
        (orientation-feature h12 orientation-xp)
    ;Craftable (defines how the features types are crafted)
        (craftable slot milling)
        (craftable slot polished)
        (craftable blind-hole drilled)
        (craftable through-hole drilled)
    )
    (:goal 
        (and
        ;Slot goals
            (crafted s2)
            (crafted s4)
            (crafted s6)
            (crafted s9)
            (crafted s10)
        ;Through-hole goals
            (crafted h1)
            (crafted h3)
            (crafted h5)
            (crafted h7)
        ;Blind-hole goals
            (crafted h9)
            (crafted h11)
            (crafted h12)
        
        )
    )
)