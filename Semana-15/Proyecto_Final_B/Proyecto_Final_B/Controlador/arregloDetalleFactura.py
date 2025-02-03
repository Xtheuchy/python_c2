from Controlador.detalleFactura import DetalleFactura

class ArregloDetalleFactura:
    def __init__(self):
        self.dataDetalleFactura = []

    def adicionaDetalleFactura(self,objDetFact):
        self.dataDetalleFactura.append(objDetFact)

    def devolverDetalleFactura(self,pos):
        return self.dataDetalleFactura[pos]
    
    def tamañoDetalleFactura(self):
        return len(self.dataDetalleFactura)
    
    def buscarDetalleFactura(self, nDocumentoFactura):
        for i in range(self.tamañoDetalleFactura()):
            if nDocumentoFactura == self.dataDetalleFactura[i].getnroCom():
                return i
        return -1
    
    def eliminarDetalleFactura(self,indice):
        del(self.dataDetalleFactura[indice])
