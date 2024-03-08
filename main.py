from s_calcs import *
from shear_calcs import *
from d_calcs_to_latex import *

if __name__ == "__main__":
    dput = d_calcs_to_latex(d_calcs, False)
    shearput = shear_calcs_to_latex(s_calcs, False)
    sput = s_calcs_to_latex(s_calcs, False)

    with open("paper.text", "w") as f:
        for i in dput.keys():
            subsection_title = f'\subsection[{dput[i]["name"]}]'
            subsection_title = subsection_title.replace("[", "{").replace("]", "}")
            f.write(subsection_title)
            # Write d calculations
            f.write(f'{dput[i]["explanation"]}\n {dput[i]["d"]}\n')
            # Write shear calculations
            f.write(f'{shearput[i]["explanation_1"]}\n {shearput[i]["Vc"]}\n')
            f.write(f'{shearput[i]["explanation_2"]}\n {shearput[i]["min_stirrup_strength"]}\n')
            f.write(f'{shearput[i]["explanation_3"]}\n {shearput[i]["max_stirrup_capacity"]}\n')
            # Write s calculations
            f.write(f'{sput[i]["explanation_1"]}\n {sput[i]["s"]}\n')