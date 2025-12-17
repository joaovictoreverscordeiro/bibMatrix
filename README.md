# Lista de métodos da classe Matrix:

## `__init__(self, elements, m, n)`:

Nesse método, são armazenados os parêmetros da classe: `elements`, `m` e `n`.

### **1.** `m` e `n`:

`m` é o número de linhas que a matriz definida possui, enquanto `n` é o número de colunas. Ambos são int's.

### **2.** `elements`:

É a lista de elementos da matriz definida. Essa lista, deve ter $$m\times n$$ elementos, que devem ser int's ou float's. Caso você não insira o número correto de elementos, o ERRO 1 será chamado.

O elemento `(i, j) -> (linha, coluna)` da matriz corresponde ao `elements[(i - 1) * n + (j - 1)]`. Ou seja, lemos linha por linha.

## `printMatrix(self)`:

Esse método não depende de outros parâmetros. Ele printa a matriz para o qual é chamado:

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
A.printMatrix()
```

**Output**
```Output
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```
## `printElement(self, i, j)`

Esse método depende dos parâmetros `(i, j) -> (linha, coluna)` que localizam o elemento que será _printado_. Note que aqui usamos a convenção matemática usual, onde a contagem começa do 1. Logo:

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
A.printElement(2, 3)
```

**Output**
```Output
6
```

## `@staticmethod sum(A, B) e sub(A, B)`  

Esses métodos estáticos são usados para somar/subtrair os dois parêmetros A e B, que são Matrix's. A subtração será feita da na ordem $$A - B$$.

**Input**

```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
B = Matrix([1, 0, 0, 0, 1, 0, 0, 0, 1], 3, 3)
C = Matrix.sum(A, B)
D = Matrix.sub(A, B)

C.printMatrix()
print()
D.printMatrix()
```

**Output**

```Output
[2, 2, 3]
[4, 6, 6]
[7, 8, 10]

[0, 2, 3]
[4, 4, 6]
[7, 8, 8]
```

## `multByEsc(self, a)`:

Esse método multiplica o `self` por um escalar $$a$$. 

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
B = A.multByEsc(2)
B.printMatrix()
```

**Output**
```Output
[2, 4, 6]
[8, 10, 12]
[14, 16, 18]
```

## `ijElementMult(self, B, i, j)`:

Esse método foi criado para ser um método auxiliar na multiplicação de matrizes, mas pode ser usado como qualquer outro. Seus parâmetros são `B -> Matrix`, `(i, j) -> (linha, coluna)`. Aqui, efetuamos a multiplicação $$A\cdot B$$ e, então, obtemos o elemento localizado por `(i, j)`.

Por exmemplo:

$$
C = \begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{pmatrix}\cdot\begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{pmatrix} = \begin{pmatrix}
30 & 36 & 42\\
66 & 81 & 96\\
102 & 126 & 150\\
\end{pmatrix}
$$

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
print(A.ijElementMult(A, 3, 3))
```

**Output**
```Output
150
```

## `mult(self, B)`:

Esse método realiza a multiplicação de self por B, que também é uma matriz. 

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
B = A.mult(A)
B.printMatrix()
```

**Output**
```Output
[30, 36, 42]
[66, 81, 96]
[102, 126, 150]  
```

Como a ordem importa na multiplicação de matrizes, você deve notar que `A.mult(B)` equivale a $$A\cdot B$$.

## `@staticmethod identity(n)`:

Esse método estático retorna a matriz identidade de ordem igual ao parâmetro $$n$$. 

**Input**
```Input
A = Marix.identity(3)
A.printMatrix()
```

**Output**
```Output
[1, 0, 0]
[0, 1, 0]
[0, 0, 1]
```

## `trans(self)`:

Esse método retorna a matriz transposta do `self`.

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
B = A.trans()
B.printMatrix()
```

**Output**
```Output
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
```

## `ijsubMatrix(self, i, j)`:

Esse método foi criado como um método auxiliar para o método que calcula o determinante. Os parâmetros são `self`, `(i, j) -> (linha, coluna)`. Ele resulta na submatriz excluindo a linha e coluna do elemento `(i, j)`.

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
B = A.ijsubMatrix(1, 1)
B.printMatrix()
```

**Output**
```Output
[5, 6]
[8, 9]
```

A matriz resultante sempre vai ter a ordem inferior em uma unidade da original.

## `det(self)`

Esse método calcula o determinante do `self`.

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
print(A.det())
```

**Output**
```Output
0
```

## `ijCof(self, i, j)`

Calcula o cofator do elemento localizado por `(i, j) -> (linha, coluna)`. 

**Input**
```Input
A = Matrix([1, -1, -1, 2, 3, 8, -3, 2, 1], 3, 3)
print(A.ijCof(2, 1))
```

**Output**
```Output
-1
```

## `cofMatrix(self)`

Esse método retorna a matriz dos cofatores de `self`.

**Input**
```Input
A = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
B = A.cofMatrix()
B.printMatrix()
```

**Output**
```Output
[-3, 6, -3]
[6, -12, 6]
[-3, 6, -3]
```

## `inv(self)`

Retorna a matriz inversa da sua matriz original. Note que ela pode estar sujeita a pequenas flutuações que podem ser resolvidas com o próximo método documentado.

**Input**
```Input
A = Matrix([1, 8, 9, 6, 5, 10, 7, 5, 12], 3, 3)
B = A.inv()
B.printMatrix()
```

**Output**
```Output
[-0.19607843, 1, -0.68627451]
[0.03921569, 1, -0.86274510]
[0.09803922, -1, 0.84313725]
```

## `cleanMatrix(self)`:

Se usarmos uma matriz e multiplicar pela sua inversa, obteremos uma matriz que não é a identidade.

**Input**
```Input
A = Matrix([1, 8, 9, 6, 5, 10, 7, 5, 12], 3, 3)
A.inv().mult(A).printMatrix()
```

**Output**
```Output
[1.0000000000000002, -2.220446049250313e-16, 8.881784197001252e-16]
[1.3877787807814457e-16, 0.9999999999999993, -5.551115123125783e-16]
[3.469446951953614e-16, 1.1102230246251565e-16, 0.9999999999999996]
```

Um resultado que, obviamente, está incorreto. Devido a pequenas instabilidades na forma com que o computador calcula os resultados numéricos, a matriz final printada está próxima, mas não é exatamente o que esperamos - uma matriz identidade de ordem 3. Para corrigir, faça:

**Input**
```Input
A = Matrix([1, 8, 9, 6, 5, 10, 7, 5, 12], 3, 3)
B = A.inv().mult(A).cleanMatrix()
B.printMatrix()
```

**Output**
```Output
[1, 0, 0]
[0, 1, 0]
[0, 0, 1]
```

Esse método retorna uma matriz onde todas as entradas menores que $$10^{-15}$$ são arredondadas para $$0$$ e todas aquelas entre $$0,9999$$ e $$1$$ são arredondadas para $$1$$.

# Lista de erros

**1. (ERRO 1)** Dimensão incompatível. Significa que você pode ter tentado:
  - Salvar uma matriz com o número de elementos diferente do declarado;
  - Fazer operações com matrizes de dimensões incompatíveis: 
    - Determinantes com matrizes não quadradas.
    - Multiplicações com matrizes de ordem incompatível.
    - Somas ou subtrações com matrizes de dimensões diferentes.

**2. (ERRO 2)** Elemento não encontrado. Siginfica que você poder ter tentado:
  - Printar elementos que não existem.
  - Obter a subMatrix de elementos que não existem.
