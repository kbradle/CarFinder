# NOTE
We created a local package for installation because one of our packages (the machine learning model) was too large to upload to PyPi because of their 60 mb file size limit.


# description
We used machine learning to identify a car's make, model, and year based soley on a photo. Under the "list of cars" tab you will see the cars that we specifically trained our model to identify and with 90% success. Cars outside of our list will have a smaller percentage of accuracy. 


# Setup
Make sure that you have the following installed:
- Python 3
- WSL's Ubuntu (Or some other Linux distro)
- You can run virtual enviroments


1. git clone https://github.com/kbradle/CarFinder

2. cd into the project directory and ensure that you can run pip commands, we reccommend a virtual environment.

3. Install the package with 'pip install dist/django-findcar-0.0.10.tar.gz' *THIS WILL TAKE AWHILE*

4. Run 'runmyserver'

5. Go to `http://127.0.0.1:8000/` in a browser.

Web page should be ready to use! 


# optional (virtual env setup)

1. once inside the project directory run 'virtualenv . -p python3'

2. run 'source bin/activate' to start your env 