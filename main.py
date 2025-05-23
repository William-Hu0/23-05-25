from studente import Studente
from rettangolo import Rettangolo

studente0=Studente("William","3FINF",[],)

studente0.aggiungi_voto(8)
studente0.aggiungi_voto(9)
studente0.aggiungi_voto(10)

studente0.stampa_info()

ret0=Rettangolo(12,6,"blu")
ret1=Rettangolo(3,4,"verde")
ret2=Rettangolo(7,3,"bianco")

ret0.stampa_info()
ret1.stampa_info()
ret2.stampa_info()