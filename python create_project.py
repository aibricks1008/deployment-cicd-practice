from pathlib import Path

PROJECT = Path(r"C:\Users\0229899\Desktop\rk2\deployment_cicd")

directories = [
    "data",
    "src",
    "tests",
    "models",
    "configs",
]

files = {
    "src/__init__.py": "",
    "tests/__init__.py": "",
    "data/.gitkeep": "",
    "models/.gitkeep": "",
    "configs/config.yaml": "# Project configuration\n",
    "requirements.txt": "",
    "README.md": "# ML Deployment CI/CD Project\n",
    ".gitignore": "",
}

# Create directories
for directory in directories:
    (PROJECT / directory).mkdir(parents=True, exist_ok=True)

# Create files
for file, content in files.items():
    path = PROJECT / file
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

print(f"Project created at:\n{PROJECT}")
print("\nDirectory structure:")

for path in sorted(PROJECT.rglob("*")):
    relative = path.relative_to(PROJECT)
    prefix = "📁" if path.is_dir() else "📄"
    print(f"{prefix} {relative}")