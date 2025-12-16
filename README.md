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
