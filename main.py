# Desenvolvido para suportar simulações computacionais em física - métodos iterativos / método das diferenças finitas
# Ajeitar possíveis questões estéticas para matrizes com números mais feios, func: printMatrix()

class Matrix:
    def __init__(self, elements, m, n):
        self.elements = elements
        self.m = m 
        self.n = n

    def printMatrix(self):
        exist = (len(self.elements) == self.m * self.n)
        
        if exist == True:
            for i in range(self.m):
                elementsI = []
                for j in range(self.n):
                    elementsI.append(self.elements[self.n * i + j])

                print(elementsI)
        else:
            print('\33[31mERRO 1. Dimensão incompatível.\33[m')

    def printElement(self, i, j):
        exist = (i <= self.m and j <= self.n)

        if exist == True:
            print(self.elements[(j - 1) + (i - 1) * self.n])
        else:
            print('\33[31mERRO 2. Elemento não encontrado.\33[m')

    @staticmethod
    def sum(A, B):
        exist = (A.m == B.m and A.n == B.n)
        newElements = []

        if exist == True:
            for i in range(A.m):
                for j in range(A.n):
                    newElements.append(A.elements[A.n * i + j] + B.elements[A.n * i + j])
        else: 
            print('\33[31mERRO 1. Dimensão incompatível.\33[m')

        return Matrix(newElements, A.m, A.n)

    @staticmethod
    def sub(A, B):
        exist = (A.m == B.m and A.n == B.n)
        newElements = []

        if exist == True:
            for i in range(A.m):
                for j in range(A.n):
                    newElements.append(A.elements[A.n * i + j] - B.elements[A.n * i + j])
        else: 
            print('\33[31mERRO 1. Dimensão incompatível.\33[m')

        return Matrix(newElements, A.m, A.n)
    
    def multByEsc(self, a):
        newElements = []
        for i in range(self.m):
            for j in range(self.n):
                newElements.append(a * self.elements[i * self.n + j])

        return Matrix(newElements, self.m, self.n)

    def ijElementMult(self, B, i, j):
        exist = (self.n == B.m)
        parcels = []

        if exist == True:
            for k in range(self.n):
                parcels.append(self.elements[self.n * (i - 1) + k] * B.elements[B.n * k + (j - 1)])
        else:
            print('\33[31mERRO 1. Dimensão incompatível.\33[m')

        return sum(parcels)
    
    def mult(self, B):
        elementsMult = []

        for i in range(self.m):
            for j in range(B.n):
                elementsMult.append(self.ijElementMult(B, i + 1, j + 1))
        
        return Matrix(elementsMult, self.m, B.n)
    
    @staticmethod
    def identity(n):
        identityElements = []

        for i in range(n):
            for j in range(n):
                if i == j:
                    identityElements.append(1)
                else:
                    identityElements.append(0)

        return Matrix(identityElements, n, n)
    
    def trans(self):
        transElements = []

        for i in range(self.m):
            for j in range(self.n):
                transElements.append(self.elements[self.n * j + i])

        return Matrix(transElements, self.n, self.m)
    
    def ijsubMatrix(self, i, j):
        exist = (i <= self.m and j <= self.n)
        newElements = []

        if exist == True:
            for l in range(self.m):
                for k in range(self.n):
                    if not(l == i - 1 or k == j - 1):
                        newElements.append(self.elements[self.n * l + k])
                    else:
                        pass
        else:
            print('\33[31mERRO 2. Elemento não encontrado.\33[m')

        return Matrix(newElements, self.m - 1, self.n - 1)
    
    def det(self):
        exist = (self.m == self.n)
        parcels = []

        if exist == True:
            if self.n != 1:
                for i in range(self.m):
                    parcels.append(self.elements[self.n * i] * (-1) ** i * self.ijMatrix(i + 1, 1).det())
            else:
                parcels.append(self.elements[0])
        else:
            print('\33[31mERRO 1. Dimensão incompatível.\33[m')

        return sum(parcels)
    
    def ijCof(self, i, j):
        return self.ijMatrix(i, j).det() * (-1)**(i + j)

    def cofMatrix(self):
        cofElements = []

        for i in range(self.m):
            for j in range(self.n):
                cofElements.append(self.ijCof(i + 1, j + 1))

        return Matrix(cofElements, self.m, self.n)

    def inv(self):
        return self.cofMatrix().trans().multByEsc(1 / (self.det()))

    def cleanMatrix(self):
        for i in range(self.m):
            for j in range(self.n):
                if abs(self.elements[i * self.n + j]) < 10 ** (-15):
                    self.elements[i * self.n + j] = 0
        
        return Matrix(self.elements, self.m, self.n)
