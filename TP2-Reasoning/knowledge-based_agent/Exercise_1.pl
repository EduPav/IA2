%KNOWLEDGE BASE (all the code)

%AXIOMS

%General Maintenance
do(maintenance):-
    status_error(check),!;
    verify(set_safety_valve);
    verify(pilot_full_service);
    verify(replace_sit_orifice);
    verify(spring_safety_to_service);
    verify(clean_sensing_pipes);
    verify(safety_valve_to_open);
    verify(safety_appropriate);
    verify(replace_safety_spring);
    verify(clean_fix_sensing_pipes);
    verify(adjust_regulator);
    %Not added a ! at the end of each because there might be other instructions in headset's branches.
    %Right use of this sentence implies selecting ";" after each instruction in CLI.
    verify(report_to_inspection);
    verify(is_reported_to_inspection);
    verify(coordinate_to_render_and_color);
    verify(report_to_repair_department).
    
%Error in duplicate status values check
status_error(check):-
    status(X,Y), status(X,Z), dif(Y,Z), writeln(X), writeln('has 2 status values. It should have exactly one for the KB to work properly'),false.



%Instruction nodes (%All leaves go first.) 
%   Middle Left
verify(set_safety_valve):-
    status(pilot, unknown), writeln('Please, check if pilot works properly'), false;
    status(pilot, yes), verify(pilot), writeln('Set the safety valve according to the instructions');
    status(proper_leakage_prevention_between_sit_and_orifice_2, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), false;
    status(proper_leakage_prevention_between_sit_and_orifice_2, yes), verify(proper_leakage_prevention_between_sit_and_orifice_2), writeln('Set the safety valve according to the instructions').

verify(pilot_full_service):-
    status(pilot, unknown), writeln('Please, check if pilot works properly'), false;
    status(pilot, no), verify(pilot), writeln('Pilot full service and reinstallation').

verify(replace_sit_orifice):-
    status(proper_leakage_prevention_between_sit_and_orifice, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), false;
    status(proper_leakage_prevention_between_sit_and_orifice, no), verify(proper_leakage_prevention_between_sit_and_orifice), writeln('Replace sit and orifice and put the safety valve into circuit');
    status(proper_leakage_prevention_between_sit_and_orifice_2, unknown), writeln('Please, check if there is a proper leakage prevention between sit and orifice'), false;
    status(proper_leakage_prevention_between_sit_and_orifice_2, no), verify(proper_leakage_prevention_between_sit_and_orifice_2), writeln('Replace sit and orifice and put the safety valve into circuit').

verify(spring_safety_to_service):-
    status(performance_and_efficiency_of_safety_valve_spring, unknown), writeln('Please, check the performance and efficiency of safety valve spring'), false;
    status(performance_and_efficiency_of_safety_valve_spring, no), verify(performance_and_efficiency_of_safety_valve_spring), writeln('Putting spring and safety in the service').

verify(clean_sensing_pipes):-
    status(control_valve_sensors_blocked, unknown), writeln('Please, check if the control valve sensors are blocked'), false;
    status(control_valve_sensors_blocked, yes), verify(control_valve_sensors_blocked), writeln('Cleaning and troubleshooting of the sensing pipes').

verify(safety_valve_to_open):-
    status(valve_status_in_close_position, unknown), writeln('Please, check if the valve status is in close position'), false;
    status(valve_status_in_close_position, yes), verify(valve_status_in_close_position), writeln('Place the safety valve in open position').

verify(safety_appropriate):-
    status(relief_valve_work_correctly_with_10_increase, unknown), writeln('Please, check if the relief valve works correctly with a 10% increase of regulating pressure'), false;
    status(relief_valve_work_correctly_with_10_increase, yes), verify(relief_valve_work_correctly_with_10_increase), writeln('Safety function is appropiate').

%   Middle Right
verify(replace_safety_spring):-
    status(safety_spring_effective, unknown), writeln('Please, check if safety spring is efective'), false;
    status(safety_spring_effective, no), verify(safety_spring_effective), writeln('Replace safety spring in the service').

verify(clean_fix_sensing_pipes):-
    status(control_pressure_sensor_pipes_blocked, unknown), writeln('Please, check if control and pressure sensor pipes are blocked'), false;
    status(control_pressure_sensor_pipes_blocked, yes), verify(control_pressure_sensor_pipes_blocked), writeln('Clean up and fix the faults of the sensing pipes').

verify(adjust_regulator):-
    status(line_gas_pressure_appropriate, unknown), writeln('Please, check if line gas pressure is appropriate'), false;
    status(line_gas_pressure_appropriate, no), verify(line_gas_pressure_appropriate), writeln('Adjust the regulator according to the instructions').

%   Left
verify(is_reported_to_inspection):-
    status(thickness_under_threshold_limit, unknown), writeln('Please check if thickness is less than the threshold limit'), false;
    status(thickness_under_threshold_limit, yes), verify(thickness_under_threshold_limit), writeln('Equipment status will be reported to the technical inspection unit immediately').

verify(suitable_equipment_condition):-
    status(thickness_under_threshold_limit, unknown), writeln('Please check if thickness is less than the threshold limit'), false;
    status(thickness_under_threshold_limit, no), verify(thickness_under_threshold_limit), writeln('The condition of the equipment is suitable').

verify(coordinate_to_render_and_color):-
    status(safety_valve_body_pipes_joints_dazzling_rusting, unknown), writeln('Please check if the safety valve body, pipes and joints have the effects of dazzling and rusting.'), false;
    status(safety_valve_body_pipes_joints_dazzling_rusting, yes), writeln('Coordination is requiered in order to render and color the equipment').
                            %No need to verify previous as it's a second layer instruction.

%   Right
verify(report_to_repair_department):-
    status(leakage_fixed_with_wrench, unknown), writeln('Please, check if the leakage is fixed with the wrench at joints'), false;
    status(leakage_fixed_with_wrench, no), verify(leakage_fixed_with_wrench), writeln('Send a report to the repair department to fix the gas leakage at joint').

verify(report_to_inspection):-
    status(leakage_fixed_with_wrench, unknown), writeln('Please check if the leakage is fixed with the wrench at joints'), false;
    status(leakage_fixed_with_wrench, yes), verify(leakage_fixed_with_wrench), writeln('Report to Technical Inspection Unit of fixed wrench at joints').
                                                                                %Not specified what to report in the exercise. Then kept generic
verify(safety_valve_no_gas_leakage):-
    status(gas_leakage_joint, unknown), writeln('Please check if there is a gas leakage at joint.'), false;
    status(gas_leakage_joint, no), writeln('The safety valve joint is free of gas leakage').
                            %No need to verify previous as it's a second layer instruction.

%Question nodes
%   Middle Left
verify(pilot):-
    status(proper_leakage_prevention_between_sit_and_orifice, unknown), writeln('Please, check if there is proper leakage prevention between sit and orifice'), false, !;
    status(proper_leakage_prevention_between_sit_and_orifice, no), writeln('There is no proper leakage prevention between Sit and Orifice'), false, !; %%%%
    status(proper_leakage_prevention_between_sit_and_orifice, yes), verify(proper_leakage_prevention_between_sit_and_orifice).


verify(proper_leakage_prevention_between_sit_and_orifice):-
    status(performance_and_efficiency_of_safety_valve_spring, unknown), writeln('Please, check the performance and efficiency of safety valve spring'), false, !;
    status(performance_and_efficiency_of_safety_valve_spring, no), writeln('Performance and efficiency of the safety valve is not good'), false, !; %%%%
    status(performance_and_efficiency_of_safety_valve_spring, yes), verify(performance_and_efficiency_of_safety_valve_spring).

verify(performance_and_efficiency_of_safety_valve_spring):-
    status(control_valve_sensors_blocked, unknown), writeln('Please, check if the control valve sensors are blocked'), false, !;
    status(control_valve_sensors_blocked, yes), writeln('The control valve sensors are blocked'), false, !; %%%%
    status(control_valve_sensors_blocked, no), verify(control_valve_sensors_blocked).

verify(control_valve_sensors_blocked):-
    status(valve_status_in_close_position, unknown), writeln('Please, check if the valve status is in close position'), false, !;
    status(valve_status_in_close_position, yes), writeln('The valve status is in CLOSE position'), false, !; %%%%
    status(valve_status_in_close_position, no), verify(valve_status_in_close_position).

verify(valve_status_in_close_position):-
    status(relief_valve_work_correctly_with_10_increase, unknown), writeln('Please, check if the relief valve works correctly with a 10% increase of regulating pressure'), false, !;
    status(relief_valve_work_correctly_with_10_increase, yes), writeln('The relief valve works correctly'), false, !; %%%%
    status(relief_valve_work_correctly_with_10_increase, no), verify(relief_valve_work_correctly_with_10_increase).
    
verify(relief_valve_work_correctly_with_10_increase):-
    status(safety_valve_continuous_gas_evacuation, unknown), writeln('Please, check if safety valve has a continuous gas evacuation'), false, !;
    status(safety_valve_continuous_gas_evacuation, unknown), writeln('The safety valve has continuous gas evacuation'), false, !; %%%%
    status(safety_valve_continuous_gas_evacuation, no).%EComment:verify(safety_valve_continuous_gas_evacuation). This has no previous node so its always true

%   Middle Right
verify(proper_leakage_prevention_between_sit_and_orifice_2):-
    status(safety_spring_effective, unknown), writeln('Please, check if safety spring is effective'), false, !;
    status(safety_spring_effective, no), writeln('The safety spring is not effective'), false, !; %%%%
    status(safety_spring_effective, yes), verify(safety_spring_effective).

verify(safety_spring_effective):-
    status(control_pressure_sensor_pipes_blocked, unknown), writeln('Please, check if control and pressure sensor pipes are blocked'), false, !;
    status(control_pressure_sensor_pipes_blocked, yes), writeln('Control pressure sensor pipes are blocked'), false, !; %%%%
    status(control_pressure_sensor_pipes_blocked, no), verify(control_pressure_sensor_pipes_blocked).

verify(control_pressure_sensor_pipes_blocked):-
    status(line_gas_pressure_appropriate, unknown), writeln('Please, check if line gas pressure is appropriate'), false, !;
    status(line_gas_pressure_appropriate, no), writeln('Line gas pressure is not appropiate'), false, !; %%%%
    status(line_gas_pressure_appropriate, yes), verify(line_gas_pressure_appropriate).

verify(line_gas_pressure_appropriate):-
    status(safety_valve_continuous_gas_evacuation, unknown), writeln('Please, check if safety valve has a continuous gas evacuation'), false, !;
    status(safety_valve_continuous_gas_evacuation, no), writeln('Savety valve has not a continuous gas evacuation'), false, !; %%%%
    status(safety_valve_continuous_gas_evacuation, yes).


%   Left
verify(thickness_under_threshold_limit):-
    status(safety_valve_body_pipes_joints_dazzling_rusting, unknown), writeln('Please check if the safety valve body, pipes and joints have the effects of dazzling and rusting.'), false, !;
    status(safety_valve_body_pipes_joints_dazzling_rusting, yes), writeln('Safety valve body, pipes and joints have the effects of dazzling and rusting.'), false, !; %%%%
    status(safety_valve_body_pipes_joints_dazzling_rusting, no).

%   Right
verify(leakage_fixed_with_wrench):-
    status(gas_leakage_joint, unknown), writeln('Please checkif there is a gas leakage at joint'), false, !;
    status(gas_leakage_joint, no), writeln('There is no gas leakage at joint'), false, !; %%%%
    status(gas_leakage_joint, yes). 


%GROUND FACTS: Only answers to questions, NOT to leaves.
%   Middle Left
status(pilot, no).
status(proper_leakage_prevention_between_sit_and_orifice, no).
status(performance_and_efficiency_of_safety_valve_spring, yes).
status(control_valve_sensors_blocked, no).
status(valve_status_in_close_position, no).
status(relief_valve_work_correctly_with_10_increase, no).
status(safety_valve_continuous_gas_evacuation, yes).

%   Middle Right
status(proper_leakage_prevention_between_sit_and_orifice_2,X):- status(proper_leakage_prevention_between_sit_and_orifice, X).
%previous sentence could be replaced by the second in Axioms, but as we do need a second constant in verify, we also use it in status for the sake of reducing code complexity.
status(safety_spring_effective,yes).
status(control_pressure_sensor_pipes_blocked,no).
status(line_gas_pressure_appropriate,yes).

%   Right
status(leakage_fixed_with_wrench, no).
status(gas_leakage_joint, yes).

%   Left
status(safety_valve_body_pipes_joints_dazzling_rusting, no).

thickness(2).
%Define status of thickness_under_threshold_limit according to a comparisson between thickness and a thickness threshold.
status(thickness_under_threshold_limit, no):- thickness(X), X >= 3, !.
status(thickness_under_threshold_limit, yes):- thickness(X), X < 3, !.




%Notes:
    %safety spring efective used twice? As written differently in the flow chart we chose to create 2 constants


%Pending tasks
    %Make all the ground facts combinations that must activate an instruction and check if that happens.





%SOLUTION LOGIC
    %verify(x): True if all the question nodes before X have the right answer to reach X
    %status(x,r): True if the question x's answer is r


%General structure for a "verify" sentence
    %Supposing D is a question and C is it's previous node. Yes is the answer to the previous node to get into D
        %verify(D):-status(C,unknown),writeln("Check C status"), false; 
        %           status(C,yes),verify(C).

    %Supposing A is a question at the top and B is second layer
        %verify(B):-status(A,unknown),writeln("Check A status"),false; 
        %           status(A,yes).

    %A won't have a verify sentence. Only a status one as it doesn't have previous nodes

    %Supposing E is a leaf
        %verify(E):-status(D,unknown),writeln("Check D status"),false; 
        %           status(D,yes),verify(D),writeln("Accion E").





%Possible improvement if we wanted to implement this in real life: 
    /*
    General Maintenance asks you to define all nodes when it's not really necessary.
    To solve the previous we should develope a chain for general maintenance that starts in the origin node and expands
    the subsequents. We have made sentences that start from leaves and check if you have all the info to define if
    that instruction should be done, but from the end to the start, which is not efficient.
    */
