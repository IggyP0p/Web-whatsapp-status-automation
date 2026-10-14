import json
from pathlib import Path

# Encontrando diretório para armazenar o arquivo diario
diretorio = Path.cwd()
arquivo = diretorio / "src" / "diario.json"
# Caso não exista cria um
if not arquivo.exists():
    _ = arquivo.write_text("[]", encoding="utf-8")

def agendar(data: str, horario: str, tarefa: str, url: str):

    # Lê as tarefas existentes
    tarefas = json.loads(arquivo.read_text(encoding="utf-8"))

    for item in tarefas:
        if tarefa == item["tarefa"]:
            raise ValueError("Não podem haver tarefas iguais")

    # Agenda novo status
    nova_tarefa = {
        "data"    : data,
        "horario" : horario,
        "tarefa"  : tarefa,
        "url"     : url,
    }

    tarefas.append(nova_tarefa)
    _ = arquivo.write_text(
        json.dumps(tarefas, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )
