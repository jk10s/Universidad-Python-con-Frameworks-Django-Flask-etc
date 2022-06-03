class Convertidos:
    MAXC=100
    MAXF=213

    @classmethod
    def c_f8(cls,celsios):
        if celsios > cls.MAXC:
            raise ValueError(f"temperatura c deamsioa alta: {celsios}")
        return celsios* 9/5 + 32

    @classmethod
    def c_fc(cls,fa):
        if fa > cls.MAXF:
            raise ValueError(f"temperatura fffff deamsioa alta: {fa}")
        return (fa -32)*5/9

if __name__=='__main__':
    resultado=Convertidos.c_f8(15)
    print(f'10 f ac: {resultado:.2f}')
    resultado=Convertidos.c_fc(10)
    print(f'10 f ac: {resultado:.2f}')