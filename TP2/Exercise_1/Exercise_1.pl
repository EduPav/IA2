%KNOWLEDGE BACKGROUND
%Axiomas
verify(pilot):-
    state(pilot, ok), writeln('Piloto funciona bien').
verify(pilot):-
    state(pilot, unknown),
    (
        (
            state(proper_leakage_prevention_between_sit_and_orifice, ok),
            writeln('Verify Pilot') %Si proper_leakage_prevention_between_sit_and_orifice es OK, imprime VERIFICAR PILOTO
        )
        ;
        verify(proper_leakage_prevention_between_sit_and_orifice) %If unknown, verify state
    ).
verify(proper_leakage_prevention_between_sit_and_orifice):-
    state(proper_leakage_prevention_between_sit_and_orifice, unknown),
    (
        (
            state(performance_and_efficiency_of_safety_valve_spring, ok),
            writeln('Verify leakage prevention between sit and orifice') %If performance_and_efficiency_of_safety_valve_spring is OK, print VERIFY PILOT
        )
        ;
        verify(performance_and_efficiency_of_safety_valve_spring) %If unknown, verify state
    ).
verify(performance_and_efficiency_of_safety_valve_spring):-
    state(performance_and_efficiency_of_safety_valve_spring, unknown),
    (
        (
            state(control_valve_sensors_blocked, no),
            writeln('Verify performance and efficiency of safety valve spring') %If control_valve_sensors_blocked is NO, print VERIFY PERFORMANCE AND...
        )
        ;
        verify(control_valve_sensors_blocked) %If unknown, verify state
    ).
verify(control_valve_sensors_blocked):-
    state(control_valve_sensors_blocked, unknown),
    (
        (
            state(valve_status_in_close_position, no),
            writeln('Verify if control valve sensors are blocked') %If valve_status_in_close_position is NO, print VERIFY IF CONTROL VALEVE SENSORS ARE BLOCKED...
        )
        ;
        verify(valve_status_in_close_position) %If unknown, verify state
    ).
verify(valve_status_in_close_position):-
    state(valve_status_in_close_position, unknown),
    (
        (
            state(relief_valve_work_correctly, no),
            writeln('Verify if the valve status is in the close position') %If relief_valve_work_correctly is no, print VERIFY IF THE VALVE STATUS...
        )
        ;
        verify(relief_valve_work_correctly) %If unknown, verify state
    ).
verify(relief_valve_work_correctly):-
    state(relief_valve_work_correctly, unknown),
    (
        (
            state(safety_valve_continuous_gas_evacuation, no),
            writeln('Verify if the relief valve works correctly') %If safety_valve_continuous_gas_evacuation is NO, print VERIFY IF THE RELIEF VALVE...
        )
        ;
        verify(safety_valve_continuous_gas_evacuation) %If unknown, verify state
    ).
verify(safety_valve_continuous_gas_evacuation):-
    state(safety_valve_continuous_gas_evacuation, unknown),
    writeln('Verify if safety valve has conituous gas evacuation').
%GROUND FACTS
state(pilot, unknown).
state(proper_leakage_prevention_between_sit_and_orifice, unknown).
state(performance_and_efficiency_of_safety_valve_spring, unknown).
state(control_valve_sensors_blocked, unknown).
state(valve_status_in_close_position, unknown).
state(relief_valve_work_correctly, unknown).
state(safety_valve_continuous_gas_evacuation, unknown).

