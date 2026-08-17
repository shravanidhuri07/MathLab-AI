import sympy as sp


def solve_math(problem, operation):

    x = sp.symbols('x')

    problem = problem.strip()

    if not problem:
        return {
            "title": "No Problem Entered",
            "steps": [],
            "answer": "Please enter a mathematical problem."
        }

    try:

        # =====================================================
        # SOLVE EQUATION
        # =====================================================

        if operation == "solve":

            if "=" in problem:

                left, right = problem.split("=", 1)

                left = sp.sympify(left)
                right = sp.sympify(right)

                equation = sp.Eq(left, right)

                expression = left - right

            else:

                expression = sp.sympify(problem)

                equation = sp.Eq(expression, 0)

            solutions = sp.solve(equation, x)

            steps = []

            steps.append(
                f"Original equation: {equation}"
            )

            steps.append(
                f"Move everything to one side: {sp.expand(expression)} = 0"
            )

            if expression.as_poly(x) is not None:

                poly = sp.Poly(expression, x)

                degree = poly.degree()

                steps.append(
                    f"This is a polynomial equation of degree {degree}."
                )

            factored = sp.factor(expression)

            if factored != expression:

                steps.append(
                    f"Factor the equation: {factored} = 0"
                )

            steps.append(
                "Set each factor equal to zero and solve for x."
            )

            if solutions:

                answer = ", ".join(
                    [f"x = {s}" for s in solutions]
                )

            else:

                answer = "No real solution found."

            return {
                "title": "Equation Solver",
                "steps": steps,
                "answer": answer
            }


        # =====================================================
        # SIMPLIFY
        # =====================================================

        elif operation == "simplify":

            expression = sp.sympify(problem)

            simplified = sp.simplify(expression)

            steps = [
                f"Original expression: {expression}",
                "Apply algebraic simplification.",
                f"Simplified expression: {simplified}"
            ]

            return {
                "title": "Simplification",
                "steps": steps,
                "answer": str(simplified)
            }


        # =====================================================
        # EXPAND
        # =====================================================

        elif operation == "expand":

            expression = sp.sympify(problem)

            expanded = sp.expand(expression)

            steps = [
                f"Original expression: {expression}",
                "Multiply out the brackets.",
                f"Expanded form: {expanded}"
            ]

            return {
                "title": "Expansion",
                "steps": steps,
                "answer": str(expanded)
            }


        # =====================================================
        # FACTOR
        # =====================================================

        elif operation == "factor":

            expression = sp.sympify(problem)

            factored = sp.factor(expression)

            steps = [
                f"Original expression: {expression}",
                "Look for common factors and algebraic patterns.",
                f"Factored form: {factored}"
            ]

            return {
                "title": "Factorization",
                "steps": steps,
                "answer": str(factored)
            }


        # =====================================================
        # DIFFERENTIATION
        # =====================================================

        elif operation == "differentiate":

            expression = sp.sympify(problem)

            derivative = sp.diff(expression, x)

            steps = [
                f"Given function: f(x) = {expression}",
                "Differentiate with respect to x.",
                f"Using standard differentiation rules:",
                f"f'(x) = {derivative}"
            ]

            return {
                "title": "Differentiation",
                "steps": steps,
                "answer": str(derivative)
            }


        # =====================================================
        # INTEGRATION
        # =====================================================

        elif operation == "integrate":

            expression = sp.sympify(problem)

            integral = sp.integrate(expression, x)

            steps = [
                f"Given function: f(x) = {expression}",
                "Integrate with respect to x.",
                f"Using integration rules:",
                f"∫ f(x) dx = {integral} + C"
            ]

            return {
                "title": "Integration",
                "steps": steps,
                "answer": f"{integral} + C"
            }


        # =====================================================
        # LIMIT
        # =====================================================

        elif operation == "limit":

            expression = sp.sympify(problem)

            limit_value = sp.limit(
                expression,
                x,
                0
            )

            steps = [
                f"Given function: f(x) = {expression}",
                "Find the limit as x approaches 0.",
                f"lim(x→0) f(x) = {limit_value}"
            ]

            return {
                "title": "Limit",
                "steps": steps,
                "answer": str(limit_value)
            }


        else:

            return {
                "title": "Unknown Operation",
                "steps": [],
                "answer": "Please select a valid mathematical operation."
            }


    except Exception as e:

        return {
            "title": "Unable to Solve",
            "steps": [
                "Check that the mathematical expression is written correctly.",
                "Use * for multiplication.",
                "Use ** for powers."
            ],
            "answer": f"Input error: {str(e)}"
        }