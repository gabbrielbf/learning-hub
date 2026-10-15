'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

class Connect:

    def __init__(self):
        self.__connect_api()

    def __connect_api(self):
        print('Connecting on API')


class TaskHandler:

    def task_handle(self, task: str) -> None:
        if not isinstance(task, str):
            error_handler = ErrorHandler()
            error_handler.__handle_report()
        else:
            self.__create_task('Play footbal')
            self.__update_task('Play footbal')
            self.__remove_task('Play footbal')

    def __create_task(self, task: str) -> None:
        print(f'Creating TASK: {task}')

    def __update_task(self, task: str) -> None:
        print(f'Updating TASK: {task}')

    def __remove_task(self, task: str) -> None:
        print(f'Removing TASK: {task}')


class Notification:

    def handle_notification(self) ->  None:
        self.__send_notification('Sending notification')

    def __send_notification(self, message: str) -> str:
        print(message)


class ErrorReport:

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)


class ErrorHandler(ErrorReport):

    def __handle_report(self) -> None:
        self.__send_report()
    
    def __generate_report(self):
        print('TASK NOT SUPPORTED')

    def __send_report(self):
        self.__raise_error(f'ERROR reported: [{self.__generate_report}]')
