from weather_service import get_weather
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

while True:
    console.print("\n[bold blue]--- Consulta de Clima ---[/bold blue]")
    
    
    city = Prompt.ask("[bold white]Digite a cidade[/bold white]").strip()

    if not city:
        console.print("[yellow]Por favor, digite o nome de uma cidade![/yellow]")
        continue

    with console.status("[bold green]Buscando dados...[/bold green]"):
        weather = get_weather(city)

    if weather:
        conteudo = (
            f"[bold cyan] {weather['cidade']}[/bold cyan]\n"
            f"[yellow] Temperatura:[/yellow] {weather['temp']:.1f}°C\n"
            f"[white] Condição:[/white]    {weather['descricao'].capitalize()}\n"
            f"[blue] Umidade:[/blue]      {weather['umidade']}%\n"
            f"---"
            f"\n[red]🔺 Máx:[/red] {weather['max']}°C | [blue]🔻 Mín:[/blue] {weather['min']}°C"
        )
        
        console.print(Panel(conteudo, title="[bold]Previsão do Tempo[/bold]", border_style="green", expand=False))
    else:
        console.print(Panel("[red]❌ Erro:[/red] Não foi possível encontrar essa cidade.", border_style="red"))

    again = Prompt.ask("\nDeseja consultar outra?", choices=["s", "n"], default="s")
    if again != "s":
        console.print("[bold yellow]Encerrando... [/bold yellow]")
        break