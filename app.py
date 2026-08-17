from flask import Flask, render_template, request
from maths.solver import solve_math
from maths.graph import create_graph
from maths.ai import get_math_answer, get_structured_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ai", methods=["GET", "POST"])
def ai():

    answer = None

    if request.method == "POST":

        question = request.form["question"]

        answer = get_structured_answer(question)

    return render_template(
        "ai.html",
        answer=answer
    )

@app.route("/solver", methods=["GET", "POST"])
def solver():

    result = None
    problem = ""

    if request.method == "POST":

        problem = request.form["problem"]

        operation = request.form["operation"]

        result = solve_math(
            problem,
            operation
        )

    return render_template(
        "solver.html",
        result=result,
        problem=problem
    )

@app.route("/graph", methods=["GET", "POST"])
def graph():

    graph_html = None
    expression = ""

    if request.method == "POST":

        expression = request.form["expression"]

        try:

            graph_html = create_graph(expression)

        except Exception as e:

            return render_template(
                "graph.html",
                graph_html=graph_html,
                expression=expression,
                error=str(e)
            )

    return render_template(
        "graph.html",
        graph_html=graph_html,
        expression=expression
    )

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/formulas")
def formulas():
    return render_template("formulas.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    questions = [

        # ==================================================
        # 1–3 : EUCLIDEAN ALGORITHM
        # ==================================================

        {
            "topic": "Euclidean Algorithm",
            "text": "What is GCD(12, 18)?",
            "options": ["2", "3", "6", "9"],
            "answer": "6",
            "explanation": "The greatest common divisor of 12 and 18 is 6."
        },

        {
            "topic": "Euclidean Algorithm",
            "text": "What is GCD(48, 18)?",
            "options": ["3", "6", "12", "18"],
            "answer": "6",
            "explanation": "48 = 18×2 + 12, 18 = 12×1 + 6, and 12 = 6×2 + 0. Therefore GCD = 6."
        },

        {
            "topic": "Euclidean Algorithm",
            "text": "In a = bq + r, what does r represent?",
            "options": ["Dividend", "Divisor", "Quotient", "Remainder"],
            "answer": "Remainder",
            "explanation": "In the division algorithm, r is the remainder and satisfies 0 ≤ r < b."
        },


        # ==================================================
        # 4–6 : CONGRUENCE
        # ==================================================

        {
            "topic": "Congruence",
            "text": "What does a ≡ b (mod n) mean?",
            "options": [
                "a + b is divisible by n",
                "a − b is divisible by n",
                "a × b is divisible by n",
                "a = b always"
            ],
            "answer": "a − b is divisible by n",
            "explanation": "a ≡ b (mod n) exactly when n divides (a − b)."
        },

        {
            "topic": "Congruence",
            "text": "Which statement is true?",
            "options": [
                "17 ≡ 5 (mod 12)",
                "17 ≡ 6 (mod 12)",
                "17 ≡ 7 (mod 12)",
                "17 ≡ 8 (mod 12)"
            ],
            "answer": "17 ≡ 5 (mod 12)",
            "explanation": "17 − 5 = 12, which is divisible by 12."
        },

        {
            "topic": "Congruence",
            "text": "What is 23 mod 5?",
            "options": ["2", "3", "4", "5"],
            "answer": "3",
            "explanation": "23 = 5×4 + 3, so the remainder is 3."
        },


        # ==================================================
        # 7–9 : LINEAR CONGRUENCE
        # ==================================================

        {
            "topic": "Linear Congruence",
            "text": "For ax ≡ b (mod n), when does a solution exist?",
            "options": [
                "gcd(a,n) divides b",
                "a divides n",
                "n divides a",
                "a = b"
            ],
            "answer": "gcd(a,n) divides b",
            "explanation": "The linear congruence ax ≡ b (mod n) has a solution exactly when gcd(a,n) divides b."
        },

        {
            "topic": "Linear Congruence",
            "text": "Which value satisfies 3x ≡ 6 (mod 9)?",
            "options": ["1", "2", "3", "5"],
            "answer": "2",
            "explanation": "3(2) = 6, and 6 ≡ 6 (mod 9)."
        },

        {
            "topic": "Linear Congruence",
            "text": "What is the gcd of 6 and 15?",
            "options": ["1", "2", "3", "5"],
            "answer": "3",
            "explanation": "The greatest number dividing both 6 and 15 is 3."
        },


        # ==================================================
        # 10–12 : FUNCTIONS
        # ==================================================

        {
            "topic": "Functions",
            "text": "Which function is also called a one-to-one function?",
            "options": [
                "Injective",
                "Surjective",
                "Constant",
                "Periodic"
            ],
            "answer": "Injective",
            "explanation": "An injective function maps different inputs to different outputs."
        },

        {
            "topic": "Functions",
            "text": "A function that is both injective and surjective is called:",
            "options": [
                "Constant",
                "Bijective",
                "Periodic",
                "Identity only"
            ],
            "answer": "Bijective",
            "explanation": "A bijective function is both one-to-one and onto."
        },

        {
            "topic": "Functions",
            "text": "For an injective function, if f(a) = f(b), then:",
            "options": [
                "a = b",
                "a > b",
                "a < b",
                "a = 0"
            ],
            "answer": "a = b",
            "explanation": "This is the defining property of an injective function."
        },


        # ==================================================
        # 13–16 : COMPLEX NUMBERS
        # ==================================================

        {
            "topic": "Complex Numbers",
            "text": "What is i²?",
            "options": ["1", "-1", "i", "0"],
            "answer": "-1",
            "explanation": "The imaginary unit is defined by i² = −1."
        },

        {
            "topic": "Complex Numbers",
            "text": "What is the modulus of z = 3 + 4i?",
            "options": ["3", "4", "5", "7"],
            "answer": "5",
            "explanation": "|z| = √(3² + 4²) = √25 = 5."
        },

        {
            "topic": "Complex Numbers",
            "text": "In z = a + bi, what does a represent?",
            "options": [
                "Imaginary part",
                "Real part",
                "Modulus",
                "Argument"
            ],
            "answer": "Real part",
            "explanation": "In a + bi, a is the real part and b is the coefficient of the imaginary part."
        },

        {
            "topic": "Complex Numbers",
            "text": "What is the value of (2 + 3i) + (4 + 2i)?",
            "options": [
                "6 + 5i",
                "6 + i",
                "2 + 5i",
                "8 + 6i"
            ],
            "answer": "6 + 5i",
            "explanation": "Add real parts and imaginary parts separately: (2+4) + (3+2)i = 6+5i."
        },


        # ==================================================
        # 17–20 : SEQUENCES & CONVERGENCE
        # ==================================================

        {
            "topic": "Sequences",
            "text": "What is the nth term of an arithmetic sequence?",
            "options": [
                "a₁ + nd",
                "a₁ + (n−1)d",
                "a₁n + d",
                "nd"
            ],
            "answer": "a₁ + (n−1)d",
            "explanation": "The nth term of an arithmetic sequence is aₙ = a₁ + (n−1)d."
        },

        {
            "topic": "Sequences",
            "text": "What happens to the sequence aₙ = 1/n as n approaches infinity?",
            "options": [
                "It approaches 0",
                "It approaches 1",
                "It approaches infinity",
                "It oscillates forever"
            ],
            "answer": "It approaches 0",
            "explanation": "As n becomes larger, 1/n becomes smaller and approaches 0."
        },

        {
            "topic": "Sequences",
            "text": "Does the sequence aₙ = (−1)ⁿ converge?",
            "options": [
                "Yes, to 0",
                "Yes, to 1",
                "No",
                "Yes, to −1"
            ],
            "answer": "No",
            "explanation": "The sequence alternates between −1 and 1 and never approaches a single value."
        },

        {
            "topic": "Sequences",
            "text": "What does lim(n→∞) aₙ = L mean?",
            "options": [
                "The sequence approaches L",
                "The sequence equals L for every n",
                "The sequence is always increasing",
                "The sequence is always decreasing"
            ],
            "answer": "The sequence approaches L",
            "explanation": "A sequence converges to L when its terms approach L as n becomes very large."
        },


        # ==================================================
        # 21–23 : LIMITS
        # ==================================================

        {
            "topic": "Limits",
            "text": "What is lim(x→2) x²?",
            "options": ["2", "4", "6", "8"],
            "answer": "4",
            "explanation": "Substituting x = 2 gives 2² = 4."
        },

        {
            "topic": "Limits",
            "text": "For a two-sided limit to exist, what must be true?",
            "options": [
                "Only the left limit exists",
                "Only the right limit exists",
                "Left and right limits are equal",
                "f(x) must equal 0"
            ],
            "answer": "Left and right limits are equal",
            "explanation": "A two-sided limit exists when the left-hand and right-hand limits exist and have the same value."
        },

        {
            "topic": "Limits",
            "text": "What does lim(x→a) f(x) = L describe?",
            "options": [
                "The value f(x) approaches as x approaches a",
                "The derivative at a",
                "The maximum value",
                "The minimum value"
            ],
            "answer": "The value f(x) approaches as x approaches a",
            "explanation": "A limit describes the value that f(x) approaches as x gets arbitrarily close to a."
        },


        # ==================================================
        # 24–26 : CONTINUITY
        # ==================================================

        {
            "topic": "Continuity",
            "text": "Which is a condition for continuity at x = a?",
            "options": [
                "f(a) exists",
                "f(a) must equal 0",
                "The derivative must exist",
                "The function must be quadratic"
            ],
            "answer": "f(a) exists",
            "explanation": "Continuity requires f(a) to exist, the limit to exist, and the limit to equal f(a)."
        },

        {
            "topic": "Continuity",
            "text": "For continuity at x = a, which equation must hold?",
            "options": [
                "lim(x→a)f(x) = f(a)",
                "f(a) = 0",
                "lim(x→a)f(x) = 1",
                "f(a) = a"
            ],
            "answer": "lim(x→a)f(x) = f(a)",
            "explanation": "The limiting value must equal the actual function value at a."
        },

        {
            "topic": "Continuity",
            "text": "Which function is continuous for every real x?",
            "options": [
                "f(x) = x²",
                "f(x) = 1/x",
                "f(x) = log(x)",
                "f(x) = 1/(x−2)"
            ],
            "answer": "f(x) = x²",
            "explanation": "Polynomial functions are continuous for every real number."
        },


        # ==================================================
        # 27–30 : PERMUTATIONS & COMBINATIONS
        # ==================================================

        {
            "topic": "Permutations",
            "text": "In a permutation, does order matter?",
            "options": [
                "Yes",
                "No",
                "Never",
                "Only when n = 1"
            ],
            "answer": "Yes",
            "explanation": "Permutations count arrangements where changing the order produces a different arrangement."
        },

        {
            "topic": "Permutations",
            "text": "What is 5P2?",
            "options": ["5", "10", "20", "25"],
            "answer": "20",
            "explanation": "5P2 = 5!/(5−2)! = 5!/3! = 5×4 = 20."
        },

        {
            "topic": "Combinations",
            "text": "What is 5C2?",
            "options": ["5", "10", "20", "25"],
            "answer": "10",
            "explanation": "5C2 = 5!/(2!3!) = 10."
        },

        {
            "topic": "Combinations",
            "text": "When are combinations used?",
            "options": [
                "When order matters",
                "When order does not matter",
                "Only for complex numbers",
                "Only for sequences"
            ],
            "answer": "When order does not matter",
            "explanation": "Combinations count selections where rearranging the selected objects does not create a new selection."
        }

    ]

    score = None
    user_answers = {}

    if request.method == "POST":

        score = 0

        for i, question in enumerate(questions):

            question_number = i + 1

            user_answer = request.form.get(
                f"q{question_number}"
            )

            user_answers[f"q{question_number}"] = user_answer

            if user_answer == question["answer"]:
                score += 1

    return render_template(
        "quiz.html",
        questions=questions,
        score=score,
        user_answers=user_answers
    )
   
   

if __name__ == "__main__":
    app.run(debug=True)