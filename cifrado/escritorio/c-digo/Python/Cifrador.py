
from Texto.TextoPlano import TextoPlano
from Cifrados.cifradoCesar import CifradoCesar
from Cifrados.cifradoTInversa import CifradoTInversa
from Cifrados.cifradoTGrupo import CifradoTGrupo

class Cifrador:

    def __init__(self):
        self.text = TextoPlano("")
        self.cifC = CifradoCesar("", 3)
        self.cifTG = CifradoTGrupo("", 3)
        self.cifTI = CifradoTInversa("")
        self.palabra_aux = ""

    def datoExternoTXT(self, nuevo ,val ,val2):
        self.palabra_aux = nuevo
        resp = TextoPlano(nuevo)
        self.text.diference(nuevo)

        self.ActualizarcifradoRev(resp,nuevo)
        self.ActualizarcifradoCesar(nuevo ,val)
        self.ActualizarcifradoRevGroup(nuevo ,val2)

        self.text.refresh(nuevo)

    def ActualizarcifradoRev(self ,resp,txt):
        if self.text.backOne(resp):
            self.cifTI.back()
        elif self.text.step(resp):
            self.cifTI.front(self.text.textoDiferen)
        else:
            self.cifTI.cifra(txt)

    def ActualizarcifradoCesar(self ,txt,salto):
        self.cifC.cifrar(txt,salto)

    def ActualizarcifradoRevGroup(self ,txt,group):
        self.cifTG.cifrar(txt,group)

