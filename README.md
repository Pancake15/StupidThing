# ds-boot-camp-prep

This repository has three purposes:

1.  To test that you are able to set up a conda environment and execute code in a Jupyter notebook using that environment.
2.  To give you an self-assessment of your Python fundamentals.  
3.  To give you a self-assessment of your statistics fundamentals.  TODO:  write stats self-assessment.

### Conda environment and running Jupyter notebooks

Check to make sure you have conda by running the following in your command line interface:

    conda --version

If you don't have conda, google how to install it!

Once you have conda run:

    conda env create  --file=environment.yml

Press [y] to all of the prompts.  You will be downloading a lot of packages.

Once this is done:

    conda activate ds-boot-camp-prep

To check everything is there:

    conda list

Should show all of the packages!

Finally open `find_secret_code.ipynb` using VSCode.  Execute the only cell there and enter the "secret code" which appears in the appropriate place on the course homepage (TODO:  implement input box).

### Python Prerequisite Self-Assessment

Complete the exercises in `python_prereq_quiz.ipynb` without using anything beyond official documentation.  Check your answers against `python_prereq_solutions.ipynb`.  Please resist the temptation to peak at the solutions before trying the quiz yourself!  If you find this quiz difficult we recommend that you take our [Python Prep Course](https://www.erdosinstitute.org/programs/asynchronous/python-prep).

### Statistical Prerequisite Self-Assessment

TODO:  Write this self-assessment.
