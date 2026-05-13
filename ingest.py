import os
import json

EXCLUDED_FOLDERS = {
    ".git",
    "__pycache__",
    "venv",
    ".idea",
    ".vscode",
    "node_modules"
}

VALID_EXTENSIONS = {
    ".py",
    ".md",
    ".txt"
}

documents = []

for root, dirs, files in os.walk("data/repos"):

    dirs[:] = [
        d for d in dirs
        if d not in EXCLUDED_FOLDERS
    ]

    for file in files:

        extension = os.path.splitext(file)[1]

        if extension not in VALID_EXTENSIONS:
            continue

        path = os.path.join(root, file)

        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read()

                if len(content.strip()) < 50:
                    continue

                documents.append({
                    "path": path,
                    "content": content[:3000]
                })

        except:
            pass

with open(
    "data/documents.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        documents,
        f,
        indent=2
    )

print(f"Ingested {len(documents)} documents")