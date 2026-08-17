import numpy as np
import plotly.graph_objects as go
import re


def is_valid_expression(expression):

    allowed_pattern = r"^[0-9xX+\-*/().^,\s_a-zA-Z]+$"

    return re.match(allowed_pattern, expression) is not None


def create_graph(expression):

    # Check the expression
    if not is_valid_expression(expression):
        raise ValueError("Invalid mathematical expression.")

    # Convert ^ to **
    expression = expression.replace("^", "**")

    # Create x values
    x = np.linspace(-10, 10, 400)

    # Functions available to the user
    allowed_functions = {
        "x": x,
        "np": np,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "exp": np.exp,
        "sqrt": np.sqrt,
        "log": np.log
    }

    # Calculate y values
    try:

        y = eval(
            expression,
            {"__builtins__": {}},
            allowed_functions
        )

    except Exception as e:

        raise ValueError(
            f"Could not understand the function: {e}"
        )


    # Create interactive Plotly figure
    fig = go.Figure()


    # Add the mathematical curve
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name=f"y = {expression}"
        )
    )


    # Configure the graph
    fig.update_layout(

        title=f"Graph of y = {expression}",

        xaxis_title="x",

        yaxis_title="y",

        height=600,

        width=None,

        hovermode="x unified",

        dragmode="pan",

        margin=dict(
            l=60,
            r=30,
            t=80,
            b=60
        )

    )


    # Make x-axis and y-axis visible
    fig.update_xaxes(
        zeroline=True,
        showgrid=True
    )

    fig.update_yaxes(
        zeroline=True,
        showgrid=True
    )


    # Create browser-ready HTML
    graph_html = fig.to_html(

        full_html=False,

        include_plotlyjs=True,

        config={

            "scrollZoom": True,

            "displayModeBar": True,

            "displaylogo": False,

            "responsive": True

        }

    )


    return graph_html