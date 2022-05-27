%KNOWLEDGE BACKGROUND
%Axiomas
verify(pilot):-
    state(pilot, ok), writeln('Piloto funciona bien').
verify(e):-
    state(pilot, unknown), writeln('Please, chechk Pilot status'), !;
    state(pilot, yes), verify(pilot), writeln('Set the safety valve according to the instructions').

verify(f):-
    state(pilot, unknown), writeln('Please, chechk Pilot status'), !;
    state(pilot, no), verify(pilot), writeln('Pilot full service and reinstallation').

verify(pilot):-
    state(pilot, unknown), writeln('Please, check Pilot status'), !;
    state(proper_leakage_prevention_between_sit_and_orifice, yes), verify(proper_leakage_prevention_between_sit_and_orifice).

verify(proper_leakage_prevention_between_sit_and_orifice):-
    state(proper_leakage_prevention_between_sit_and_orifice, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), !;
    state(performance_and_efficiency_of_safety_valve_spring, yes), verify(performance_and_efficiency_of_safety_valve_spring).

verify(g):-
    state(proper_leakage_prevention_between_sit_and_orifice, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), !;
    state(proper_leakage_prevention_between_sit_and_orifice, no), verify(proper_leakage_prevention_between_sit_and_orifice), writeln('Repleace sit and orifice and put the safety valve into circuit').

verify(performance_and_efficiency_of_safety_valve_spring):-
    state(performance_and_efficiency_of_safety_valve_spring, unknown), writeln('Please, chek the performance and efficiency of safety valve spring'), !;
    state(control_valve_sensors_blocked, no), verify(control_valve_sensors_blocked).

verify(d):-
    state(performance_and_efficiency_of_safety_valve_spring, unknown), writeln('Please, check the performance and efficiency of safety valve spring'), !;
    state(performance_and_efficiency_of_safety_valve_spring, no), verify(performance_and_efficiency_of_safety_valve_spring), writeln('Putting spring and safety in the service').

verify(control_valve_sensors_blocked):-
    state(control_valve_sensors_blocked, unknown), writeln('Please, check if the control valve sensors are blocked'), !;
    state(valve_status_in_close_position, no), verify(valve_status_in_close_position).

verify(c):-
    state(control_valve_sensors_blocked, unknown), writeln('Please, check if the control valve sensors are blocked'), !;
    state(control_valve_sensors_blocked, yes), verify(control_valve_sensors_blocked), writeln('Cleaning and troubleshooting of the sensing pipes').

verify(valve_status_in_close_position):-
    state(valve_status_in_close_position, unknown), writeln('Please, check if the valve status is in close position'), !;
    state(relief_valve_work_correctly, no), verify(relief_valve_work_correctly).

verify(b):-
    state(valve_status_in_close_position, unknown), writeln('Please, check if the valve status is in close position'), !;
    state(valve_status_in_close_position, yes), verify(valve_status_in_close_position), writeln('Plase the safety valve in open position').
    
verify(relief_valve_work_correctly):-
    state(relief_valve_work_correctly, unknown), writeln('Please, chechk if the relief valve works correctly'), !;
    state(safety_valve_continuous_gas_evacuation, no), verify(safety_valve_continuous_gas_evacuation).

verify(a):-
    state(relief_valve_work_correctly, unknown), writeln('Please, chechk if the relief valve works correctly'), !;
    state(relief_valve_work_correctly, yes), verify(relief_valve_work_correctly), writeln('Safety function is appropiate').

verify(safety_valve_continuous_gas_evacuation):-
    state(safety_valve_continuous_gas_evacuation, unknown),writeln('Verify if safety valve has conituous gas evacuation'), !;
    state(safety_valve_continuous_gas_evacuation, no).
%GROUND FACTS
state(pilot, yes).
state(proper_leakage_prevention_between_sit_and_orifice, unknown).
state(performance_and_efficiency_of_safety_valve_spring, unknown).
state(control_valve_sensors_blocked, unknown).
state(valve_status_in_close_position, unknown).
state(relief_valve_work_correctly, unknown).
state(safety_valve_continuous_gas_evacuation, unknown).

