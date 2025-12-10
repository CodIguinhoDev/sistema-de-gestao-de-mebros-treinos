"""
classe membro: representa os mebros da academia
Treino: representa os treinos dos membros
Academia: gerencia os membros e seus treinos
Adiciona, lista e salva as informações em um arquivo txt
"""

import datetime
from time import sleep
import os


def clear():
    os.system("cls")


class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.workouts = []

    def add_training(self, training):
        self.workouts.append(training)

    def user_information(self):
        information = f"Nome: {self.name}, {self.age} anos\nTreinos:\n"
        for training in self.workouts:
            information += f"Descrição do treino: {training.description}\nDuração do treino: {training.duration} horas\nData do treino: {training.date}\n"
        return information


class Training:
    def __init__(self, description, duration, date):
        self.description = description
        self.duration = duration
        self.date = date

    def training_information(self):
        return f"Descrição: {self.description}\nDuração: {self.duration}\nData: {self.date}"


class Academy:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def list_member(self):
        if not self.members:
            print("Nenhum membro cadastrado.")
        for member in self.members:
            print(member.user_information())

    def save_information(self, file_name):
        with open(file_name, "w") as file:
            for member in self.members:
                file.write(f"{member.name}, {member.age}\n")
                for training in member.workouts:
                    file.write(
                        f"{training.description}, {training.duration}, {training.date}\n"
                    )
        print(
            f"\033[1;32mMembros e treinos salvos no arquivo {file_name} com sucesso!\033[0m"
        )


def main():
    academy = Academy()

    while True:
        clear()

        print("ACADEMIA IGORILA")
        print()
        print("1) Adicionar membro")
        print("2) Adicionar treino ao membro")
        print("3) Listar membros e treinos")
        print("4) Salvar membros e treinos")
        print("5) Sair")
        print()

        option = input("Escolha uma opção: ").strip()

        try:
            number_option = int(option)
            if number_option < 1 or number_option > 5:
                print("\033[31mEssas opções são inválidas...\033[0m")
                input("Pressione ENTER para continuar...")
                continue
        except ValueError:
            print("\033[31mPor favor, digite um número válido.\033[0m")
            input("Pressione ENTER para continuar...")
            continue

        if option == "1":
            clear()
            name = input("Digite o nome do membro: ").capitalize()
            age = input("Digite a idade do membro: ")
            member = Member(name, age)
            academy.add_member(member)
            print("\033[1;32mMembro adicionado com sucesso!\033[0m")
            input("Pressione ENTER para continuar...")

        elif option == "2":
            clear()
            name = input("Digite o nome do membro: ").strip().capitalize()

            member_found = None
            for member in academy.members:
                if member.name == name:
                    member_found = member
                    break

            if member_found is None:
                print("\033[33mMembro não encontrado\033[0m")
                input("Pressione ENTER para continuar...")
                continue

            description_training = input("Descrição do treino: ").strip().capitalize()
            duration_training = input("Duração do treino: ").strip()

            date_training = datetime.datetime.today().strftime("%d/%m/%Y")
            print(f"Data do treino registrada automaticamente: {date_training}")

            training = Training(description_training, duration_training, date_training)
            member_found.add_training(training)

            print("\033[1;32mTreino adicionado com sucesso!\033[0m")
            input("Pressione ENTER para continuar...")

        elif option == "3":
            clear()
            print("Lista de membros e treinos:\n")
            academy.list_member()
            print()
            input("Pressione ENTER para continuar...")

        elif option == "4":
            clear()
            file_name = input("Nome do arquivo para salvar: ").strip()
            academy.save_information(file_name)
            print()
            input("Pressione ENTER para continuar...")

        elif option == "5":
            print("Saindo...")
            sleep(2)
            break


if __name__ == "__main__":
    main()
