from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt # For better input validation
from rich.table import Table
from rich.text import Text
import pyfiglet # For the big heading
import sys # For sys.exit()

# --- Initialisiere Rich Console ---
console = Console()

# --- Funktionen für die Temperaturumrechnung ---
def celsius_zu_fahrenheit(c: float) -> float:
    """Wandelt Celsius in Fahrenheit um."""
    return c * 9/5 + 32

def fahrenheit_zu_celsius(f: float) -> float:
    """Wandelt Fahrenheit in Celsius um."""
    return (f - 32) * 5/9

# --- Hauptprogramm ---
def main():
    # ASCII Art Heading
    # Experimentiere mit verschiedenen Fonts wie "block", "banner", "standard"
    ascii_banner = pyfiglet.figlet_format("Temp Converter", font="chunky")
    console.print(f"[bold red]{ascii_banner}[/bold red]")
    console.print("[bold blue]Willkommen beim Temperaturen-Umrechner![/bold blue]\n")

    # Anleitung als Panel
    console.print(
        Panel(
            "Wähle eine Umrechnungsrichtung und gib die Temperatur ein.\n"
            "[yellow]Gib 'exit' ein, um das Programm zu beenden.[/yellow]",
            title="[green]Anleitung[/green]",
            border_style="yellow",
            expand=False,
        )
    )

    while True:
        console.print("\n[bold magenta]Was möchtest du umwandeln?[/bold magenta]")
        console.print("[cyan]1.[/cyan] Celsius nach Fahrenheit")
        console.print("[cyan]2.[/cyan] Fahrenheit nach Celsius")
        console.print("[red]exit[/red] Programm beenden")

        # Verwende rich.prompt.Prompt für bessere Eingabeaufforderung und -validierung
        choice = Prompt.ask(
            "[bold green]Deine Auswahl (1, 2 oder exit)[/bold green]",
            choices=["1", "2", "exit"], # Restrict valid inputs
            default="1", # Optional: Set a default choice
            show_choices=False # Don't show choices in the prompt line itself
        ).lower()

        if choice == "exit":
            console.print("\n[bold magenta]👋 Tschüss! Programm beendet.[/bold magenta]")
            sys.exit() # Beendet das Programm sauber

        conversion_type = ""
        if choice == "1":
            conversion_type = "[cyan]Celsius nach Fahrenheit[/cyan]"
        elif choice == "2":
            conversion_type = "[cyan]Fahrenheit nach Celsius[/cyan]"

        console.print(f"\n[bold yellow]Du hast gewählt: {conversion_type}[/bold yellow]")

        # Schleife für die Temperatureingabe mit Fehlerprüfung
        while True:
            temp_input = console.input("[bold magenta]Bitte gib die Temperatur ein:[/bold magenta] ").lower()
            if temp_input == "exit":
                console.print("\n[bold magenta]👋 Tschüss! Programm beendet.[/bold magenta]")
                sys.exit()

            try:
                temperature = float(temp_input)
                break # Gültige Zahl, Schleife beenden
            except ValueError:
                console.print("[bold red]🚫 Ungültige Eingabe! Bitte gib eine Zahl ein (z.B. 25.5 oder -10).[/bold red]")

        result = None
        unit_from = ""
        unit_to = ""

        if choice == "1":
            result = celsius_zu_fahrenheit(temperature)
            unit_from = "°C"
            unit_to = "°F"
        elif choice == "2":
            result = fahrenheit_zu_celsius(temperature)
            unit_from = "°F"
            unit_to = "°C"

        # Zeige das Ergebnis in einer schönen Tabelle
        console.print("\n[bold cyan]✨ Dein Ergebnis:[/bold cyan]")
        # HIER WURDE DIE ZEILE KORRIGIERT: [/underline] kommt vor [/bold]
        result_table = Table(title="[bold][underline]Temperaturumrechnung[/underline][/bold]", style="dim")
        result_table.add_column("Original", style="bold", justify="right")
        result_table.add_column("Umrechnung", style="green", justify="right")

        # Füge einen kleinen Pfeil hinzu, um die Richtung zu zeigen
        result_table.add_row(f"{temperature:.2f}{unit_from}", f"{result:.2f}{unit_to} [green]➡️[/green]")

        console.print(result_table)
        console.print("[bold yellow]------------------------------------[/bold yellow]") # Trennlinie

if __name__ == "__main__":
    main()