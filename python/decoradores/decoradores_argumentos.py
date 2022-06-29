""" una funcion que recibe una funcion y  debueove otra  oirdmi sdectdar itrhdirvalores vaire scalores de aldovalsorsvalores de funcione pythonpero  abn suoendelaejcuacun dela fredfresa fr errutioel c ntrl deunoi tepotwrl mas detal deo definir un genrardor esta deand the funcuuon de fredsgragrande del valor de como respe cuavar rs dgenrafir pero aemmanda demanda  avarible de de gen de ls los asldor oshhdcoanncada kkamdsa consumsuinlaoras wjfdslfñsldjfñlsdkjfñlasdkjflñkdjfisdflskfaislkdsjffaifdlfjldsjfifrosdlnñklv dsñ jfñfj lkfjlsjflñksufs fsflsdkjflkfjirffi fsfjft sfñdlijsdlsjfsldfkjj sdlfjdsksdojoscndme dao osd sodosolsod  rkvnaslr d e uson pjos  srlnduoasid vsldor sd u d ahovoasodrsdonsdsoisdaorb vls is deas dkfsdf ysdbasdu sdlaspjdselbsyduhfue sisdfe fisd fddysd ddyyd dydddoifuysdfishdfoshfksjdhfiahfksdhfiusdhfkjhdsfkdffgkshfgaskdflkfladkfwalfnjdhñlahdfódfldkjkadhflkdlkasdiajndstaslbadoshakdflksdfhidfekjfgahjdfñldshfskdsoslomnteysb ctdtrISDECONAUAODMAMNSAVARB EHDLAOSQUEBACRJOIANIASNCEL 
"""


from gzip import READ


def funciondeco(funciondecob):
    def funciondecoc(*args, **kwargs):
        print("****hola esto es un decorador*****")
        # pass
        resultado=funciondecob(*args, **kwargs)
        print("depues hola esto es un decorador")
        return resultado

    return funciondecoc 

@funciondeco
def sumar(a,b):
    return a+b
# def mostrar():
#     print("esta funcion imprime otra")
# mostrar()
resultado=sumar(5,6)
print(f'el resultado de la suma es {resultado}')

