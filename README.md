# python_sorting_visualiser
A sorting visualiser done in python. 

Various steps followed:
1. Set up a virtual environment for development purposes. 
2. create a recruitment.txt file for easy pip installation if needed on a code 
deployment to somewhere (server/docker container)  
3. basic steps and layout.
4. add pytests to the project. This will help in the addition of new sorting 
algorithms.
5. added a .gitignore.
6. basic project setup was completed.
7. start on some of the sorting algorithms 
8. after that start on creating a visual GUI for the damn visuals!!
9. think about some proper type of loggin.
10. create a manager in the base file, this is to launch the project and also 
to allow us to create more than one instance of the code base. ie. potentially
have all of the sorting algo's open at the same time.
11. added the pytest to the manage.py command executables as well. 
12. The above required that a pytest.ini file be created to indicate the path 
to be used when running pytests.


Steps to create a virtual environment. 
1. python3 -m venv venv
2. source ./venv/bin/activate
3. pip3 install -r requirements.txt

To automatically create a recruitments.txt file:
1. pip3 freeze > requirements.txt