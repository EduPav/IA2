%verify(maintenance):- 
%    status(safety_valve_continuous_gas_evacuation,yes),verify()


%assert y retract de una oración la agrega o quita respectivamente de la Base del conocimiento.

%Encadenamiento hacia adelante? I can ask if I have anything to do or for an specific task true value?
%How would this KB be used? I don't get the example
%To have proven an specific point in the workflow doesn't guarantee you have to accomplish the consequent task.
%Chain of yes and no variable values for every leaf.



%verify(E):-status(D,unknown),writeln("Check D status"),!; 
%           status(D,yes),verify(D),writeln("Accion E").



%KNOWLEDGE BASE
%Axioms
%Oración lógica (consecuente :- antecedente)
%predicados: verificar(predicado unario), estado(binario), writeln...Un predicado es una relación. Hay predicados n-arios

%verify(x): True if all the question nodes before X have the right answer to reach X
%status(x,r): True if the question x's answer is r

%EComment: All leaves should go first. 
%EComment: Every leaf name changed to a descriptive one
%EComment: Status unknown instruction changed to a user readable format

%Instruction nodes
%   Middle Left
verify(set_safety_valve):-
    status(pilot, unknown), writeln('Please, check if pilot works properly'), !;
    status(pilot, yes), verify(pilot), writeln('Set the safety valve according to the instructions');
    status(proper_leakage_prevention_between_sit_and_orifice_2, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), !;
    status(proper_leakage_prevention_between_sit_and_orifice_2, yes), verify(proper_leakage_prevention_between_sit_and_orifice_2), writeln('Set the safety valve according to the instructions').

verify(pilot_full_service):-
    status(pilot, unknown), writeln('Please, check if pilot works properly'), !;
    status(pilot, no), verify(pilot), writeln('Pilot full service and reinstallation').

verify(replace_sit_orifice):-
    status(proper_leakage_prevention_between_sit_and_orifice, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), !;
    status(proper_leakage_prevention_between_sit_and_orifice, no), verify(proper_leakage_prevention_between_sit_and_orifice), writeln('Replace sit and orifice and put the safety valve into circuit');
    status(proper_leakage_prevention_between_sit_and_orifice_2, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), !;
    status(proper_leakage_prevention_between_sit_and_orifice_2, no), verify(proper_leakage_prevention_between_sit_and_orifice_2), writeln('Replace sit and orifice and put the safety valve into circuit').

verify(spring_safety_to_service):-
    status(performance_and_efficiency_of_safety_valve_spring, unknown), writeln('Please, check the performance and efficiency of safety valve spring'), !;
    status(performance_and_efficiency_of_safety_valve_spring, no), verify(performance_and_efficiency_of_safety_valve_spring), writeln('Putting spring and safety in the service').

verify(clean_sensing_pipes):-
    status(control_valve_sensors_blocked, unknown), writeln('Please, check if the control valve sensors are blocked'), !;
    status(control_valve_sensors_blocked, yes), verify(control_valve_sensors_blocked), writeln('Cleaning and troubleshooting of the sensing pipes').

verify(safety_valve_to_open):-
    status(valve_status_in_close_position, unknown), writeln('Please, check if the valve status is in close position'), !;
    status(valve_status_in_close_position, yes), verify(valve_status_in_close_position), writeln('Place the safety valve in open position').

verify(safety_appropriate):-
    status(relief_valve_work_correctly_with_10_increase, unknown), writeln('Please, check if the relief valve works correctly with a 10% increase of regulating pressure'), !;
    status(relief_valve_work_correctly_with_10_increase, yes), verify(relief_valve_work_correctly_with_10_increase), writeln('Safety function is appropiate').
%   Middle Right
verify(replace_safety_spring):-
    status(safety_spring_effective, unknown), writeln('Please, check if safety spring is efective'), !;
    status(safety_spring_effective, no), verify(safety_spring_effective), writeln('Replace safety spring in the service').

verify(clean_fix_sensing_pipes):-
    status(control_pressure_sensor_pipes_blocked, unknown), writeln('Please, check if control and pressure sensor pipes are blocked'), !;
    status(control_pressure_sensor_pipes_blocked, yes), verify(control_pressure_sensor_pipes_blocked), writeln('Clean up and fix the faults of the sensing pipes').

verify(adjust_regulator):-
    status(line_gas_pressure_appropriate, unknown), writeln('Please, check if line gas pressure is appropriate'), !;
    status(line_gas_pressure_appropriate, no), verify(line_gas_pressure_appropriate), writeln('Adjust the regulator according to the instructions').



%Question nodes
%EComment: Corrected status asking for its own node status value as unknown to asking previous node value as unknown
%Added a false clause in first sentence so it stops there
%   Middle Left
verify(pilot):-
    status(proper_leakage_prevention_between_sit_and_orifice, unknown), writeln('Please, check if there is proper leakage prevention between sit and orifice'), false, !;
    status(proper_leakage_prevention_between_sit_and_orifice, yes), verify(proper_leakage_prevention_between_sit_and_orifice).

verify(proper_leakage_prevention_between_sit_and_orifice):-
    status(performance_and_efficiency_of_safety_valve_spring, unknown), writeln('Please, check the performance and efficiency of safety valve spring'), false, !;
    status(performance_and_efficiency_of_safety_valve_spring, yes), verify(performance_and_efficiency_of_safety_valve_spring).

verify(performance_and_efficiency_of_safety_valve_spring):-
    status(control_valve_sensors_blocked, unknown), writeln('Please, check if the control valve sensors are blocked'), false, !;
    status(control_valve_sensors_blocked, no), verify(control_valve_sensors_blocked).

verify(control_valve_sensors_blocked):-
    status(valve_status_in_close_position, unknown), writeln('Please, check if the valve status is in close position'), false, !;
    status(valve_status_in_close_position, no), verify(valve_status_in_close_position).

verify(valve_status_in_close_position):-
    status(relief_valve_work_correctly_with_10_increase, unknown), writeln('Please, check if the relief valve works correctly with a 10% increase of regulating pressure'), false, !;
    status(relief_valve_work_correctly_with_10_increase, no), verify(relief_valve_work_correctly_with_10_increase).
    
verify(relief_valve_work_correctly_with_10_increase):-
    status(safety_valve_continuous_gas_evacuation, unknown), writeln('Please, check if safety valve has a continuous gas evacuation'), false, !;
    status(safety_valve_continuous_gas_evacuation, no).%verify(safety_valve_continuous_gas_evacuation). This has no previous node so its always true
%   Middle Right
verify(proper_leakage_prevention_between_sit_and_orifice_2):-
    status(safety_spring_effective, unknown), writeln('Please, check if safety spring is effective'), false, !;
    status(safety_spring_effective, yes), verify(safety_spring_effective).

verify(safety_spring_effective):-
    status(control_pressure_sensor_pipes_blocked, unknown), writeln('Please, check if control and pressure sensor pipes are blocked'), false, !;
    status(control_pressure_sensor_pipes_blocked, no), verify(control_pressure_sensor_pipes_blocked).

verify(control_pressure_sensor_pipes_blocked):-
    status(line_gas_pressure_appropriate, unknown), writeln('Please, check if line gas pressure is appropriate'), false, !;
    status(line_gas_pressure_appropriate, yes), verify(line_gas_pressure_appropriate).

verify(line_gas_pressure_appropriate):-
    status(safety_valve_continuous_gas_evacuation, unknown), writeln('Please, check if safety valve has a continuous gas evacuation'), false, !;
    status(safety_valve_continuous_gas_evacuation, yes).

%Ecomment:
/* Erased, because it makes no sense to check this.
verify(safety_valve_continuous_gas_evacuation):-
    status(safety_valve_continuous_gas_evacuation, unknown),writeln('Verify '), !;
    status(safety_valve_continuous_gas_evacuation, no).
*/

%GROUND FACTS
status(pilot, yes).
status(proper_leakage_prevention_between_sit_and_orifice, yes).
status(performance_and_efficiency_of_safety_valve_spring, yes).
status(control_valve_sensors_blocked, no).
status(valve_status_in_close_position, no).
status(relief_valve_work_correctly_with_10_increase, no).
status(safety_valve_continuous_gas_evacuation, no).




%verify(E):-status(D,unknown),writeln("Check D status"),!;
%           status(D,yes),verify(D),writeln("Accion E").
%verify(valve_status_closed) :-
%                status(valve_status_closed, undefined), writeln('Check valve status')),!;
%                status(relief_valve_ok_with_10_percent_more_pressure, no),verify(relief_valve_ok_with_10_percent_more_pressure).
%Add instruction to make status(proper_leakage_prevention_between_sit_and_orifice_2,yes/no) equal to the 1 case
%Manejo de error de tener una constante con dos valores de status?
%Verificacion de errores probando que TODAS las combinaciones de ground facts den lo correcto
%safety sprong efectivee used twice?
%Add general maintenance sentence
%When read, delete all EComments
