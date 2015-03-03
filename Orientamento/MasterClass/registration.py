import re
import string 
import datetime

class Registration:
    """ simple class to handle MasterClass registrations in eml format"""
    def __init__(self, datetime_tuple, form):
        self.data = datetime.datetime(*datetime_tuple[:7])
        self.insegnante = []
        self.email = ''
        self.cellulare = ''
        self.scuola = ''
        self.studenti = []

        # split input string into multiline
        for line in form.splitlines():
            if re.match('^Nome',line):
                self.insegnante.append(line.split()[-1])
            elif re.match('^Cognome',line):     
                self.insegnante.append(line.split()[-1])
            elif re.match('^Scuola',line):        
                match = re.search(r"Scuola:\s(.*)", line)
                if match:
                    self.scuola = match.group(1)
                else:
                    self.scuola = ""
            elif re.match('^E-mail',line):    
                self.email = line.split()[-1] 
            elif re.match('^Cellulare',line):    
                match = re.search(r"Cellulare:\s(.*)", line)
                if match:
                    self.cellulare = match.group(1)
                else:
                    self.cellulare = ""
            elif re.match('^1.',line):        
                if line.split()[1] != '(classe':
                    self.studenti.append(line[2:])
            elif re.match('^2.',line):         
                if line.split()[1] != '(classe':
                    self.studenti.append(line[2:])
            elif re.match('^3.',line):       
                if line.split()[1] != '(classe':
                    self.studenti.append(line[2:])

        # capitalize
        for index, item in enumerate(self.insegnante):
            self.insegnante[index] = self.capitalize(item)             

        for ii, studente in enumerate(self.studenti):
            str_out = ''
            for index, item in enumerate( studente.split("(")[0].split() ):
                str_out += self.capitalize(item)
                str_out += ' '
            self.studenti[ii] = str_out


    def __repr__(self):
        """ pretty printing """
        str_out = self.data.strftime("%d/%m/%y %H:%M:%S \t")
        str_out += '%s %s \t' % (self.insegnante[0], self.insegnante[1])
        str_out += '%s \t' % self.email
        str_out += '%s \t' % self.cellulare
        str_out += '%s \t' % self.scuola 
#        str_out += '%d \n' % self.get_nstudenti()
        return str_out

    def get_data(self):
        return self.data
        
    def get_insegnante(self):
        return self.insegnante

    def get_email(self):
        return self.email

    def get_scuola(self):
        return self.scuola

    def get_studenti(self):
        return self.studenti

    def get_studente(self, index):
        return self.studenti[index].split("(")[0]

    def get_nstudenti(self):
        return len(self.studenti)

    def capitalize(self, str): 
        return str[:1].upper() + str[1:].lower()
