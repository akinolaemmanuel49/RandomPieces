#!/usr/bin/python
import typer
from rich import print, prompt

from database import confirm_user, create_new_user, get_all_credentials


def get_passwords():
    username = prompt.Prompt.ask('Enter your username')
    password = prompt.Prompt.ask('Enter your password', password=True)

    user_id = confirm_user(username, password)
    get_all_credentials(user_id)


def main_screen():
    print(
        """Options\n[1] View your passwords\n[2] Create a new profile\n[3] Exit""")
    option = prompt.Prompt.ask("Select option")
    if option == '1':
        get_passwords()
    elif option == '2':
        create_new_profile()
    elif option == '3':
        typer.Exit()
    else:
        return main_screen()


def create_new_profile():
    username = prompt.Prompt.ask('Please enter a username')
    if prompt.Confirm.ask(
            f'Are you sure you want your username to be {username}'):
        password = prompt.Prompt.ask(
            'Please enter your password', password=True)
        confirm_password = prompt.Prompt.ask(
            'Please confirm your password', password=True)
        if password == confirm_password:
            create_new_user(username=username, plaintext_password=password)


def main(retry: int = 0):
    if int(retry) <= 3:
        is_new_user = prompt.Prompt.ask('Are you a new user? [y/n]')

        if is_new_user.lower() == 'y':
            create_new_profile()
            main_screen()

        elif is_new_user.lower() == 'n':
            main_screen()
        else:
            print(retry)
            retry = int(retry) + 1

            return main(retry)
    else:
        raise typer.Exit()


if __name__ == '__main__':
    typer.run(main)
