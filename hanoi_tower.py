from typing import Dict, List
from colorama import Fore


def hanoi(
    n: int, source: str, target: str, auxiliary: str, towers: Dict[str, List[int]]
):
    """
    Recursively moves disks from the source tower to the target tower,
    using the auxiliary tower according to the Tower of Hanoi rules.

    Args:
        n (int): Number of disks to move.
        source (str): The name of the source tower.
        target (str): The name of the destination tower.
        auxiliary (str): The name of the auxiliary tower.
        towers (Dict[str, List[int]]): Dictionary representing all towers.
    """
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(
            f"{Fore.RED}1 {Fore.BLUE}Move disk {disk} from {Fore.GREEN}{source} {Fore.BLUE}to {Fore.GREEN}{target}"
        )
        print(f"Intermediate state: {towers}\n")
        return

    # step 1
    hanoi(n - 1, source=source, target=auxiliary, auxiliary=target, towers=towers)

    # step 2
    disk = towers[source].pop()
    towers[target].append(disk)

    print(
        f"{Fore.RED}2 {Fore.BLUE}Moving disk {disk} from {Fore.GREEN}{source} {Fore.BLUE}to {Fore.GREEN}{target}"
    )
    print(f"Intermediate state: {towers}\n")

    # step 3
    hanoi(n - 1, source=auxiliary, target=target, auxiliary=source, towers=towers)


def solve_hanoi(disks_quantity: int):
    initial_tower = list(range(disks_quantity, 0, -1))
    towers = {
        "A": initial_tower,
        "B": [],
        "C": [],
    }

    print(f"{Fore.YELLOW}initial state: {towers}")
    hanoi(disks_quantity, "A", "C", "B", towers)
    print(f"{Fore.YELLOW}Final state: {towers}{Fore.RESET}")


solve_hanoi(3)
