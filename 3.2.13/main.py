from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import pyfiglet

console = Console()

def celsius_zu_fahrenheit(c):
    return round(c * 9 / 5 + 32, 2)

def celsius_zu_kelvin(c):
    return round(c + 273.15, 2)


def fahrenheit_zu_celsius(f):
    return round((f - 32) * 5 / 9, 2)


def fahrenheit_zu_kelvin(f):
    return round((f - 32) * 5 / 9 + 273.15, 2)


def kelvin_zu_celsius(k):
    return round(k - 273.15, 2)


def kelvin_zu_fahrenheit(k):
    return round((k - 273.15) * 9 / 5 + 32, 2)


def calc_conversion(type_of_conversion):
    while True:
        try:
            value = float(console.input(f"[bold magenta]Gebe den Wert für [cyan]{type_of_conversion}[/cyan] ein: [/bold magenta]").strip())
            break
        except ValueError:
            print("Upps, das war keine Zahl. Gebe eine Zahl wie 2, -10 oder 4.7 ein.")

    result_table = Table(
        title=f"\n[bold][underline]Umrechnungen für {value} {type_of_conversion}[/underline][/bold]",
        style="dim",
        show_header=True,
    )
    result_table.add_column(f"{type_of_conversion}", style="bold green", justify="left")
    result_table.add_column(f"Umrechnung", style="cyan", justify="right")
            
    match type_of_conversion:
        case "Celsius":
            in_fahrenheit = celsius_zu_fahrenheit(value)
            in_kelvin = celsius_zu_kelvin(value)
            result_table.add_row(f"{value}°C", f"{in_fahrenheit}°F")
            result_table.add_row(f"{value}°C", f"{in_kelvin}K")
            
        case "Fahrenheit":
            in_celsius = fahrenheit_zu_celsius(value)
            in_kelvin = fahrenheit_zu_kelvin(value)
            result_table.add_row(f"{value}°F", f"{in_celsius}°C")
            result_table.add_row(f"{value}°F", f"{in_kelvin}K")
            
        case "Kelvin":
            in_celsius = kelvin_zu_celsius(value)
            in_fahrenheit = kelvin_zu_fahrenheit(value)
            print("\n --- Ergebnisse --- ")
            result_table.add_row(f"{value}K", f"{in_celsius}°C")
            result_table.add_row(f"{value}K", f"{in_fahrenheit}°F")
            
    console.print(result_table)
    console.print("[bold green]------------------------------------[/bold green]")

def menu():
    ascii_banner = pyfiglet.figlet_format("Temp Converter", font="chunky") # Oder "block", "slant"
    console.print(f"[bold purple]{ascii_banner}[/bold purple]")

    console.print(
        Panel(
            "\n[bold blue]Willkommen beim Temperaturumrechner![/bold blue]\n\n"
            "[cyan]Wähle 1 für Celsius in Fahrenheit und Kelvin.[/cyan]\n"
            "[cyan]Wähle 2 für Fahrenheit in Celsius und Kelvin.[/cyan]\n"
            "[cyan]Wähle 3 für Kelvin in Celsius und Fahrenheit.[/cyan]\n",
            title="[bold green]Optionen[/bold green]",
            border_style="blue",
            expand=False,
        )
    )

menu()

while True:
    choice = console.input("[bold green]('exit' = beenden, 'menu' = menü anzeigen): [/bold green]").lower().strip()

    if choice == "exit":
        break

    if choice == "menu":
        menu()
        continue

    try:
        choice = int(choice)
    except ValueError:
        print("Upps, das war keine Zahl. Gebe eine 1, 2 oder 3 ein.")

    match choice:
        case 1:
            type = "Celsius"
            calc_conversion(type)
        case 2:
            type = "Fahrenheit"
            calc_conversion(type)

        case 3:
            type = "Kelvin"
            calc_conversion(type)

