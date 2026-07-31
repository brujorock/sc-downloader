# Class import
from Src.Util.console import console, msg


def parse_selection(text, max_value):
    """Parse an index-selection string into a sorted list of unique 1-based indices.

    Accepted formats:
      "*"       -> every index from 1 to max_value
      "N"       -> a single index
      "[N-M]"   -> an inclusive range
      "[N,M,K]" -> an explicit list of indices

    Raises ValueError with a user-facing (Italian) message on any invalid input.
    """

    text = text.strip()

    if not text:
        raise ValueError("Input vuoto.")

    if text == "*":
        return list(range(1, max_value + 1))

    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        if not inner:
            raise ValueError("Formato non valido: parentesi vuote.")

        if "," in inner:
            try:
                indices = [int(p.strip()) for p in inner.split(",")]
            except ValueError:
                raise ValueError(f"Formato lista non valido: '{text}'. Usa [N,M,K] con numeri interi, es. [1,3,5].")
        else:
            parts = inner.split("-")
            if len(parts) != 2:
                raise ValueError(f"Formato intervallo non valido: '{text}'. Usa [N-M], es. [1-2].")
            try:
                start, end = int(parts[0].strip()), int(parts[1].strip())
            except ValueError:
                raise ValueError(f"Formato intervallo non valido: '{text}'. Usa [N-M] con numeri interi, es. [1-2].")
            if start > end:
                start, end = end, start
            indices = list(range(start, end + 1))

        out_of_range = sorted(i for i in indices if not (1 <= i <= max_value))
        if out_of_range:
            shown = out_of_range[:10]
            suffix = f", ... (+{len(out_of_range) - 10} altri)" if len(out_of_range) > 10 else ""
            raise ValueError(f"Indici fuori range (1-{max_value}): {shown}{suffix}")

        return sorted(set(indices))

    try:
        value = int(text)
    except ValueError:
        raise ValueError(f"'{text}' non e' un formato valido. Usa un numero, '*' oppure [N-M] (es. [1-2]).")

    if not (1 <= value <= max_value):
        raise ValueError(f"Indice fuori range: deve essere tra 1 e {max_value}.")

    return [value]


def ask_selection(prompt_text, max_value):
    """Prompt the user for an index selection, re-asking until the input is valid."""

    while True:
        raw = str(msg.ask(prompt_text))
        try:
            return parse_selection(raw, max_value)
        except ValueError as e:
            console.print(f"[error]{e} Riprova.[/]")
