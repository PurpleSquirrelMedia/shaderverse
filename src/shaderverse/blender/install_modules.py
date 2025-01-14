import subprocess
import sys




def install_modules():
    python_path = sys.executable
    required = {'uvicorn[standard]', 'fastapi', 'pydantic', 'pyngrok', 'psutil'}

    # subprocess.run([python_path, "-m", "ensurepip"], capture_output=True)
    # subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip",])
    
    result = subprocess.run([python_path, "-m", "pip", "install", *required], capture_output=True)

    
if __name__ == "__main__":
    install_modules()
