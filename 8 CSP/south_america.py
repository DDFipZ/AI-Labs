from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        suv = self.select_unassigned_variable(assignment)
        for x in self.order_domain_values(suv, assignment):
            if self.is_consistent(suv, x, assignment):
                assignment[suv] = x
                result = self.recursive_backtracking(assignment)
                if result != False:
                    return result
                assignment.pop(suv)
        return False

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_south_america_csp():
    columbia, venezuela, ecuador, guyana, suriname, guyane_fr = "columbia", "venezuela", "ecuador", "guyana", "suriname", "guyane_fr"
    peru, brazil, bolivia, paraguay, chile, argentina, uruguay  = "peru", "brazil", "bolivia", "paraguay", "chile", "argentina", "uruguay"
    values = ['Red', 'Green', 'Blue', "Yellow"]
    variables = [
                    columbia, venezuela, ecuador, guyana, suriname, guyane_fr,
                    peru, brazil, bolivia, paraguay, chile, argentina, uruguay
                ]
    domains = {
        columbia: values[:],
        venezuela: values[:],
        ecuador: values[:],
        guyana: values[:],
        suriname: values[:],
        guyane_fr: values[:],
        peru: values[:],
        brazil: values[:],
        bolivia: values[:],
        paraguay: values[:],
        chile: values[:],
        argentina: values[:],
        uruguay: values[:],
    }
    neighbours = {
        columbia: [venezuela, ecuador, brazil, peru],
        venezuela: [columbia, guyana, brazil],
        ecuador: [columbia, peru],
        guyana: [suriname, venezuela, brazil],
        suriname: [guyana, brazil, guyane_fr],
        guyane_fr: [suriname, brazil],
        peru: [columbia, ecuador, bolivia, chile],
        brazil: [guyane_fr, suriname, guyana, venezuela, columbia, peru, bolivia, paraguay, uruguay],
        bolivia: [brazil, paraguay, argentina, chile, peru],
        paraguay: [brazil, bolivia, argentina],
        chile: [peru, bolivia, argentina],
        argentina: [chile, bolivia, paraguay, brazil, uruguay],
        uruguay: [brazil, argentina]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        columbia: constraint_function,
        venezuela: constraint_function,
        ecuador: constraint_function,
        guyana: constraint_function,
        suriname: constraint_function,
        guyane_fr: constraint_function,
        peru: constraint_function,
        brazil: constraint_function,
        bolivia: constraint_function,
        paraguay: constraint_function,
        chile: constraint_function,
        argentina: constraint_function,
        uruguay: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))