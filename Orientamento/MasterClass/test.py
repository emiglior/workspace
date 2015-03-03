#!/usr/bin/env python

import os  
import sys
import email
import datetime
from email.utils import parsedate_tz
from optparse import OptionParser

from registration import Registration

#################
def main():            
    
# command line options
    parser = OptionParser()
    parser.add_option("-i", "--input-dir",  
                      action="store", type="string", dest="input_dir",
                      help="input dir")

    (options, args) = parser.parse_args()

    for filename in os.listdir(options.input_dir):
        fp = open(os.path.join(options.input_dir,filename),'r')
        msg = email.message_from_file(fp)
        datetime_tuple = parsedate_tz(msg.get('Date'))
        for part in msg.walk():
             if part.get_content_type() == 'text/plain':
                 reg = Registration(datetime_tuple, part.get_payload())
                 for index, student in enumerate(reg.get_studenti()):
                     print index+1, '\t', reg.get_studente(index), '\t',  reg
                 
        fp.close()

if __name__ == "__main__":        
    main()
