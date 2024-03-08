import pandas as pd
import os

d_calcs = pd.read_csv("d_calcs.csv")

print(d_calcs.head())

latex_finished = {}
d_eqn = "$d = \frac{\phi M_{n}}{0.9*A_{s}*f_{y}} + \frac{a}{2}$"


# d_calcs
def d_calcs_to_latex(df: pd.DataFrame, write_to_file: bool = False):
    """Converts the d_calcs dataframe to a latex formatted string"""
    for row in df.iterrows():
        typed_eqn = f"d = \\frac[\phi M_[n][[\phi A_[s] f_[y]] + \\frac[a][2] = \\frac[\phi ({row[1][3]})][0.9*(3.81)*(60000)] + \\frac[{row[1][5]}][2] = {row[1][4]}"
        typed_eqn = typed_eqn.replace("[", "{").replace("]", "}")
        latex_finished[row[1][1]] = {}
        latex_finished[row[1][1]][
            "explanation"
        ] = f"""Consider a typical {row[1][1]} beam. From analysis in SAP2000, the beam was found to experience a maximum moment of ${row[1][2]*-1}$. The depth $d$ of the Whitney Stress Block can be found with the following equation:"""
        latex_finished[row[1][1]]["d"] = typed_eqn
        if write_to_file:
            with open(f"d_calc_text/d_calcs_{row[1][1]}.tex", "w") as f:
                f.write(f'{latex_finished[row[1][1]]["explanation"]}\n {latex_finished[row[1][1]]["d"]}\n')


if __name__ == "__main__":
    d_calcs_to_latex(d_calcs)
    print(latex_finished['Roof, Long, Exterior side'])
