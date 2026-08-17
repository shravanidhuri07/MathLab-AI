def topic_answer(title, definition, explanation, formula,
                 conditions, steps, example, important):

    return {
        "title": title,
        "definition": definition,
        "explanation": explanation,
        "formula": formula,
        "conditions": conditions,
        "steps": steps,
        "example": example,
        "important": important
    }

def get_math_answer(question):

    question = question.lower()

    if "euclid" in question or "gcd" in question:
       return topic_answer(
    "Euclid's Algorithm",

    "Euclid's Algorithm is a method for finding the Greatest Common Divisor (GCD) of two integers.",

    "The algorithm repeatedly divides the larger number by the smaller number. "
    "The remainder becomes the divisor in the next step. "
    "When the remainder becomes zero, the last non-zero divisor is the GCD.",

    "a = bq + r, where 0 ≤ r < b",

    "It can be applied to two integers a and b, with b ≠ 0. "
    "It is useful for finding GCDs and is also used in solving certain "
    "linear congruences and finding modular inverses.",

    [
        "Divide the larger number by the smaller number.",
        "Write down the remainder.",
        "Use the previous divisor and remainder for the next division.",
        "Continue until the remainder becomes 0.",
        "The last non-zero remainder is the GCD."
    ],

    "Find GCD(252, 105):\n"
    "252 = 2 × 105 + 42\n"
    "105 = 2 × 42 + 21\n"
    "42 = 2 × 21 + 0\n\n"
    "Therefore, GCD(252, 105) = 21.",

    "The final non-zero remainder is the GCD."
) 

    elif "complex number" in question:
        return """
A complex number has the form:

z = a + bi

where a and b are real numbers and i² = -1.

For example:

z = 3 + 4i

Here, 3 is the real part and 4 is the imaginary part.

The modulus is:

|z| = √(a² + b²)

For 3 + 4i:

|z| = √(3² + 4²) = 5
"""

    elif "de moivre" in question:
        return """
De Moivre's Theorem connects complex numbers in polar form with powers.

The theorem states:

(cos θ + i sin θ)^n
= cos(nθ) + i sin(nθ)

It is particularly useful for calculating powers and roots of complex numbers.
"""

    elif "permutation" in question:
        return """
A permutation is an arrangement where the order matters.

The number of ways to arrange r objects from n objects is:

nPr = n! / (n-r)!

For example:

5P2 = 5! / 3!
    = 5 × 4
    = 20
"""

    elif "combination" in question:
        return """
A combination is a selection where the order does not matter.

The formula is:

nCr = n! / (r!(n-r)!)

For example:

5C2 = 5! / (2!3!)
    = 10

Therefore, there are 10 ways to select 2 objects from 5.
"""

    elif "injective" in question or "one-one" in question:
        return """
An injective function is a function in which different elements of the
domain have different images.

In simple terms:

If f(a) = f(b), then a = b.

Therefore, no two different inputs can have the same output.
"""

    elif "surjective" in question or "onto" in question:
        return """
A surjective function is a function in which every element of the codomain
has at least one element from the domain mapping to it.

In simple terms:

Every possible output must be reached by at least one input.
"""

    elif "limit" in question:
        return """
A limit describes the value that a function approaches as the input
approaches a particular value.

For example:

lim(x→2) x² = 4

because as x gets closer and closer to 2, x² gets closer and closer to 4.
"""

    elif "continuity" in question:
        return """
A function is continuous at x = a if:

1. f(a) exists.
2. lim(x→a) f(x) exists.
3. lim(x→a) f(x) = f(a).

Intuitively, a continuous graph can be drawn near that point without lifting
your pen from the paper.
"""

    elif "sequence" in question:
        return """
A sequence is an ordered list of numbers.

Example:

2, 4, 6, 8, 10, ...

This is an arithmetic sequence because the common difference is 2.

The nth term of an arithmetic sequence is:

aₙ = a₁ + (n-1)d
"""
    elif "integer" in question or "divisibility" in question:
        return """
Integers are whole numbers including positive numbers, negative numbers
and zero.

Examples:

..., -3, -2, -1, 0, 1, 2, 3, ...

Divisibility means determining whether one integer can be divided by another
without leaving a remainder.

For example:

24 is divisible by 6 because:

24 ÷ 6 = 4

Therefore, 6 divides 24.
"""


    elif "congruence" in question or "modulo" in question:
        return """
Two integers a and b are congruent modulo n if they have the same remainder
when divided by n.

The notation is:

a ≡ b (mod n)

This means:

n divides (a - b).

For example:

17 ≡ 5 (mod 12)

because:

17 - 5 = 12

and 12 is divisible by 12.
"""


    elif "function" in question and "injective" not in question and "surjective" not in question:
        return """
A function maps every element of a domain to exactly one element of a
codomain.

We write:

f : A → B

where:

A = domain
B = codomain

Important terms:

Domain = set of allowed inputs
Codomain = set containing possible outputs
Range = set of actual outputs produced by the function.
"""


    elif "bijective" in question:
        return """
A bijective function is both injective and surjective.

Therefore:

Bijective = Injective + Surjective

Every element of the codomain has exactly one corresponding element
in the domain.

A bijective function has an inverse function.
"""


    elif "inverse image" in question:
        return """
The inverse image of a set under a function contains all input elements
whose outputs belong to that set.

If:

f : A → B

and C is a subset of B, then the inverse image is:

f⁻¹(C) = {x ∈ A : f(x) ∈ C}

It is the set of inputs that map into C.
"""


    elif "multiset" in question:
        return """
A multiset is a collection in which elements are allowed to occur more
than once.

For example:

{A, A, B, C, C}

contains repeated elements.

When calculating permutations of a multiset, repeated elements must be
accounted for.

If there are n total objects with repetitions n₁, n₂, ..., nₖ, then:

Number of distinct permutations =
n! / (n₁! n₂! ... nₖ!)
"""


    elif "arithmetic of continuous" in question or "continuous function" in question:
        return """
Continuous functions can be combined using normal arithmetic operations.

If f and g are continuous at a point, then:

f + g
f - g
f × g

are also continuous at that point.

The quotient:

f / g

is continuous wherever g(x) ≠ 0.
"""


    elif "limit" in question and "function" in question:
        return """
The limit of a function describes the value that the function approaches
as x approaches a particular value.

We write:

lim(x→a) f(x) = L

This means that f(x) approaches L as x approaches a.

For example:

lim(x→2) x² = 4.
"""

    elif "linear congruence" in question:
        return """
A linear congruence has the form:

ax ≡ b (mod n)

To solve it, first calculate:

d = gcd(a, n)

A solution exists only if d divides b.

If gcd(a, n) = 1, then a has a multiplicative inverse modulo n.

For example:

3x ≡ 6 (mod 9)

Since:

gcd(3, 9) = 3

and 3 divides 6, solutions exist.

Linear congruences are closely connected to modular arithmetic and the
Euclidean Algorithm.
"""

    else:
        return """
I can currently help with topics from the MathLab AI syllabus such as:

• Integers and divisibility
• Euclid's Algorithm
• Congruence
• Complex Numbers
• De Moivre's Theorem
• Permutations
• Combinations
• Functions
• Injective and Surjective Functions
• Limits
• Continuity
• Sequences

Try asking about one of these topics.
"""

def get_structured_answer(question):

    question = question.lower()

    topics = {

        "integers": {
            "title": "Integers and Divisibility",
            "definition": "Integers are positive numbers, negative numbers and zero.",
            "explanation": "Divisibility studies whether one integer can be divided by another without leaving a remainder.",
            "formula": "a divides b if b = ak for some integer k.",
            "conditions": "The divisor must be a non-zero integer.",
            "steps": [
                "Identify the dividend and divisor.",
                "Perform the division.",
                "Check whether the remainder is zero.",
                "If the remainder is zero, the divisor divides the number."
            ],
            "example": "24 ÷ 6 = 4, so 6 divides 24.",
            "important": "A number is divisible by another number exactly when the remainder is zero."
        },


        "congruence": {
            "title": "Properties of Congruences",
            "definition": "Two integers a and b are congruent modulo n if n divides their difference.",
            "explanation": "Congruence is the foundation of modular arithmetic and is used when numbers are considered according to their remainders.",
            "formula": "a ≡ b (mod n)  ⇔  n | (a − b)",
            "conditions": "The modulus n must be a positive integer.",
            "steps": [
                "Subtract the two integers.",
                "Check whether the modulus divides the difference.",
                "If it does, the integers are congruent modulo n."
            ],
            "example": "17 ≡ 5 (mod 12) because 17 − 5 = 12.",
            "important": "Congruent numbers have the same remainder when divided by the modulus."
        },


        "linear congruence": {
            "title": "Linear Congruences",
            "definition": "A linear congruence has the form ax ≡ b (mod n).",
            "explanation": "Linear congruences are solved using modular arithmetic and sometimes the Euclidean Algorithm.",
            "formula": "ax ≡ b (mod n)",
            "conditions": "A solution exists when gcd(a,n) divides b.",
            "steps": [
                "Calculate gcd(a,n).",
                "Check whether gcd(a,n) divides b.",
                "If it does, simplify the congruence.",
                "Find the modular inverse when appropriate.",
                "Determine x modulo n."
            ],
            "example": "3x ≡ 6 (mod 9) has solutions because gcd(3,9)=3 and 3 divides 6.",
            "important": "Always check gcd(a,n) before trying to find the solution."
        },


        "complex number": {
            "title": "Complex Numbers",
            "definition": "A complex number has the form z = a + bi, where a and b are real numbers and i² = −1.",
            "explanation": "The number a is the real part and b is the imaginary coefficient. Complex numbers can also be represented geometrically on the complex plane.",
            "formula": "|z| = √(a² + b²)",
            "conditions": "A complex number is written using a real part and an imaginary part.",
            "steps": [
                "Identify the real part a.",
                "Identify the imaginary coefficient b.",
                "Calculate the modulus if required.",
                "For polar form, calculate the argument θ."
            ],
            "example": "For z = 3 + 4i, |z| = √(3² + 4²) = 5.",
            "important": "Remember that i² = −1."
        },


        "polar": {
            "title": "Polar Form of Complex Numbers",
            "definition": "Polar form represents a complex number using its modulus and argument.",
            "explanation": "Instead of z = a + bi, a complex number can be represented using its distance from the origin and its angle.",
            "formula": "z = r(cos θ + i sin θ), where r = √(a²+b²)",
            "conditions": "The argument depends on the quadrant containing the complex number.",
            "steps": [
                "Calculate r = √(a²+b²).",
                "Calculate θ = tan⁻¹(b/a), adjusting for the correct quadrant.",
                "Write z in polar form."
            ],
            "example": "For z = 1 + i, r = √2 and θ = π/4, so z = √2(cos π/4 + i sin π/4).",
            "important": "Always check the quadrant when finding the argument."
        },


        "de moivre": {
            "title": "De Moivre's Theorem",
            "definition": "De Moivre's theorem gives a formula for powers of complex numbers written in polar form.",
            "explanation": "It converts powers of complex numbers into multiplication of their arguments.",
            "formula": "(cos θ + i sin θ)^n = cos(nθ) + i sin(nθ)",
            "conditions": "The complex number should be represented in polar/trigonometric form.",
            "steps": [
                "Convert the complex number to polar form.",
                "Raise the modulus to the required power.",
                "Multiply the argument by the power.",
                "Convert back to rectangular form if required."
            ],
            "example": "(cos θ + i sin θ)^3 = cos(3θ) + i sin(3θ).",
            "important": "Multiply the angle by n, but raise the modulus to n."
        },


        "sequence": {
            "title": "Sequences and Convergence",
            "definition": "A sequence is an ordered list of numbers indexed by positive integers.",
            "explanation": "A sequence may converge when its terms approach a finite number as n becomes very large.",
            "formula": "A sequence (aₙ) converges to L if lim(n→∞) aₙ = L.",
            "conditions": "For convergence, the sequence must approach a single finite limit.",
            "steps": [
                "Identify the general term.",
                "Study what happens as n approaches infinity.",
                "Calculate the limit if it exists.",
                "If the limit is finite, the sequence converges."
            ],
            "example": "aₙ = 1/n converges to 0 because lim(n→∞) 1/n = 0.",
            "important": "A sequence does not converge merely because its terms become smaller; its limit must exist."
        },


        "permutation": {
            "title": "Permutations",
            "definition": "A permutation is an arrangement of objects where order matters.",
            "explanation": "Changing the order of selected objects creates a different permutation.",
            "formula": "nPr = n! / (n−r)!",
            "conditions": "Use permutations when the order of selected objects matters.",
            "steps": [
                "Identify n, the total number of objects.",
                "Identify r, the number being arranged.",
                "Use nPr = n!/(n−r)!."
            ],
            "example": "5P2 = 5! / 3! = 5 × 4 = 20.",
            "important": "Permutation means arrangement: order matters."
        },


        "combination": {
            "title": "Combinations",
            "definition": "A combination is a selection of objects where order does not matter.",
            "explanation": "Selecting A and B is the same combination as selecting B and A.",
            "formula": "nCr = n! / [r!(n−r)!]",
            "conditions": "Use combinations when the order of selection does not matter.",
            "steps": [
                "Identify n and r.",
                "Determine whether order matters.",
                "If order does not matter, use nCr.",
                "Substitute the values into the formula."
            ],
            "example": "5C2 = 5!/(2!3!) = 10.",
            "important": "Combination means selection: order does not matter."
        },


        "multiset": {
            "title": "Permutations of Multisets",
            "definition": "A multiset is a collection in which some elements can occur more than once.",
            "explanation": "Repeated elements make some arrangements identical, so we divide by the factorials of the repetition counts.",
            "formula": "Number of arrangements = n!/(n₁!n₂!...nₖ!)",
            "conditions": "Use this formula when objects contain repeated identical elements.",
            "steps": [
                "Count the total number of objects.",
                "Count the repetitions of each identical object.",
                "Calculate n!.",
                "Divide by the factorial of every repetition count."
            ],
            "example": "The letters of AAB can be arranged in 3!/2! = 3 distinct ways.",
            "important": "Repeated objects must not be counted as different."
        },


        "injective": {
            "title": "Injective Function",
            "definition": "A function is injective if different inputs always produce different outputs.",
            "explanation": "No two different elements of the domain can map to the same element of the codomain.",
            "formula": "f(a) = f(b) ⇒ a = b",
            "conditions": "Every output has at most one corresponding input.",
            "steps": [
                "Take two arbitrary domain elements a and b.",
                "Assume f(a) = f(b).",
                "Show that this implies a = b.",
                "Therefore the function is injective."
            ],
            "example": "f(x)=2x is injective over the real numbers.",
            "important": "Injective means one-to-one."
        },


        "surjective": {
            "title": "Surjective Function",
            "definition": "A function is surjective if every element of the codomain has at least one preimage in the domain.",
            "explanation": "There are no unused elements in the codomain.",
            "formula": "For every y ∈ B, there exists x ∈ A such that f(x)=y.",
            "conditions": "Every element of the codomain must be reached.",
            "steps": [
                "Take an arbitrary element y from the codomain.",
                "Find an x in the domain such that f(x)=y.",
                "If this is possible for every y, the function is surjective."
            ],
            "example": "f(x)=x³ from R to R is surjective.",
            "important": "Surjective means onto."
        },


        "bijective": {
            "title": "Bijective Function",
            "definition": "A function is bijective when it is both injective and surjective.",
            "explanation": "Every codomain element corresponds to exactly one domain element.",
            "formula": "Bijective = Injective + Surjective",
            "conditions": "The function must satisfy both one-to-one and onto properties.",
            "steps": [
                "Check whether the function is injective.",
                "Check whether the function is surjective.",
                "If both conditions hold, the function is bijective."
            ],
            "example": "f(x)=x+1 from R to R is bijective.",
            "important": "A bijective function has an inverse function."
        },


        "inverse image": {
            "title": "Inverse Images of Sets",
            "definition": "The inverse image of a set contains all inputs whose function values belong to that set.",
            "explanation": "If C is a subset of the codomain, its inverse image contains every x that maps into C.",
            "formula": "f⁻¹(C) = {x ∈ A : f(x) ∈ C}",
            "conditions": "The set C must be a subset of the codomain.",
            "steps": [
                "Identify the target set C.",
                "Find the inputs that map into C.",
                "Collect those inputs into the inverse image."
            ],
            "example": "For f(x)=x², the inverse image of {4} is {-2, 2}.",
            "important": "Inverse image is not necessarily the same thing as an inverse function."
        },


        "limit": {
            "title": "Limit of a Function",
            "definition": "The limit describes the value a function approaches as its input approaches a particular value.",
            "explanation": "A limit studies the behavior near a point rather than necessarily the value exactly at that point.",
            "formula": "lim(x→a) f(x) = L",
            "conditions": "The limit must approach the same value from both sides for a two-sided limit to exist.",
            "steps": [
                "Identify the point x approaches.",
                "Evaluate the behavior from the left.",
                "Evaluate the behavior from the right.",
                "If both approaches give the same value, the limit exists."
            ],
            "example": "lim(x→2) x² = 4.",
            "important": "The function does not necessarily need to be defined at the point for a limit to exist."
        },


        "continuity": {
            "title": "Continuity of a Function",
            "definition": "A function is continuous at x=a if its value, limit and function behavior agree at that point.",
            "explanation": "Informally, a continuous graph has no break, hole or jump at the point being considered.",
            "formula": "f(a) exists, lim(x→a)f(x) exists, and lim(x→a)f(x)=f(a)",
            "conditions": "All three continuity conditions must hold at the point.",
            "steps": [
                "Check whether f(a) exists.",
                "Calculate lim(x→a) f(x).",
                "Check whether the limit exists.",
                "Compare the limit with f(a)."
            ],
            "example": "Polynomial functions such as f(x)=x² are continuous for every real x.",
            "important": "A function is continuous at a point only when all three conditions are satisfied."
        },


        "arithmetic of continuous": {
            "title": "Arithmetic of Continuous Functions",
            "definition": "Arithmetic operations on continuous functions generally produce continuous functions wherever the operations are defined.",
            "explanation": "Sums, differences and products of continuous functions remain continuous. Quotients are continuous where the denominator is non-zero.",
            "formula": "f±g, fg are continuous; f/g is continuous where g(x) ≠ 0.",
            "conditions": "For division, the denominator must not equal zero.",
            "steps": [
                "Check that the original functions are continuous.",
                "Identify the arithmetic operation.",
                "For division, check that the denominator is non-zero.",
                "Apply the corresponding continuity rule."
            ],
            "example": "If f(x)=x² and g(x)=x+1, then f(x)+g(x) is continuous everywhere.",
            "important": "Division requires special attention to points where the denominator is zero."
        }
    }

    for keyword, answer in topics.items():

        if keyword in question:
            return answer
    if "one-one and onto" in question:
        return topics["bijective"]

    if "one-one" in question or "one to one" in question:
        return topics["injective"]

    if "onto" in question:
        return topics["surjective"]
   
    return {
        "title": "Topic Not Found",
        "definition": "I could not identify the requested syllabus topic.",
        "explanation": "Try asking about one of the topics covered by MathLab AI.",
        "formula": "Not applicable",
        "conditions": "Ask using a topic name from the syllabus.",
        "steps": [
            "Try using the exact topic name.",
            "For example: Explain permutations.",
            "Or: What is continuity?"
        ],
        "example": "Example question: Explain Euclid's Algorithm.",
        "important": "The tutor currently covers the mathematics topics listed in your syllabus."
    }