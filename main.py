import re


def listar_tarefas(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa encontrada.')
        return

    print('Tarefas:')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa}')


def desfazer_tarefa(tarefas, refazer_tarefa):
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return

    tarefa = tarefas.pop()
    refazer_tarefa.append(tarefa)
    print(f'Tarefa "{tarefa}" desfeita.')
    print()


def refazer_tarefa(tarefas, refazer_tarefa):
    if not refazer_tarefa:
        print('Nenhuma tarefa para refazer.')
        return

    tarefa = refazer_tarefa.pop()
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada.')
    print()


tarefas = []
refazer_tarefas = []


while True:
    print('Comandos: "Adicionat", "Listar", "Desfazer", "Refazer", "Sair"')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'sair':
        print('Saindo do programa...')
        break

    if tarefa == 'listar':
        listar_tarefas(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer_tarefa(tarefas, refazer_tarefas)
        continue
    elif tarefa == 'refazer':
        refazer_tarefa(tarefas, refazer_tarefas)
        continue
    elif tarefa == 'adicionar':
        nova_tarefa = input('Digite a nova tarefa: ')
        if re.match(r'^[\w\s.,!?\'"-]+$', nova_tarefa):
            adicionar(nova_tarefa, tarefas)
        else:
            print('Tarefa inválida. Tente novamente.')
            continue
