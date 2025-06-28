import subprocess

def get_installed_packages():
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    return set(result.stdout.strip().split('\n'))

def read_requirements_file(file_path="requirements.txt"):
    try:
        with open(file_path, "r") as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        return set()

def write_requirements_file(packages, file_path="requirements.txt"):
    with open(file_path, "w") as file:
        for package in sorted(packages):
            file.write(package + "\n")

def update_requirements():
    print("🔍 Checking installed packages...")
    installed = get_installed_packages()

    print("📄 Reading current requirements.txt...")
    existing = read_requirements_file()

    combined = installed.union(existing)

    print(f"📦 Total packages after update: {len(combined)}")
    write_requirements_file(combined)

    print("✅ requirements.txt updated successfully!")

if __name__ == "__main__":
    update_requirements()
