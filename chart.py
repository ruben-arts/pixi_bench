import json
import math
import os
def main():
    # Load hyperfine data
    with open('hyperfine.json') as f:
        data = json.load(f)

    commands = data['results']
    commands_labels = [cmd['command'].split()[0] for cmd in commands]
    means = [cmd['mean'] for cmd in commands]

    # Set y_max to the maximum mean value
    y_max = math.ceil(max(means))

    # Create enhanced x-axis labels that include the bar value
    enhanced_labels = [f"{lbl} ({round(val,3)}[s])" for lbl, val in zip(commands_labels, means)]

    # Format labels and means for Mermaid
    labels_str = '[' + ', '.join(f'"{label}"' for label in enhanced_labels) + ']'
    means_str = '[' + ', '.join(str(round(m, 2)) for m in means) + ']'

    # If the env var ENV_FILE is set, get the string value
    env_file = os.getenv('ENV_FILE', None)
    if env_file:
        env_file = f" (from '{env_file}')"
    else:
        env_file = ""

    # Print the Mermaid snippet
    print("```mermaid")
    print("---")
    print("config:")
    print("    xyChart:")
    print("        width: 900")
    print("        height: 600")
    print("    themeVariables:")
    print("        xyChart:")
    print("            plotColorPalette: \"#FFC300\"")
    print("---\n")
    print("xychart-beta")
    print(f'    title "Comparison of Environment Creation Times{env_file}"')
    print(f"    x-axis {labels_str}")
    print(f'    y-axis "Time[s]" 0 --> {y_max}\n')
    print(f"    bar {means_str}")
    print("```")

if __name__ == '__main__':
    main()
