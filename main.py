import re
import json
import os

ARQUIVO = 'tarefas.json'


def listar_tarefas(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa encontrada.')
    else:
        print('Tarefas:')
        for i, tarefa in enumerate(tarefas, 1):
            print(f'{i}. {tarefa}')


def desfazer_tarefa(tarefas, refazer_tarefas):
    if tarefas:
        refazer_tarefas.append(tarefas.pop())
        print('Tarefa desfeita.\n')
    else:
        print('Nenhuma tarefa para desfazer.')


def refazer_tarefa(tarefas, refazer_tarefas):
    if refazer_tarefas:
        tarefas.append(refazer_tarefas.pop())
        print('Tarefa refeita.\n')
    else:
        print('Nenhuma tarefa para refazer.')


def adicionar(tarefa, tarefas):
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada.\n')


def ler_tarefas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print('Erro ao ler o arquivo de tarefas. Criando um novo arquivo.')
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as file:
        json.dump(tarefas, file, indent=4)
    print('Tarefas salvas com sucesso.\n')


def main():
    tarefas = ler_tarefas()
    refazer_tarefas = []

    comandos = {
        'listar': lambda: listar_tarefas(tarefas),
        'desfazer': lambda: desfazer_tarefa(tarefas, refazer_tarefas),
        'refazer': lambda: refazer_tarefa(tarefas, refazer_tarefas),
        'salvar': lambda: salvar_tarefas(tarefas)
    }

    while True:
        print('Comandos: "adicionar", "listar", "desfazer", "refazer", "salvar", "sair"')
        comando = input('Digite uma tarefa ou comando: ').strip().lower()

        if comando == 'sair':
            print('Saindo do programa...')
            break
        elif comando == 'adicionar':
            nova_tarefa = input('Digite a nova tarefa: ')
            if re.match(r'^[\w\s.,!?\'"-]+$', nova_tarefa):
                adicionar(nova_tarefa, tarefas)
            else:
                print('Tarefa inválida. Tente novamente.')
        elif comando in comandos:
            comandos[comando]()
        else:
            print('Comando inválido.')


if __name__ == '__main__':
    main()
