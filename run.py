
import argparse
import conftest
import pytest
import subprocess
"""
    pip install pytest
    Usage :
    python .\run.py -s                                          # Simulate setup
    python .\run.py -r                                          # run all tests
    python .\run.py -rt  tests\test_simple.py                   # run specific test file
    python .\run.py -rt  tests\test_simple.py::test_always_pass # run specific test
    python .\run.py -rg math                                    # run test group
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pytest lab')
    parser.add_argument('-s', '--setup',
                    help='setup mode', action='store_true')
    parser.add_argument('-r','--run', help='run test', action='store_true')
    parser.add_argument('-rt','--run_test_file', help='run test file')
    parser.add_argument('-rg','--run_group', help='run test group')
    args = parser.parse_args()
    if args.setup:
        conftest.setup()
    elif args.run:
        completed_process = subprocess.run(['pytest', 'tests'])
        assert completed_process.returncode == 0
    elif args.run_test_file:
        sub_p = subprocess.run(['pytest', args.run_test_file])
    elif args.run_group:
        sub_p = subprocess.run(['pytest', '-m', args.run_group])
    else :
        raise Exception ('unsupported parameter')
