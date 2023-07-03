import os
import timeit
import subprocess

def main():
    # Ask for a filename
    filename = "main"

    # List all the .in files
    input_files = ['1.in','2.in','3.in']

    # Initialize counters
    total_cases = 0
    correct_cases = 0

    # Determine the file extension and choose the appropriate run command
    if os.path.isfile(f"{filename}.py"):
        command = f"python {filename}.py"
    elif os.path.isfile(f"{filename}.java"):
        subprocess.run(["javac", f"{filename}.java"])
        command = f"java {filename}"
    elif os.path.isfile(f"{filename}.c"):
        subprocess.run(["gcc", "-o", f"{filename}", f"{filename}.c"])
        command = f"./{filename}"
    elif os.path.isfile(f"{filename}.cpp"):
        subprocess.run(["g++", "-o", f"{filename}", f"{filename}.cpp"])
        command = f"./{filename}"
    else:
        print(f"No valid file found for {filename}.")
        return

    # Run the chosen command on each .in file and compare output to .ans file
    for in_file in input_files:
        ans_file = in_file.replace('.in', '.ans')
        # Run the command and time it
        start_time = timeit.default_timer()

        try:
            output = subprocess.check_output(f"{command} < {in_file}", shell=True, timeout=1).decode()
        except subprocess.TimeoutExpired:
            print(f"Time limit exceeded for test case: {in_file}.")
            continue
        except Exception as e:
            print(f"Error occurred while running test case {in_file}: {str(e)}")
            continue

        elapsed = timeit.default_timer() - start_time

        # Open the answer file and compare
        with open(ans_file, 'r') as f:
            ans = f.read()

        if ''.join(output).replace('\n','') == ''.join(ans).replace('\n',''):
            print("Pass")
            correct_cases += 1
        else:
            print("Fail, you have",output,'but expected',ans)

if __name__ == "__main__":
    main()
