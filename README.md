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
