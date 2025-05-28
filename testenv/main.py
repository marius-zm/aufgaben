from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint # Alias rich's print to rprint to avoid conflicts
import time # For the spinner demo

console = Console()
running = True
users_list = []

# Enhanced welcome message using a Panel
console.print(
    Panel(
        "[bold cyan]🔢 Zahlen-Assistent 🔢[/bold cyan]\n\n"
        "Gib mir deine ganzen Zahlen. Ich sammle sie, sortiere sie und "
        "zeige dir nützliche Informationen an.\n\n"
        "[yellow]Schreibe 'stop', um die Eingabe zu beenden und die Analyse zu starten.[/yellow]",
        title="[green]Willkommen![/green]",
        border_style="blue",
        expand=False,
    )
)

while running:
    user_input = console.input("[bold magenta]Gebe eine beliebige ganze Zahl ein:[/bold magenta] ").lower()

    if user_input == "stop":
        if not users_list: # More Pythonic way to check if list is empty
            console.print("[bold red]❌ Deine Liste ist leer. Ich habe nichts für dich zu analysieren.[/bold red]")
            running = False # Corrected from running == False
            break

        console.print("\n[bold green]✅ Zahlen-Eingabe beendet. Verarbeite Daten...[/bold green]")

        # Simulate a small processing time with a spinner
        with console.status("[bold green]Berechne Statistiken...[/bold green]", spinner="dots"):
            time.sleep(1.5) # Simulate work

        # Calculations (your original logic is fine, but using built-ins where possible)
        list_sum = sum(users_list)
        highest_number = max(users_list)
        lowest_number = min(users_list)
        average = list_sum / len(users_list)
        users_list_sorted = sorted(users_list)

        console.print("\n[bold cyan]📊 Hier sind die Ergebnisse deiner Zahlen:[/bold cyan]")

        # Create a table for the main statistics
        table = Table(title="[bold underline]Zahlen-Statistiken[/bold underline]", style="dim")
        table.add_column("Statistik", style="bold", justify="left")
        table.add_column("Wert", style="green", justify="right")

        table.add_row("Anzahl der Zahlen", str(len(users_list)))
        table.add_row("Summe aller Zahlen", str(list_sum))
        table.add_row("Höchste Zahl", str(highest_number))
        table.add_row("Niedrigste Zahl", str(lowest_number))
        table.add_row("Durchschnitt", f"{average:.2f}") # Format to 2 decimal places

        console.print(table)

        # Display the sorted list separately
        console.print(f"\n[bold yellow]Sortierte Liste:[/bold yellow] [italic]{users_list_sorted}[/italic]")

        running = False

    else:
        try:
            num = int(user_input)
            users_list.append(num)
            console.print(f"[green]👍 '{num}' wurde hinzugefügt.[/green]") # Confirmation message
        except ValueError: # Catch specific error for better practice
            console.print("[bold red]🚫 Das war keine ganze Zahl. Bitte gib eine gültige ganze Zahl ein.[/bold red]")

console.print("\n[bold magenta]Programm beendet. Bis zum nächsten Mal![/bold magenta]")