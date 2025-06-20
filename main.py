#!/usr/bin/env python3

from rich.console import Console
import ansible_runner
import typer
import time
import sys
import os

app = typer.Typer()
console = Console()

# Create a global spinner instance
spinner = None

def process_ansible_event(event):
    global spinner

    if 'event' in event:

        if event['event'] == 'runner_on_start':
            # Start the spinner
            spinner = console.status(f"[bold yellow]{event['event_data']['task']}[/bold yellow]", spinner="dots")
            spinner.start()  # Start the spinner
            #print(f"Task started: {event['event_data']['task']}")

        elif event['event'] == 'runner_on_ok':
            if spinner:
                spinner.stop()  # Stop the spinner
            console.print(f"[bold green]✔️{event['event_data']['task']}[/bold green]")
            #print(f"Task succeeded: {event['event_data']['task']}")

        elif event['event'] == 'runner_on_failed':
            if spinner:
                spinner.stop()  # Stop the spinner
            console.print(f"[bold red]✖️{event['event_data']['task']}[/bold red]")
            #print(f"Task failed: {event['event_data']['task']}")

        elif event['event'] == 'runner_on_skipped':
            if spinner:
                spinner.stop()  # Stop the spinner
            console.print(f"[bold yellow]? {event['event_data']['task']}[/bold yellow]")
            #print(f"Task skipped: {event['event_data']['task']}")

@app.command()
def update():
    print(f"This will proces code changes")

@app.command()
def deploy(dry_run: bool = False):

    # Suppress standard output and error
    r = ansible_runner.run(
        private_data_dir='ansible',
        playbook='deploy.yaml',
        event_handler=process_ansible_event,
        quiet=True  # Suppress standard output
    )

    #r = ansible_runner.run(private_data_dir='config', playbook='playbook.yaml', event_handler=process_event)
    print(f"Playbook finished with status: {r.status}, return code: {r.rc}")
    print("{}: {}".format(r.status, r.rc))

    print("Final status:")
    print(r.stats)


if __name__ == "__main__":
    # Show help message if no command is provided
    if len(sys.argv) == 1:
        sys.argv.append("--help")
    app()