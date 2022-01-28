import subprocess

if __name__ == "__main__":
    run_tests_command = "unittest-parallel -t . -s tests --coverage"
    subprocess.run(run_tests_command.split(" "), check=True, text=True)
