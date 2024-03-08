import pandas as pd


shear_calcs = pd.read_csv("shear_calcs.csv")

print(shear_calcs.head())


d_eqn = "$d = \frac{\phi M_{n}}{0.9*A_{s}*f_{y}} + \frac{a}{2}$"


# d_calcs
def shear_calcs_to_latex(df: pd.DataFrame, write_to_file: bool = False):
    """Converts the shear_calcs dataframe to a latex formatted string"""
    latex_finished = {}
    for row in df.iterrows():
        latex_finished[row[1][0]] = {}
        # Explain first step, equation for shear capacity of concrete
        latex_finished[row[1][0]][
            "explanation_1"
        ] = f"""Now that the shear calculations have been finalized, stirrup spacing calculations can begin. """
        latex_finished[row[1][0]]["explanation_1"] = (
            latex_finished[row[1][0]]["explanation_1"]
            .replace("[", "{")
            .replace("]", "}")
        )
    return latex_finished


if __name__ == "__main__":
    output = shear_calcs_to_latex(shear_calcs, True)
    print(output["R1"])
