import json
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from apscheduler.schedulers.blocking import BlockingScheduler

# Procura o diario para fazer a leitura dos dados
diretorio = Path.cwd()
diario = diretorio / "src" / "diario.json"
# Setando TimeZone
TZ = ZoneInfo("America/Sao_Paulo")
scheduler = BlockingScheduler(timezone=TZ)

tarefas_pendentes = []

def verificar_diario():
    global tarefas_pendentes

    if not diario.is_file():
        raise FileNotFoundError("Não há diário para fazer a leitura")

    # carregando os dados do diario
    tarefas = json.loads(diario.read_text(encoding="utf-8"))
    # Pegando data atual para comparação
    data_atual = datetime.now(TZ).date().isoformat()

    for item in tarefas:
        if item["data"] == data_atual:
            tarefas_pendentes.append(item)
            print(f'{item["horario"]} - {item["tarefa"]}')

    if not tarefas_pendentes:
        print("Não há tarefas para hoje.")

    while tarefas_pendentes:

        agora = datetime.now(TZ)
        hora_atual = agora.strftime("%H:%M")

        pendentes = [
            item for item in tarefas_pendentes
            if item["horario"] <= hora_atual
        ]

        for item in pendentes:
            try:
                executar_tarefas(item)
            except Exception as erro:
                print(
                    f'Erro ao executar "{item["tarefa"]}": {erro}'
                )
            else:
                tarefas_pendentes.remove(item)

        if not tarefas_pendentes:
            print("Tarefas realizadas com sucesso!")
            break

        time.sleep(60)



def executar_tarefas(nome: str) -> None:
    print(f"Executando tarefa: {nome}")

    if nome == "subir imagem":

        print("imagem subida!")


def agendar():
    for item in tarefas:
        data_hora = datetime.strptime(
            f"{item['data']} {item['horario']}",
            "%d/%m/%Y %H:%M"
        ).replace(tzinfo=TZ)

        if data_hora <= datetime.now(TZ):
            print(f"Data já passou: {item['tarefa']}")
            continue

        _ = scheduler.add_job(
            executar_tarefas,
            trigger="date",
            run_date=data_hora,
            args=[item["tarefa"]]
        )

        print(f"Agendado: {item['tarefa']} para {data_hora}")
