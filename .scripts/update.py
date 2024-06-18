import subprocess
from typing import Dict

def run_command(command: str, cwd: str = None) -> None:
    result = subprocess.run(command, shell=True, text=True, cwd=cwd, capture_output=True)
    if result.returncode != 0:
        print(result.stderr)
    else:
        print(result.stdout)

def get_submodules_branches() -> Dict:
    submodules : Dict = {}
    with open('.gitmodules', 'r') as file:
        lines = file.readlines()
        current_submodule = None
        for line in lines:
            if line.startswith('[submodule "'):
                current_submodule = line.split('"')[1]
                submodules[current_submodule] = {'path': None, 'branch': None}
            elif 'path =' in line and current_submodule:
                submodules[current_submodule]['path'] = line.split('=')[1].strip()
            elif 'branch =' in line and current_submodule:
                submodules[current_submodule]['branch'] = line.split('=')[1].strip()
    return submodules

def update_and_checkout_submodules() -> None:
    run_command("git pull --rebase")
    run_command("git submodule update --init --recursive --remote")
    submodules = get_submodules_branches()
    for name, info in submodules.items():
        submodule_path = info['path']
        submodule_branch = info['branch']
        if submodule_path and submodule_branch:
            print(f"Checking {submodule_path} to {submodule_branch}")
            run_command(f"git checkout {submodule_branch}", cwd=submodule_path)
            run_command(f"git pull --rebase", cwd=submodule_path)

def main() -> None:
    """
    - Initialiser et mettre à jour tous les sous-modules
    - Récupérer les branches spécifiées dans .gitmodules et faire un checkout dessus.
    """
    update_and_checkout_submodules()
    print("OK.")

if __name__ == "__main__":
    main()
