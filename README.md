# install virtualenv if not installed
$ [sudo] pip install virtualenv

# if virtualenv setup fail
$ export LC_ALL="en_US.UTF-8"
$ export LC_CTYPE="en_US.UTF-8"

# create virtual environment ( here i create it on folder m )
$ virtualenv ml  [ if it sets python2 default try $ virtualenv -p python3 ml ]

# activate virtulaenv
$ source ml/bin/activate

#install tkinter
$ sudo apt-get install python3-tk

# install numpy scipy matplotlib ipython scikit-learn
$ pip install numpy scipy matplotlib ipython scikit-learn

#install panda
$ pip install pandas