# csp.py
# From Classic Computer Science Problems in Python Chapter 3
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type


# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables # variables to be constrained
        self.domains: Dict[V, List[D]] = domains # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # print(f"assign {first} with {value}")
            # if we're still consistent, we recurse (continue)
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None


# ---------- sudoku solver ----------
import sys
import time
from typing import List, NamedTuple, Dict, Tuple


GRID_SIZE = 9
BOX_SIZE = 3


class GridLocation(NamedTuple):
    row: int
    column: int


def parse_input(input: str) -> Tuple[List[GridLocation], Dict[GridLocation, List[int]], Dict[GridLocation, List[int]]]:
    grid_locations = []
    possible_values_by_location = {}
    assignment = {}

    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            grid_location = GridLocation(row, column)
            grid_locations.append(grid_location)
            value = input[row*GRID_SIZE + column]
            if value == ".":
                possible_values_by_location[grid_location] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                possible_values_by_location[grid_location] = []
                assignment[grid_location] = int(value)
    return grid_locations, possible_values_by_location, assignment


def display_grid(solution: Dict[GridLocation, int]) -> None:
    out = "\n"
    for row in range(GRID_SIZE):
        if row % 3 == 0:
            out += "| " + "- - - - - -  |  " * (GRID_SIZE // 3) + "\n\n"
        out += "| "
        for column in range(GRID_SIZE):
            out += str(solution.get(GridLocation(row, column), "*"))
            out += "    " if column % 3 != 2 else "  |  "
        out += " \n\n"
    out += "| " + "- - - - - -  |  " * (GRID_SIZE // 3) + "\n"
    print(out)


COUNTER = 0
PRINT_STEP = False
class SudokuConstraint(Constraint[GridLocation, List[int]]):
    def __init__(self, grid_location: GridLocation, grid_locations: List[GridLocation]) -> None:
        super().__init__([grid_location])
        self.grid_locations = grid_locations

    def __repr__(self) -> str:
        return "Constraint: " + " ".join(f"({grid_location.row}, {grid_location.column})" for grid_location in self.grid_locations)

    def satisfied(self, assignment: Dict[V, D]) -> bool:
        values = [assignment[grid_location] for grid_location in self.grid_locations if grid_location in assignment]
        result = len(set(values)) == len(values)

        global COUNTER
        COUNTER += 1
        if PRINT_STEP:
            print(f"step - {COUNTER}, satisfied - {result}")
            display_grid(assignment)
            print("============================================================")
        return result


def solve_sudoku(input: str) -> Optional[Dict[GridLocation, int]]:
    global COUNTER
    COUNTER = 0
    grid_locations, possible_values_by_location, assignment = parse_input(input)
    print("puzzle:")
    display_grid(assignment)

    csp: CSP[GridLocation, List[int]] = CSP(grid_locations, possible_values_by_location)

    for grid_location in grid_locations:
        # row constraint
        grid_location_rows = [GridLocation(grid_location.row, column) for column in range(GRID_SIZE)]
        csp.add_constraint(SudokuConstraint(grid_location, grid_location_rows))

        # column constraint
        grid_location_columns = [GridLocation(row, grid_location.column) for row in range(GRID_SIZE)]
        csp.add_constraint(SudokuConstraint(grid_location, grid_location_columns))

        # # box constraint
        start_row = grid_location.row - grid_location.row % 3
        start_column = grid_location.column - grid_location.column % 3
        grid_location_box = []
        for row in range(start_row, start_row + 3):
            for column in range(start_column, start_column + 3):
                grid_location_box.append(GridLocation(row, column))
        csp.add_constraint(SudokuConstraint(grid_location, grid_location_box))

    start = time.time()
    solution = csp.backtracking_search(assignment=assignment)
    duration = time.time() - start
    if solution:
        print(f"solution ({COUNTER} steps, {duration} seconds):")
        display_grid(solution)
    print("==================================================\n")
    return solution


if __name__ == "__main__":
    fb = open(sys.argv[1], 'rt')
    inputs = [line.strip("\n\r") for line in fb.readlines()]
    for input in inputs:
        solve_sudoku(input)
