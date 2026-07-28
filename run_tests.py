import subprocess
import os
import shutil
import sys

def run_tests():
    print("Starting test execution with Allure...")
    
    # Clean previous results if they exist
    if os.path.exists('reports'):
        shutil.rmtree('reports')
    
    # Run pytest
    # The --alluredir is already in pytest.ini, but we can be explicit
    result = subprocess.run([sys.executable, '-m', 'pytest', '--alluredir=reports', '--clean-alluredir'])
    
    if result.returncode == 0 or result.returncode == 1: # 1 means some tests failed, which is fine
        print("\nTests completed. Generating Allure report...")
        
        # Clean previous report if it exists
        if os.path.exists('allure-report'):
            shutil.rmtree('allure-report')
            
        # Generate report
        allure_cmd = shutil.which('allure') or os.path.expandvars(r'%APPDATA%\npm\allure.cmd')
        gen_result = subprocess.run([allure_cmd, 'generate', 'reports', '-o', 'allure-report', '--clean'])
        
        if gen_result.returncode == 0:
            print("\nAllure report generated successfully in 'allure-report' folder.")
            print("To view the report, run: allure open allure-report")
        else:
            print("\nFailed to generate Allure report. Make sure Allure command line tool is installed.")
    else:
        print(f"\nPytest failed with exit code {result.returncode}")

if __name__ == "__main__":
    run_tests()
