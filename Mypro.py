import os
from rich.console import Console
from rich.panel import Panel

LANGUAGE_EXTENSIONS = {
    "Python": ".py",
    "Java": ".java",
    "C++": ".cpp",
    "C": ".c",
    "C#": ".cs",
    "JavaScript": ".js",
    "TypeScript": ".ts",
    "HTML": ".html",
    "CSS": ".css",
    "PHP": ".php",
    "Ruby": ".rb",
    "Go": ".go",
    "Swift": ".swift",
    "Kotlin": ".kt",
    "Shell Script": ".sh",
    "R": ".r",
    "Perl": ".pl",
    "Scala": ".scala",
    "Haskell": ".hs",
    "Lua": ".lua",
    "Objective-C": ".m",
    "SQL": ".sql",
    "YAML": ".yml",
    "JSON": ".json",
    "Markdown": ".md",
    "XML": ".xml"
}

def list_files_by_extension(extension):
    console = Console()
    console.log(f"Searching for files with extension: {extension}")
    try:
        for root, dirs, files in os.walk("/", topdown=True):
            # Skip system directories to prevent endless search
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in (
                "proc", "sys", "dev", "run", "tmp", "var", "snap", "usr", "lib", "lib64", "boot", "srv", "opt", "sbin", "bin"
            )]
            console.log(f"Currently scanning directory: {root}")
            for file in files:
                if file.endswith(extension):
                    console.log(f"Found file: {file}")
                    print(os.path.join(root, file))
    except PermissionError as e:
        console.log(f"PermissionError: {e}", style="bold red")

def main():
    console = Console()
    console.print(Panel("Welcome to MyPro Tool", expand=False, style="bold green"))
    console.print("\nSelect a language:\n", style="bold cyan")
    for idx, language in enumerate(LANGUAGE_EXTENSIONS.keys(), start=1):
        console.print(f"{idx}. {language}", style="bold yellow")

    while True:
        choice = input("\nEnter the number: ")
        console.log(f"User entered: {choice}")
        try:
            choice = int(choice)
            if 1 <= choice <= len(LANGUAGE_EXTENSIONS):
                selected_language = list(LANGUAGE_EXTENSIONS.keys())[choice - 1]
                extension = LANGUAGE_EXTENSIONS[selected_language]
                console.print(f"\nListing {selected_language} files...\n", style="bold magenta")
                console.log(f"User selected language: {selected_language}")
                list_files_by_extension(extension)
                break
            else:
                console.print(f"\nInvalid choice, please enter a number between 1 and {len(LANGUAGE_EXTENSIONS)}.", style="bold red")
                console.log("Invalid choice by user, out of range.")
        except ValueError:
            console.print("\nPlease enter a valid number.", style="bold red")
            console.log("ValueError: User did not enter a valid number.")

if __name__ == "__main__":
    main()