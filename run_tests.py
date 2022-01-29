import subprocess

if __name__ == "__main__":
    run_tests_command = (
        "unittest-parallel -t . -s tests --coverage --coverage-rcfile .coveragerc"
    )
    subprocess.run(run_tests_command.split(" "), check=True, text=True)
