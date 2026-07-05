import psutil
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel

class SystemMonitor:
    def __init__(self):
        self.console = Console()

    def get_metrics(self):
        cpu_percent = psutil.cpu_percent(interval=0.5)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net = psutil.net_io_counters()
        net_sent = net.bytes_sent / (1024 * 1024) 
        net_recv = net.bytes_recv / (1024 * 1024)
        
        return {
            'cpu_pct': cpu_percent,
            'ram_pct': ram.percent,
            'disk_pct': disk.percent,
            'ram_used': f"{ram.used / (1024**3):.1f}/{ram.total / (1024**3):.1f} GB",
            'disk_used': f"{disk.used / (1024**3):.1f}/{disk.total / (1024**3):.1f} GB",
            'cpu_cores': psutil.cpu_count(),
            'net_sent': f"{net_sent:.1f} MB",
            'net_recv': f"{net_recv:.1f} MB"
        }

    def create_bar(self, percent, color="green"):
        filled = int(percent / 5)
        empty = 20 - filled
        return f"[{color}]{'█' * filled}{'░' * empty}[/{color}]"

    def generate_dashboard(self):
        m = self.get_metrics()
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Metric", style="cyan bold", width=12)
        table.add_column("Value", justify="right", width=15)
        table.add_column("Load", justify="left")

        table.add_row("CPU", f"{m['cpu_pct']}%", self.create_bar(m['cpu_pct'], "red"))
        table.add_row("RAM", m['ram_used'], self.create_bar(m['ram_pct'], "yellow"))
        table.add_row("Disk", m['disk_used'], self.create_bar(m['disk_pct'], "blue"))
        table.add_row("Cores", str(m['cpu_cores']), "")
        table.add_row("Net (Up)", m['net_sent'], "")
        table.add_row("Net (Down)", m['net_recv'], "")
        return Panel(table, title="[bold magenta]🖥️ Term-Stat v0.1[/bold magenta]", border_style="bright_blue")

    def run(self):
        with Live(self.generate_dashboard(), refresh_per_second=2, screen=True) as live:
            try:
                while True:
                    live.update(self.generate_dashboard())
                    time.sleep(0.5)
            except KeyboardInterrupt:
                print("\n👋 Bye!")
