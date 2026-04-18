import os
import subprocess

class CodeGenerator:
    def __init__(self, code:str):
        self.code = code

    def execute(self):
        # Execute the code safely
        # Warning: This is a simple example and may not cover all security aspects.
        try:
            result = subprocess.run(['python', '-c', self.code], capture_output=True, text=True)
            return result.stdout, result.stderr
        except Exception as e:
            return '', str(e)

    def save_to_file(self, file_path:str):
        # Save the code to a specified file path
        with open(file_path, 'w') as f:
            f.write(self.code)

    @classmethod
    def from_file(cls, file_path:str):
        # Load code from a specified file path
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                code = f.read()
            return cls(code)
        else:
            raise FileNotFoundError(f"{file_path} not found")
