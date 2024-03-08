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
        ] = f"""Now that $d$ has been located, shear calculations can begin. From SAP2000, the typical Roof, Long, Exterior Side beam was found to have a max factored applied shear of $\phi * V_[u] = {abs(row[1][2])}$. To find the minimum strength needed from shear stirrups, the relationship $V_[u] \leq V_[s] + V_[c]$ can be rewritten as $V_[s] \geq V_[u] - V_[c]$. The shear strength of the beam, $V_[c]$, can be found using the following calculation:"""
        latex_finished[row[1][0]]["explanation_1"] = (
            latex_finished[row[1][0]]["explanation_1"]
            .replace("[", "{")
            .replace("]", "}")
        )
        shear_capacity_eqn = f"""\\begin[equation] \nV_[c] = \phi * 2 \lambda \sqrt[f'_[c](psi)] b_[w] d = V_[c] = 0.75 * 2 * 1 * \sqrt[3000psi] * 12 in *  {row[1][12]} in = {row[1][4]} lbs = {row[1][5]} kips \n\end[equation]"""
        shear_capacity_eqn = shear_capacity_eqn.replace("[", "{").replace("]", "}")
        latex_finished[row[1][0]]["Vc"] = shear_capacity_eqn

        # Explain second step, equation for minimum shear strength needed from shear stirrups
        latex_finished[row[1][0]][
            "explanation_2"
        ] = f"""With the shear strength of the beam found, the minimum shear strength needed from shear stirrups can be found using the following calculation:"""
        min_stirrup_strength = f"""\\begin[equation] \n\phi V_[s, min] = \phi V_[u] - \phi V_[c] = \\frac[{abs(row[1][2])} - {row[1][5]}][\phi = 0.75] = {row[1][9]} kips \n\end[equation]"""
        min_stirrup_strength = min_stirrup_strength.replace("[", "{").replace("]", "}")
        latex_finished[row[1][0]]["min_stirrup_strength"] = min_stirrup_strength

        # Explain third step, max shear capacity of stirrups
        latex_finished[row[1][0]][
            "explanation_3"
        ] = f"""Now that the minimum shear capacity of the stirrups has been determined, the strength limit to allow for a tension controlled failure shall be determined. The maximum shear capacity of the stirrups can be found using the following calculation:"""
        max_stirrup_capacity = f"""\\begin[equation] \nV_[s, max] = 8 \sqrt[f'_[c]] b_[w]d = 8 \sqrt[3000 psi] * 12 in * {row[1][12]} in = {row[1][10]} kips \n\end[equation]"""
        max_stirrup_capacity = max_stirrup_capacity.replace("[", "{").replace("]", "}")
        latex_finished[row[1][0]]["max_stirrup_capacity"] = max_stirrup_capacity

        if write_to_file:
            with open(f"shear_calc_text/shear_calcs_{row[1][0]}.text", "w") as f:
                f.write(
                    f"{latex_finished[row[1][0]]['explanation_1']}\n"
                    f"{latex_finished[row[1][0]]['Vc']}\n"
                    f"{latex_finished[row[1][0]]['explanation_2']}\n"
                    f"{latex_finished[row[1][0]]['min_stirrup_strength']}\n"
                    f"{latex_finished[row[1][0]]['explanation_3']}\n"
                    f"{latex_finished[row[1][0]]['max_stirrup_capacity']}\n"
                )
    return latex_finished


if __name__ == "__main__":
    output = shear_calcs_to_latex(shear_calcs, True)
    print(output["R1"])
