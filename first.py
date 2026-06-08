import psutil
import socket
import platform
import datetime
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live

console = Console()

SUSPICIOUS_PORTS = {
    21: "FTP",
    23: "Telnet",
    135: "RPC",
    139: "NetBIOS",
    445: "SMB",
    3389: "RDP"
}

def get_system_info():
    return {
        "OS": platform.system() + " " + platform.release(),
        "Hostname": socket.gethostname(),
        "IP": socket.gethostbyname(socket.gethostname()),
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "RAM Usage": f"{psutil.virtual_memory().percent}%"
    }

def create_system_table():
    info = get_system_info()

    table = Table(title="System Information")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    for key, value in info.items():
        table.add_row(key, str(value))

    return table

def create_connections_table():
    table = Table(title="Active Network Connections")
    table.add_column("Local Address")
    table.add_column("Remote Address")
    table.add_column("Status")
    table.add_column("Risk")

    try:
        connections = psutil.net_connections()

        count = 0
        for conn in connections:
            if count >= 15:
                break

            local = (
                f"{conn.laddr.ip}:{conn.laddr.port}"
                if conn.laddr else "N/A"
            )

            remote = (
                f"{conn.raddr.ip}:{conn.raddr.port}"
                if conn.raddr else "N/A"
            )

            risk = "Normal"

            if conn.laddr and conn.laddr.port in SUSPICIOUS_PORTS:
                risk = f"⚠ {SUSPICIOUS_PORTS[conn.laddr.port]}"

            table.add_row(local, remote, conn.status, risk)
            count += 1

    except Exception:
        table.add_row("Permission Denied", "-", "-", "-")

    return table

def create_process_table():
    table = Table(title="Running Processes")
    table.add_column("PID")
    table.add_column("Name")
    table.add_column("CPU %")

    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except:
            pass

    processes = sorted(
        processes,
        key=lambda x: x['cpu_percent'],
        reverse=True
    )[:10]

    for p in processes:
        table.add_row(
            str(p['pid']),
            str(p['name']),
            str(p['cpu_percent'])
        )

    return table

def create_layout():
    layout = Layout()

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body")
    )

    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )

    layout["left"].split_column(
        Layout(name="system"),
        Layout(name="processes")
    )

    layout["right"].update(create_connections_table())

    layout["header"].update(
        Panel(
            f"CYBERSECURITY MONITORING DASHBOARD\n"
            f"{datetime.datetime.now()}",
            style="bold green"
        )
    )

    layout["system"].update(create_system_table())
    layout["processes"].update(create_process_table())

    return layout

def main():
    with Live(create_layout(), refresh_per_second=1) as live:
        while True:
            live.update(create_layout())

if __name__ == "__main__":
    main()
