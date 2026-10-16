'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

class ApiConnection:
    """Responsável exclusivamente por gerenciar a conexão com a API."""
    def __init__(self):
        self.connect()

    def connect(self):
        print('Connecting to API...')


class TaskValidator:
    """Responsável exclusivamente por validar se a tarefa é válida."""
    def validate(self, task: str) -> bool:
        return isinstance(task, str)


class ErrorHandler:
    """Responsável exclusivamente por gerar e reportar erros."""
    def handle_error(self, message: str) -> None:
        print(f'ERROR reported: {message}')
        raise Exception(message)


class NotificationService:
    """Responsável exclusivamente por enviar notificações."""
    def send_notification(self, message: str) -> None:
        print(message)


class TaskManager:
    """ Responsável exclusivamente pelas 
    operações de gerenciamento de tarefas. """
    
    def create_task(self, task: str) -> None:
        print(f'Creating TASK: {task}')

    def update_task(self, task: str) -> None:
        print(f'Updating TASK: {task}')

    def remove_task(self, task: str) -> None:
        print(f'Removing TASK: {task}')


class TaskHandler:
    """ Responsável por coordenar o fluxo de execução da tarefa, 
    delegando cada responsabilidade para sua respectiva classe especializada. """
    
    def __init__(self, validator: TaskValidator, manager: TaskManager, error_handler: ErrorHandler):
        self.validator = validator
        self.manager = manager
        self.error_handler = error_handler

    def task_handle(self, task: str) -> None:
        if not self.validator.validate(task):
            self.error_handler.handle_error('TASK NOT SUPPORTED')
        else:
            self.manager.create_task(task)
            self.manager.update_task(task)
            self.manager.remove_task(task)


if __name__ == "__main__":
    
    api = ApiConnection()
    validator = TaskValidator()
    manager = TaskManager()
    error_handler = ErrorHandler()
    
    handler = TaskHandler(validator, manager, error_handler)

    print("\n--- Testando com tarefa válida ---")
    handler.task_handle("Estudar Princípios SOLID")

    print("\n--- Testando com tarefa inválida (disparará exceção) ---")
    try:
        handler.task_handle(123) # <- Passando um inteiro em vez de string
    except Exception as e:
        print(f"Exceção capturada com sucesso: {e}")
