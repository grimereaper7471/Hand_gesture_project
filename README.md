# Hand_gesture_project
Using Hagrid dataset to create a hand and gesture classification model 

To run the code first the user need to create a python enviroment with python 3.9:

To do this first install Miniconda3 on to your system this can be done with ever the windows or linux installer and making sure that when the propt to and miniconda to the path that it is checked, then to make the process of creating the enviroment faster micromamba is used. This is a shell for conda.

The way to install micromamba is first to open a powershell terminal and make sure that miniconda is install by type in `conda` then to run this code `conda install mamba -n base -c conda-forge` and to make sure it install properly type in `mamba`

Once mamba is setup with in powershell to create the need python enviroment simple run this code:
`mamba create -n threenine python=3.9 -c conda -c conda-forge`
If the user want they can add a `-c nvidia` to the end of the code

Then make sure that pipenc is intall with in the enviroment first activate the enviroment by type into the terminal
`mamba activate threenine` this will enter you into the mamba enviroment, once inside type into the terminal
`mamba install pipenv` this will intall pipenc into the mamaba enviroment

Next cd into the derectory you want to clone this github repository into and clone it into that derectory.

If done correct you should be able to see the clone repository with in the want decertory with a zipped file called hagrid unzip this file.

Next cd into the cloned enviroment and make sure using `ls` that it does have the pipenv file and the piplock file then run `ipenv install`and then after run `pip shell`

This will install all need files and derectorys however opencv seems to have a strange bug so make it work simple unistall it and reinstal it using `pip uninstall opencv-python` `pip install opencv-python`

to test if it works simple run ever the hand detection.py or the hand classification.py
