import os


def analyze_dependencies(repo_path):

    dependencies = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                filepath = os.path.join(root, file)

                with open(filepath, "r", encoding="utf-8") as f:

                    lines = f.readlines()

                    for line in lines:

                        if line.startswith("import"):
                            dependencies.append(line.strip())

                        elif line.startswith("from"):
                            dependencies.append(line.strip())

    return dependencies