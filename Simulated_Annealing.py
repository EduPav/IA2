import random
import math

# As we read distance matrix from archive we don't need a_star or the maze here.


def random_permutation(order_list):
    """
    Returns a neighbour sequence of the input.

    Args:
        order_list (list): Sequence of products

    Returns:
        list: initial list of products with one permutation 
    """
    i = 0
    random_a = random.randint(0, len(order_list)-1)

    aux = order_list[random_a]
    order_list.pop(random_a)
    order_list.append(aux)
    return order_list


def temperature(Temp, dT):
    """
    Returns the new temperature to follow a linear cooling schedule

    Args:
        Temp (float): current temperature
        dT (float): variation in temperature

    Returns:
        float: new temperature
    """
    Temp = Temp-dT
    return Temp


def probability(new_cost, current_cost, T):
    """
    Returns the probability of accepting a worse neighbour

    Args:
        new_cost (int): cost of neighbour sequence
        current_cost (int): cost of current sequence
        T (float): _description_

    Returns:
        float:  probability of the sequence
    """
    prob = math.exp(-(new_cost-current_cost) /
                    T)  # Bigger cost difference reduces prob. Bigger Temp increases prob
    return prob


def total_cost_of(sequence, distances):
    """
    Returns the picking sequence total cost

    Args:
        sequence (list): sequence of products
        distances (list of lists): distance_matrix with lower costs of traveling between each pair of products

    Returns:
        int: total cost of a list of product
    """
    total_cost = 0
    # We assume cargo bay in the same picking position of product 3 in the maze (its left)
    total_cost += int(distances[2][sequence[0]-1])
    for i in range(len(sequence)-1):
        # minus one because product n is row n-1
        total_cost += int(distances[sequence[i]-1][sequence[i+1]-1])
    total_cost += int(distances[sequence[i+1]-1][2])
    return total_cost


def simulated_annealing(distances, sequence, T, Kmax):
    """
    Returns the evolution of probability, the evolution of cost for each sequence, the sequence to use for one order of command and its cost

    Args:
        distances (list of lists): distance_matrix with lower costs of traveling between each pair of products
        sequence (list): starting sequence
        T (float): starting temperature
        Kmax (int): max number of iterations

    Returns:
        list: list of probability to accept worse neighbour
        list: list of cost of each neighbour sequence we accept
        list: best picking sequence found
        int: cost of the best picking sequence

    """
    costs_evolution = []
    probs = []
    current_cost = total_cost_of(sequence, distances)
    best_cost = current_cost
    best_sequence = sequence.copy()
    costs_evolution.append(current_cost)
    dT = T/Kmax
    for _ in range(Kmax):
        # Generate a neighbor.It can't be itself.
        new_sequence = random_permutation(sequence)
        new_cost = total_cost_of(new_sequence, distances)
        if new_cost < current_cost:
            sequence = new_sequence
            current_cost = new_cost
            if current_cost < best_cost:
                # .copy() so it's not changed when we change new_sequence
                best_sequence = new_sequence.copy()
                best_cost = current_cost

        else:
            r = random.uniform(0, 1)
            # Probability of accepting the neighbor
            prob = probability(new_cost, current_cost, T)
            probs.append(prob)
            if r <= prob:  # If not keeps last sequence
                sequence = new_sequence
                current_cost = new_cost

        T = temperature(T, dT)  # Reduces temperature
        costs_evolution.append(current_cost)
    # Best picking sequence and its cost
    return probs, costs_evolution, best_sequence, best_cost
