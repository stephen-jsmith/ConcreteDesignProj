import pandas as pd


shear_calcs = pd.read_csv("shear_calcs.csv")
s_calcs = pd.read_csv("s_calcs.csv")

print(shear_calcs.head())


d_eqn = "$d = \frac{\phi M_{n}}{0.9*A_{s}*f_{y}} + \frac{a}{2}$"


# d_calcs
def s_calcs_to_latex(
    df: pd.DataFrame, shear: pd.DataFrame, write_to_file: bool = False
):
    """Converts the s_calcs dataframe to a latex formatted string"""
    latex_finished = {}
    for row in df.iterrows():
        latex_finished[row[1][0]] = {}
        # Explain first step, equation for stirrup spacing of concrete
        latex_finished[row[1][0]][
            "explanation_1"
        ] = """Now that the shear calculations have been finalized, stirrup spacing calculations can begin. """
        if row[1][12] == 2:
            # First case, where 0.5phiV_c < V_u < phiV_c
            latex_finished[row[1][0]][
                "explanation_1"
            ] += f"In this case, $0.5 \phi V_[c] < V_[u] = {row[1][2]} < \phi V_[c]$, so $s$ is based on maixmum spacing rules. As per the tables from the lecture notes, $A_[v,min]$ is not required, so $s$ will be based on \n \\begin[equation] \n_[min](\\frac[d][2],\\frac[A_[v]f_[yt](psi)][0.75\sqrt[f'_[c](psi)]b_[w]]\n\end[equation]:"
            latex_finished[row[1][0]]["explanation_1"] = (
                latex_finished[row[1][0]]["explanation_1"]
                .replace("[", "{")
                .replace("]", "}")
            )
            latex_finished[row[1][0]][
                "s"
            ] = f"\\begin[equation] \n s = _min(\\frac[d][2] = \\frac[{row[1][11]} in][2] = {row[1][3]}in, \\frac[A_[v]f_[yt]][0.75\sqrt[f'_[c]]b_[w]] = \\frac[0.22 in^2 *60000psi][0.75 \sqrt[3000psi]*12in] = 26.78in) = {row[1][3]}in \n \\end[equation]"
            latex_finished[row[1][0]]["s"] = (
                latex_finished[row[1][0]]["s"].replace("[", "{").replace("]", "}")
            )
        elif row[1][12] == 3:
            latex_finished[row[1][0]][
                "explanation_1"
            ] += "In this case, $\phi V_{c} < V_{u}$, so $s$ is based on strength needed to resist shear. As per the tables from the lecture notes, $A_[v,min]$ is not required, so $s$ will be based on \n \\begin[equation] \n_[min](\\frac[A_[v]f_[y]d][V_[s,req]],\\frac[A_[v]f_[yt](psi)][0.75\sqrt[f'_[c](psi)]b_[w]]\n\end[equation]:"
            latex_finished[row[1][0]]["explanation_1"] = (
                latex_finished[row[1][0]]["explanation_1"]
                .replace("[", "{")
                .replace("]", "}")
            )
            latex_finished[row[1][0]][
                "s"
            ] = f"\\begin[equation] \n s = _[min](\\frac[A_[v]f_[y]d][V_[s,req]] = \\frac[0.22 in^2 *60ksi*{row[1][11]} in][{row[1][2]} kips]={row[1][3]},\\frac[A_[v]f_[yt](psi)][0.75\sqrt[f'_[c](psi)]b_[w]] = \\frac[0.22 in^2 *60000psi][0.75 \sqrt[3000psi]*12in] = 26.78in) = {row[1][3]}in \n \\end[equation]"
            latex_finished[row[1][0]]["s"] = (
                latex_finished[row[1][0]]["s"].replace("[", "{").replace("]", "}")
            )

    return latex_finished


if __name__ == "__main__":
    output = s_calcs_to_latex(s_calcs, True)
    print(output["R1"])
