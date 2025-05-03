import tkinter as tk
from tkinter import ttk, messagebox, Text, Scrollbar, Frame


class ChiffrementVagues:
    def __init__(self, n, offset):
        if n < 2:
            raise ValueError("n doit être supérieur ou égal à 2")
        if offset < 0 or offset > 2 * n - 3:
            raise ValueError(f"offset doit être compris entre 0 et {2 * n - 3}")

        self.n = n
        self.offset = offset

    def chiffrer(self, texte):
        texte = texte.replace(" ", "").upper()

        colonnes = len(texte) + self.offset
        tableau = [['' for _ in range(colonnes)] for _ in range(self.n)]

        ligne = 0
        direction = 1
        caractere_index = 0

        for col in range(colonnes):
            if col >= self.offset and caractere_index < len(texte):
                tableau[ligne][col] = texte[caractere_index]
                caractere_index += 1

            if ligne == 0 and direction == -1:
                direction = 1
            elif ligne == self.n - 1 and direction == 1:
                direction = -1

            ligne += direction

        texte_chiffre = ''
        for i in range(self.n):
            for j in range(colonnes):
                if tableau[i][j]:
                    texte_chiffre += tableau[i][j]

        return texte_chiffre, tableau

    def get_vague_positions(self, longueur):
        """Obtient toutes les positions en vague pour une longueur donnée"""
        positions = []
        ligne = 0
        direction = 1

        for col in range(longueur):
            positions.append((ligne, col))

            if ligne == 0 and direction == -1:
                direction = 1
            elif ligne == self.n - 1 and direction == 1:
                direction = -1

            ligne += direction

        return positions

    def get_valid_vague_after_offset(self, texte):
        """Obtient les positions de vague pour le texte après offset"""
        longueur = len(texte) + self.offset
        return self.get_vague_positions(longueur)[self.offset:]

    def dechiffrer(self, texte_chiffre):
        texte_chiffre = texte_chiffre.replace(" ", "").upper()

        longueur_totale = len(texte_chiffre) + self.offset

        tableau = [['' for _ in range(longueur_totale)] for _ in range(self.n)]

        positions_vague = self.get_vague_positions(longueur_totale)

        positions_avec_caracteres = positions_vague[self.offset:][:len(texte_chiffre)]

        positions_triees = sorted(positions_avec_caracteres, key=lambda pos: (pos[0], pos[1]))

        for i, (ligne, col) in enumerate(positions_triees):
            if i < len(texte_chiffre):
                tableau[ligne][col] = texte_chiffre[i]

        texte_dechiffre = ''
        for ligne, col in positions_avec_caracteres:
            texte_dechiffre += tableau[ligne][col]

        return texte_dechiffre

    def afficher_tableau(self, tableau, ignorer_offset=True):
        debut_col = self.offset if ignorer_offset else 0

        tableau_vide = True
        for ligne in tableau:
            for col_idx in range(debut_col, len(ligne)):
                if ligne[col_idx]:
                    tableau_vide = False
                    break
            if not tableau_vide:
                break

        if tableau_vide and ignorer_offset:
            return

        resultat = ""

        for ligne in tableau:
            ligne_texte = ""
            for col_idx in range(debut_col, len(ligne)):
                if ligne[col_idx]:
                    ligne_texte += ligne[col_idx] + " "
                else:
                    ligne_texte += "· "
            resultat += ligne_texte + "\n"

        return resultat


class InterfaceVagues:
    def __init__(self, root):
        self.root = root
        self.root.title("Chiffrement par Vagues")
        self.root.state('zoomed')

        self.n_var = tk.IntVar(value=6)
        self.offset_var = tk.IntVar(value=0)

        self.creer_interface()

    def creer_interface(self):
        main_frame = Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        params_frame = Frame(main_frame)
        params_frame.pack(fill=tk.X, pady=5)

        ttk.Label(params_frame, text="n (lignes):").grid(row=0, column=0, padx=5, pady=5)
        self.n_spinbox = ttk.Spinbox(params_frame, from_=2, to=20, textvariable=self.n_var, width=5)
        self.n_spinbox.grid(row=0, column=1, padx=5, pady=5)
        self.n_spinbox.bind("<<Increment>>", self.update_contrainte)
        self.n_spinbox.bind("<<Decrement>>", self.update_contrainte)

        ttk.Label(params_frame, text="offset:").grid(row=0, column=2, padx=5, pady=5)
        self.offset_spinbox = ttk.Spinbox(params_frame, from_=0, to=9, textvariable=self.offset_var, width=5)
        self.offset_spinbox.grid(row=0, column=3, padx=5, pady=5)

        self.contrainte_label = ttk.Label(params_frame, text="Contrainte: 0 ≤ offset ≤ ?")
        self.contrainte_label.grid(row=0, column=4, padx=10, pady=5)
        self.update_contrainte()

        ttk.Label(main_frame, text="Texte original:").pack(anchor=tk.W, pady=(10, 0))
        self.texte_entree = Text(main_frame, height=5, width=80)
        self.texte_entree.pack(fill=tk.X, pady=5)

        boutons_frame = Frame(main_frame)
        boutons_frame.pack(fill=tk.X, pady=5)

        self.bouton_chiffrer = ttk.Button(boutons_frame, text="Chiffrer ↓", command=self.chiffrer)
        self.bouton_chiffrer.pack(side=tk.LEFT, padx=5)

        self.bouton_dechiffrer = ttk.Button(boutons_frame, text="Déchiffrer ↑", command=self.dechiffrer)
        self.bouton_dechiffrer.pack(side=tk.LEFT, padx=5)

        ttk.Label(main_frame, text="Texte chiffré:").pack(anchor=tk.W, pady=(10, 0))
        self.texte_sortie = Text(main_frame, height=5, width=80)
        self.texte_sortie.pack(fill=tk.X, pady=5)

        ttk.Label(main_frame, text="Visualisation:").pack(anchor=tk.W, pady=(10, 0))

        visualisation_frame = Frame(main_frame)
        visualisation_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        scrollbar_y = Scrollbar(visualisation_frame, orient=tk.VERTICAL)
        scrollbar_x = Scrollbar(visualisation_frame, orient=tk.HORIZONTAL)

        self.affichage_tableau = Text(
            visualisation_frame,
            height=15,
            width=120,
            font=("Courier New", 10),
            wrap=tk.NONE,
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        scrollbar_y.config(command=self.affichage_tableau.yview)
        scrollbar_x.config(command=self.affichage_tableau.xview)

        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.affichage_tableau.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def update_contrainte(self, event=None):
        n = self.n_var.get()
        max_offset = 2 * n - 3
        self.contrainte_label.config(text=f"Contrainte: 0 ≤ offset ≤ {max_offset}")
        self.offset_spinbox.config(to=max_offset)

        if self.offset_var.get() > max_offset:
            self.offset_var.set(max_offset)

    def chiffrer(self):
        try:
            n = self.n_var.get()
            offset = self.offset_var.get()

            max_offset = 2 * n - 3
            if offset < 0 or offset > max_offset:
                messagebox.showerror("Erreur", f"offset doit être compris entre 0 et {max_offset}")
                return

            texte = self.texte_entree.get("1.0", tk.END).strip()
            if not texte:
                messagebox.showwarning("Attention", "Veuillez saisir un texte à chiffrer.")
                return

            chiffreur = ChiffrementVagues(n, offset)
            texte_chiffre, tableau = chiffreur.chiffrer(texte)

            self.texte_sortie.delete("1.0", tk.END)
            self.texte_sortie.insert("1.0", texte_chiffre)

            self.affichage_tableau.delete("1.0", tk.END)
            self.affichage_tableau.insert("1.0", chiffreur.afficher_tableau(tableau, ignorer_offset=True))

        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def dechiffrer(self):
        try:
            n = self.n_var.get()
            offset = self.offset_var.get()

            max_offset = 2 * n - 3
            if offset < 0 or offset > max_offset:
                messagebox.showerror("Erreur", f"offset doit être compris entre 0 et {max_offset}")
                return

            texte_chiffre = self.texte_sortie.get("1.0", tk.END).strip()
            if not texte_chiffre:
                messagebox.showwarning("Attention", "Veuillez saisir un texte à déchiffrer.")
                return

            chiffreur = ChiffrementVagues(n, offset)
            texte_dechiffre = chiffreur.dechiffrer(texte_chiffre)

            self.texte_entree.delete("1.0", tk.END)
            self.texte_entree.insert("1.0", texte_dechiffre)

            _, tableau = chiffreur.chiffrer(texte_dechiffre)
            self.affichage_tableau.delete("1.0", tk.END)
            self.affichage_tableau.insert("1.0", chiffreur.afficher_tableau(tableau, ignorer_offset=True))

        except Exception as e:
            messagebox.showerror("Erreur", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceVagues(root)
    root.mainloop()