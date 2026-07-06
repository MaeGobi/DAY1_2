def fonction(X):
    n_lignes = len(X)
    n_cols = len(X[0])

    moyennes = []

    for j in range(n_cols):
        somme = 0
        for i in range(n_lignes):
            somme += X[i][j]

        moyennes.append(float(somme / n_lignes))

    return moyennes