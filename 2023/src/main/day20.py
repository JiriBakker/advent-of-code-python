from main.util import all
from math import lcm

def day20a(input: list[str]) -> int:
    modules = parse_input(input)
    broadcaster = modules["broadcaster"]

    queue: list[tuple[Module, str, str]] = []
    high_pulses_outputted = 0
    low_pulses_outputted = 0

    def count_pulse(pulse: str) -> None:
        if pulse == "high": nonlocal high_pulses_outputted; high_pulses_outputted += 1
        else:               nonlocal low_pulses_outputted; low_pulses_outputted += 1

    for _ in range(0, 1000):
        queue.append((broadcaster, "button", "low"))

        while len(queue) > 0:
            (module, prev_module_name, pulse) = queue.pop(0)

            count_pulse(pulse)

            if isinstance(module, Output):
                pass
            elif isinstance(module, Broadcaster):
                pulse = module.receive(pulse)
                for dest_module in module.dest_modules:
                    queue.append((modules[dest_module], module.name, pulse))
            elif isinstance(module, FlipFlop):
                pulse = module.receive(pulse)
                if pulse is not None:
                    for dest_module in module.dest_modules:
                        queue.append((modules[dest_module], module.name, pulse))
            elif isinstance(module, Conjuction):
                pulse = module.receive(pulse, prev_module_name)
                for dest_module in module.dest_modules:
                    queue.append((modules[dest_module], module.name, pulse))
            
    return high_pulses_outputted * low_pulses_outputted

def day20b(input: list[str]) -> int:
    modules = parse_input(input)
    broadcaster = modules["broadcaster"]

    queue: list[tuple[Module, str, str]] = []
    high_pulses_outputted = 0
    low_pulses_outputted = 0

    def count_pulse(pulse: str) -> None:
        if pulse == "high": nonlocal high_pulses_outputted; high_pulses_outputted += 1
        else:               nonlocal low_pulses_outputted; low_pulses_outputted += 1

    special = set(["qq", "sj", "bg", "ls"])
    cycles: dict[str,tuple[int,int|None]] = {}

    i = 1

    def collect_cycle_info(module_name: str):
        if module_name not in cycles:
            cycles[module_name] = (i, None)
        elif cycles[module_name][1] is None:
            cycles[module_name] = (cycles[module_name][0], i)
            
    while True:
        queue.append((broadcaster, "button", "low"))

        i += 1

        while len(queue) > 0:
            (module, prev_module_name, pulse) = queue.pop(0)

            if prev_module_name in special and pulse == "high":
                collect_cycle_info(prev_module_name)
                if len(cycles) == len(special) and all(lambda cycle: cycle[1] != None, cycles.values()):
                    cycle_lengths = list(map(lambda cycle: cycle[1] - cycle[0] if cycle[1] != None else 1, cycles.values()))
                    return lcm(*cycle_lengths)

            count_pulse(pulse)

            if isinstance(module, Output):
                pass
            elif isinstance(module, Broadcaster):
                pulse = module.receive(pulse)
                for dest_module in module.dest_modules:
                    queue.append((modules[dest_module], module.name, pulse))
            elif isinstance(module, FlipFlop):
                pulse = module.receive(pulse)
                if pulse is not None:
                    for dest_module in module.dest_modules:
                        queue.append((modules[dest_module], module.name, pulse))
            elif isinstance(module, Conjuction):
                pulse = module.receive(pulse, prev_module_name)
                for dest_module in module.dest_modules:
                    queue.append((modules[dest_module], module.name, pulse))

class Module(object):
    def __init__(self, name: str, dest_modules: list[str]):
        self.name = name
        self.dest_modules = dest_modules

class Output(Module):
    def __init__(self, name: str):
        super().__init__(name, [])

    def receive(self, pulse: str) -> str:
        return pulse

class Broadcaster(Module):
    def __init__(self, name: str, dest_modules: list[str]):
        super().__init__(name, dest_modules)

    def receive(self, pulse: str) -> str:
        return pulse

class FlipFlop(Module):
    def __init__(self, name: str, dest_modules: list[str]):
        super().__init__(name, dest_modules)
        self.on = False

    def receive(self, pulse: str) -> str | None:
        if pulse == "high":
            return None
        
        if self.on:
            self.on = False
            return "low"
        else:
            self.on = True
            return "high"


class Conjuction(Module):
    def __init__(self, name: str, dest_modules: list[str]):
        super().__init__(name, dest_modules)
        self.last_pulses: dict[str,str] = {}

    def receive(self, pulse: str, input: str) -> str:
        if input not in self.last_pulses:
            raise Exception(f"Unknown input {input} -- {self}")
        
        self.last_pulses[input] = pulse

        if all(lambda pulse: pulse == "high", self.last_pulses.values()):
            return "low"
        else:
            return "high"
        
    def register_input(self, input: str) -> None:
        self.last_pulses[input] = "low"

    def __str__(self) -> str:
        return f"Conjuction {self.name} {self.last_pulses}"


def parse_input(input: list[str]) -> dict[str, Module]:
    modules: dict[str, Module] = {}
    for line in input:
        (key, dest) = line.split(" -> ")
        name = key.lstrip("&").lstrip("%")
        dest_modules = dest.split(", ")

        if key.startswith("%"):
            name = key[1:]
            modules[name] = FlipFlop(name, dest_modules)
        elif key.startswith("&"):
            name = key[1:]
            modules[name] = Conjuction(name, dest_modules)
        else:
            modules[key] = Broadcaster(key, dest_modules)


    for line in input:
        (key, dest) = line.split(" -> ")
        name = key.lstrip("&").lstrip("%")
        dest_modules = dest.split(", ")

        for dest_module in dest_modules:
            module = modules.get(dest_module, None)
            if isinstance(module, Conjuction):
                module.register_input(name)
            if module is None:
                modules[dest_module] = Output(dest_module)

    return modules