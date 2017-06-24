import logging

logging.basicConfig(filename='example.log', filemode='w',
                    format='%(asctime)s %(message)s',datefmt='%d/%m/%Y %I:%M %p',
                    level=logging.CRITICAL)

logging.critical('Param-pam ERRRRORR!')
logging.critical('tum-tudum-WAARNING!!!!')
