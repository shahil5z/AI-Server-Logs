import os
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

# Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
console = Console()

def read_logs(file_path):
    """Read logs from a text file."""
    with open(file_path, "r") as f:
        return f.read()

def logs_to_story(log_text):
    """Send logs to OpenAI and get back a human-readable story."""
    prompt = f"""
    You are a system log storyteller.
    Convert the following server/CLI logs into a detective-style report.
    Keep it chronological, clear, and professional.
    
    Logs:
    {log_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    log_file = "sample_logs.txt"

    if not os.path.exists(log_file):
        console.print(f"[red]No log file found: {log_file}[/red]")
    else:
        console.print("[cyan]Reading logs...[/cyan]")
        logs = read_logs(log_file)

        console.print("[cyan]Converting logs into a story...[/cyan]")
        story = logs_to_story(logs)

        console.print("\n[green]--- Story Generated ---[/green]\n")
        console.print(story)
