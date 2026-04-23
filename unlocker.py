import os
import sys
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import json

APP_NAME = "CoFUnlocker"

def get_config_path():
    appdata = os.getenv("APPDATA")
    config_dir = os.path.join(appdata, APP_NAME)
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "config.json")

console = Console()

UNLOCK_DATA = {
    1: {  # 0x1
        "strings": ("v9agjak+p)(,03qb)aq4", "v9agjak+p)(,o3qb)aq4"),
        "line": 15,
        "desc": "Ending 5 Achievement"
    },
    2: {  # 0x2
        "strings": ("ye&0le1^0(fcanb3v5t4", "ye&ole1^0(fcanb3v5t4"),
        "line": 7,
        "desc": "Ending 4 Achievement"
    },
    3: {  # 0x4
        "strings": ("1r6fd46ob7u2yj9r83yx", "1r6fd46ob7u2yj9q83yx"),
        "line": 45,
        "desc": "Ending 3 Achievement"
    },
    4: {  # 0x8
        "strings": ("2quvo6z3y4w£ld)y!i35", "2quwo6z3y4w£ld)y!i35"),
        "line": 22,
        "desc": "Ending 2 Achievement"
    },
    5: {  # 0x10
        "strings": ("z3,4rj)4b!9g7vgi4x5a", "z3,4lj)4b!9g7vgi4x5a"),
        "line": 3,
        "desc": "The secret room and an empty hint book"
    },
    6: {  # 0x20
        "strings": ("&fx!hd$bw!ayk%dfmcbg", "&fx!hd$bw^ayk%dfmcbg"),
        "line": 83,
        "desc": "Nightmare Difficulty Mode"
    },
    7: {  # 0x40
        "strings": ("r1&,iji4cjtvf.44w919", "r1&,iji4cjtvf,44w919"),
        "line": 39,
        "desc": "FAMAS (Infinite Ammo)"
    },
    8: {  # 0x80
        "strings": ("olt0£s^£rn(aki!9eqkj", "olt0£s^£rn(aki!9eqkh"),
        "line": 51,
        "desc": "David Leatherhoff Hoodie"
    },
    9: {  # 0x100
        "strings": ("h*wchks£n&%!£bf%jtei", "h*wchks£n&%!£bf%jtew"),
        "line": 52,
        "desc": "Mod DB Hoodie"
    },
    10: {  # 0x200
        "strings": ("£xn%i)jhxmfnbgjsr^if", "%xn%i)jhxmfnbgjsr^if"),
        "line": 53,
        "desc": "Hello Kitty Hoodie"
    },
    11: {  # 0x400
        "strings": ("fy^xix&&vkz)vcrn!wtv", "fy^xix&&vkz)vcdn!wtv"),
        "line": 54,
        "desc": "Afraid of Monsters Hoodie"
    },
    12: {  # 0x800
        "strings": ("jwtyv**yb&(qtqlg)moj", "jwsyv**yb&(qtqlg)moj"),
        "line": 55,
        "desc": "Camo Hoodie"
    },
    13: {  # 0x1000
        "strings": ("henp(cm$at!m%£f(c$jp", "henp(cm$at!n%£f(c$jp"),
        "line": 56,
        "desc": "Half-Life Creations Hoodie"
    },
    14: {  # 0x2000
        "strings": ("yef!&kyzw*^vd*tj)zkc", "yef!xkyzw*^vd*tj)zkc"),
        "line": 57,
        "desc": "Black Metal Hoodie"
    },
    15: {  # 0x4000
        "strings": ("z(*mbwy(tolqlrqf$lmw", "z(*mbwy(talqlrqf$lmw"),
        "line": 58,
        "desc": "Team Psykskallar Hoodie"
    },
    16: {  # 0x8000
        "strings": ("zwpwg£vyqlzensuauwat", "zgpwg£vyqlzensuauwat"),
        "line": 59,
        "desc": "Awesome Hoodie"
    },
    17: {  # 0x10000
        "strings": ("dzpy)*iiy$0j!akyfbn%", "dzpy)*iiy$oj!akyfbn%"),
        "line": 60,
        "desc": "Sick Simon Hoodie"
    },
    18: {  # 0x20000
        "strings": ("pe%!``rxr(%(bog)l^j", "pe%!``rxa(%(bog)l^j"),
        "line": 61,
        "desc": "AoM Twitcher Hoodie"
    },
    19: {  # 0x40000
        "strings": ("efq%)u)mk£*odxsdocb)", "efq%)x)mk£*odxsdocb)"),
        "line": 62,
        "desc": "Custom Hoodie"
    },
    20: {  # 0x80000
        "strings": ("pzakhx&p^lbk^kw($(fo", "pzakmx&p^lbk^kw($(fo"),
        "line": 70,
        "desc": "David Leatherhoff's Axe (AoM:DC)"
    },
    21: {  # 0x100000
        "strings": ("g*q$cceqhz&vcdp(av%!", "g*q$cceqhz&vcdp(au%!"),
        "line": 71,
        "desc": "Digital Camera (Weapon)"
    },
    22: {  # 0x200000
        "strings": ("aba^$i)whenzprdh!vus", "aaa^$i)whenzprdh!vus"),
        "line": 72,
        "desc": "Simon's Book (Weapon)"
    },
    23: {  # 0x400000
        "strings": ("mwu£g$&stmkfwej(bg^a", "mwu£g$&ztmkfwej(bg^a"),
        "line": 73,
        "desc": "Developer Commentary"
    },
    24: {  # 0x800000
        "strings": ("tzi&a0xfbkb^n&ikaxj%", "tzi&aoxfbkb^n&ikaxj%"),
        "line": 74,
        "desc": "Hidden Package"
    },
    25: {  # 0x1000000
        "strings": ("wph!uhmgrws)*erdb*rg", "wph!uhhgrws)*erdb*rg"),
        "line": 75,
        "desc": "Gasmask (Nightvision)"
    },
    26: {  # 0x2000000
        "strings": ("&x&v%dvcr&$yoqs%c%ar", "&x&w%dvcr&$yoqs%c%ar"),
        "line": 76,
        "desc": "First Hint Page (Pages)"
    },
    27: {  # 0x4000000
        "strings": ("foyvvuxq^i)brfentm$&", "feyvvuxq^i)brfentm$&"),
        "line": 77,
        "desc": "Second Hint Page (Ranks)"
    },
    28: {  # 0x8000000
        "strings": ("*j%gb*^noyresqjihoes", "*j%gb*^noyresqjihoez"),
        "line": 78,
        "desc": "Third Hint Page (Outfits)"
    },
    29: {  # 0x10000000
        "strings": ("nz(xdxj*w)£!&uh£qn*j", "nz(xdxj*w(£!&uh£qn*j"),
        "line": 79,
        "desc": "Fourth Hint Page (Items)"
    },
    30: {  # 0x20000000
        "strings": ("rvdw&bhwjqsjm$pfwnp)", "lvdw&bhwjqsjm$pfwnp)"),
        "line": 80,
        "desc": "Fifth Hint Page (Weapons)"
    },
    31: {  # 0x80000000
        "strings": (")cfhc$vle$^hn£podlvd", ")cfhc$vle$^hn£padlvd"),
        "line": 82,
        "desc": "Doctor Mode"
    },
    32: {
        "strings": ("ck78kewvx9!%n218dkss", "kk78kewvx9!%n218dkss"),
        "line": 48,
        "desc": "Ending 1 Achievement"
    },
}

def apply_unlock_patch(script_path, unlock_id, should_unlock=True):
    if unlock_id not in UNLOCK_DATA:
        console.print(f"[bold red][!] Error: Unlock ID '{unlock_id}' not found![/bold red]")
        return False
    target_line_number = UNLOCK_DATA[unlock_id]["line"]
    unlocked_str, locked_str = UNLOCK_DATA[unlock_id]["strings"]
    replacement_str = unlocked_str if should_unlock else locked_str
    original_file = script_path
    temp_file = original_file + ".tmp"
    try:
        with open(original_file, 'r', encoding='latin-1') as f_in:
            file_lines = f_in.read().splitlines()
        while len(file_lines) < target_line_number:
            file_lines.append("")
        file_lines[target_line_number - 1] = replacement_str
        output_content = "\n".join(file_lines)
        with open(temp_file, 'w', encoding='latin-1') as f_out:
            f_out.write(output_content)
    except FileNotFoundError:
        console.print(f"[bold red][!] File '{script_path}' not found![/bold red]")
        return False
    except PermissionError:
        console.print(f"[bold red][!] Permission denied! Ensure the game is not running.[/bold red]")
        return False
    except Exception as e:
        console.print(f"[bold red][!] Error: {e}[/bold red]")
        return False
    try:
        os.replace(temp_file, original_file)
    except Exception as e:
        console.print(f"[bold red][!] Failed to replace file: {e}[/bold red]")
        return False
    return True

def display_current_unlock_status(script_path):
    try:
        with open(script_path, 'r', encoding='latin-1') as f:
            lines = f.read().splitlines()
        table = Table(title="Unlock Status", title_style="bold magenta")
        table.add_column("ID", style="cyan", width=4)
        table.add_column("Description", style="white")
        table.add_column("Status", style="green")
        for unlock_id in sorted(UNLOCK_DATA.keys()):
            data = UNLOCK_DATA[unlock_id]
            line_num = data['line']
            if line_num <= len(lines):
                current_line = lines[line_num - 1]
                unlocked_str, locked_str = data['strings']
                is_unlocked = (current_line == unlocked_str)
                status = "[green]Unlocked[/green]" if is_unlocked else "[red]Locked[/red]"
                table.add_row(str(unlock_id), data['desc'][:50], status)
        console.print(table)
        return True
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
        return False

def show_available_unlocks():
    unlock_text = Text()
    for unlock_id in sorted(UNLOCK_DATA.keys()):
        data = UNLOCK_DATA[unlock_id]
        unlock_text.append(f"{unlock_id}. ", style="bold cyan")
        unlock_text.append(f"{data['desc']}\n", style="white")
    console.print(Panel(unlock_text, title="[bold white]Available Unlocks[/bold white]", border_style="blue"))

def show_menu_options():
    console.print("\n[dim]Additional Commands:[/dim]")
    console.print("  [cyan]all[/cyan] - Unlock all items")
    console.print("  [cyan]status[/cyan] - Refresh status")
    console.print("  [cyan]q[/cyan] - Quit\n")

def main():
    console.rule("[bold magenta]Cry of Fear Unlocker[/bold magenta]", style="bold magenta")

    config = load_config()
    saved_path = config.get("script_path", "")

    default_base_path = ""
    if getattr(sys, 'frozen', False):
        default_base_path = os.path.dirname(sys.executable)
    else:
        steam_path = os.path.join(
            os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)'),
            "Steam", "steamapps", "common", "Cry of Fear", "cryoffear"
        )
        if os.path.exists(steam_path):
            default_base_path = steam_path

    default_full_path = os.path.join(default_base_path, "scriptsettings.dat") if default_base_path else ""

    if saved_path and os.path.exists(saved_path):
        console.print(f"[cyan]Using saved path:[/cyan] {saved_path}")
        use_saved = Prompt.ask("Use this path?", choices=["yes", "no"], default="yes")

        if use_saved == "yes":
            settings_path = saved_path
        else:
            settings_path_input = Prompt.ask(
                "[green]Path to scriptsettings.dat[/green]",
                default=default_full_path if default_full_path else None
            )
            settings_path = settings_path_input
    else:
        settings_path_input = Prompt.ask(
            "[green]Path to scriptsettings.dat[/green]",
            default=default_full_path if default_full_path else None
        )
        settings_path = settings_path_input

    if os.path.isdir(settings_path):
        settings_path = os.path.join(settings_path, "scriptsettings.dat")

    if not os.path.exists(settings_path):
        console.print(f"\n[bold red][!] File not found: {settings_path}[/bold red]")
        return

    config["script_path"] = settings_path
    save_config(config)

    console.print(f"[green][✓] File found[/green]\n")

    while True:
        console.rule("[bold cyan]Menu[/bold cyan]", style="bold cyan")
        show_available_unlocks()
        display_current_unlock_status(settings_path)
        show_menu_options()

        choice = Prompt.ask("[bold yellow]Enter unlock ID or command[/bold yellow]").lower()

        if choice == 'q':
            console.print("[bold blue]Goodbye![/bold blue]")
            break

        elif choice == 'status':
            continue

        elif choice == 'all':
            console.print("[bold yellow]WARNING! Unlock ALL items?[/bold yellow]")
            confirm = Prompt.ask("Are you sure? (yes/no)", choices=["yes", "no"]).lower()

            if confirm == "yes":
                success_count = 0
                for unlock_id in UNLOCK_DATA.keys():
                    if apply_unlock_patch(settings_path, unlock_id, should_unlock=True):
                        success_count += 1
                console.print(f"[green][✓] Unlocked {success_count} out of {len(UNLOCK_DATA)} items[/green]")
            else:
                console.print("[yellow]Canceled[/yellow]")

        else:
            try:
                unlock_id = int(choice)
                if unlock_id not in UNLOCK_DATA:
                    console.print("[bold red][!] Invalid ID![/bold red]")
                    continue

                action = Prompt.ask("[bold yellow]1 - Unlock, 2 - Lock[/bold yellow]", choices=["1", "2"])
                should_unlock = (action == '1')

                action_text = "[green]Unlocking[/green]" if should_unlock else "[red]Locking[/red]"
                console.print(f"[*] {action_text}: {UNLOCK_DATA[unlock_id]['desc']}...")

                if apply_unlock_patch(settings_path, unlock_id, should_unlock):
                    console.print(f"[bold green][✓] Done![/bold green]")
                else:
                    console.print(f"[bold red][!] Error![/bold red]")

            except ValueError:
                console.print("[bold red][!] Invalid command![/bold red]")

        print()

def load_config():
    path = get_config_path()
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(config):
    path = get_config_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    main()
