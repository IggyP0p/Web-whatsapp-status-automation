import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from apscheduler.schedulers.blocking import BlockingScheduler

from .agenteweb import postar_status

# Procura o diario para fazer a leitura dos dados
diretorio = Path.cwd()
diario = diretorio / "src" / "diario.json"
# Setando TimeZone
TZ = ZoneInfo("America/Sao_Paulo")
scheduler = BlockingScheduler(timezone=TZ)


def iniciar() -> None:
    verificar_diario()
    scheduler.start()


def verificar_diario():

    if not diario.is_file():
        raise FileNotFoundError("Não há diário para fazer a leitura")

    # carregando os dados do diario
    tarefas = json.loads(diario.read_text(encoding="utf-8"))
    # Pegando data atual para comparação
    data_atual = datetime.now(TZ).date().isoformat()
    tarefas_agendadas = 0

    for item in tarefas:
        if item["data"] != data_atual:
            continue

        horario_execucao = datetime.strptime(
            f'{item["data"]} {item["horario"]}',
            "%Y-%m-%d %H:%M"
        ).replace(tzinfo=TZ)

        if horario_execucao <= datetime.now(TZ):
            print(
                f'Tarefa ignorada (horário passado): {item["tarefa"]}'
            )
            continue

        try:
            _ = scheduler.add_job(
                postar_status,
                trigger="date",
                run_date=horario_execucao,
                args=[item["url"]]
            )

            tarefas_agendadas += 1
            print(
                f'Tarefa agendada: {item["tarefa"]}'
            )

        except Exception as erro:
            print(
                f'Erro ao agendar {item["tarefa"]}: {erro}'
            )

    if tarefas_agendadas == 0:
        print("Nenhuma tarefa agendada para hoje.")
