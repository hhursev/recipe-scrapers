import subprocess

if __name__ == "__main__":
    run_tests_command = "coverage run -m unittest discover -t . -s tests"
    subprocess.run(run_tests_command.split(" "), check=True, text=True)
