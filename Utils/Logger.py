import logging

def initialize_logger(name='Logger to record the flow of Webservice Books',logfile=r"C:\Users\swetha_senthilkumar\PycharmProjects\demoqaBooks\pytestlogs.log",level=logging.INFO):
    #Create the logger
       logger=logging.getLogger(name)
       logger.setLevel(level)
    #File handle
       filehandler=logging.FileHandler(logfile)
       filehandler.setLevel(level)
    #Format
       formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
       filehandler.setFormatter(formatter)
    #Adding the file to logger
       logger.addHandler(filehandler)

       return logger
