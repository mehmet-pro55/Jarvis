class TaskExecutor:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def execute_tasks(self):
        for task in self.tasks:
            print(f'Executing task: {task}')  # Placeholder for actual task execution logic
            # Actual execution code would go here

    def clear_tasks(self):
        self.tasks.clear()