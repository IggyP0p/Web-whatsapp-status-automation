# Scheduler de Status do Whatsapp WEB

Utiliando o selenium com APScheduler criei uma aplicação que monitora o tempo e sobe uma imagem nos status do whatsapp de forma autonoma no navegador firefox.


## Como usar

Para usar você precisa apenas baixar o repositório, existe um exemplo de agendamento em main.py. Crie agendamentos naquele mesmo estilo e rode a agenda ele ficará esperando o horario marcado e enviará os status.

[!ATENÇÃO!]

Se deve ter uma conta logada no whatsapp web, veja em src/agenteweb.py "SEU_PROFILE_DO_FIREFOX_AQUI".
Dois agendamentos não podem ter o mesmo "nome" (tarefa), ele lança um erro caso isso ocorra.
Não se pode fazer Dois agendamentos no mesmo horario.
Coloque as imagens na pasta "imgs" no diretório principal. Siga o exemplo do main.py


## Dificuldades

- Infelizmente se o usuario ja estiver usando o navegador ele não consegue abrir/fazer uso do navegador


## Possiveis melhorias possiveis

[ ] Uma interface gráfica para criar agendamentos.
[ ] Script de inicialização com a maquina.
[ ] Aceitar diferentes navegadores além do firefox.
[ ] Aceitar imagens de outros diretórios/locais
[ ] Execução em segundo plano.
