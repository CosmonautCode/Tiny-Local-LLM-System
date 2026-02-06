from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time


console = Console()

SYSTEM_PROMPT = (
    "You are a helpful assistant.\n"
    "Always reply in clear and concise English.\n"
    "Do not give advice about how to be helpful — respond directly to the user.\n"
    "Answer logically and on-topic. Stay brief. Never use French.\n"
)


MAX_HISTORY = 6

class ChatSystem:
    def __init__(self, llm):
        self.llm = llm
        self.history = []

    def chat_display(self):
        console.clear()
        console.rule("[bold blue] Tiny Local LLM Chat [/bold blue]", style="bold blue")

        console.print(Panel.fit(
            "[bold green]Local LLM ready![/bold green]\n Type [bold yellow] 'exit' [/bold yellow] to quit",
            title="[bold cyan] Status [/bold cyan]",
            border_style="green"
        ))

        console.print(Panel.fit(
            "[bold magenta]Welcome![/bold magenta]\nYou can start chatting with your Tiny LLM below.",
            border_style="magenta"
        ))

        while True:
            user_input = console.input("[bold cyan]You > [/bold cyan] ")

            if user_input.lower() in {"exit", "quit"}:
                console.print("[bold red]Exiting... Goodbye![/bold red]")
                break

            self.history.append(("user", user_input))

            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            messages += [
                {"role": role, "content": text}
                for role, text in self.history
            ]

            with console.status(
                "[bold magenta]LLM is typing...[/bold magenta]",
                spinner="dots"
            ):
                output = self.llm.create_chat_completion(
                    messages=messages,
                    max_tokens=1028,
                    temperature=0.2,
                    top_p=0.9,
                    repeat_penalty=1.15,
                )

            response = output["choices"][0]["message"]["content"].strip()
            self.history.append(("assistant", response))


            if len(self.history) > MAX_HISTORY:
                del self.history[:-MAX_HISTORY]

            console.print(
                Panel(
                    Text(response, style="bold magenta"),
                    title="[bold green]LLM[/bold green]",
                    border_style="cyan"
                )
            )



