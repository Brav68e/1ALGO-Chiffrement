class Chiffrement1():

    def __init__(self, keyLeft, keyRight):
        
        self.keyLeft = keyLeft
        self.keyRight = keyRight
        self.InitialKeyLeft = keyLeft
        self.InitialKeyRight = keyRight



    def corres_right_left(self, letter):
        '''Return the corresponding letter of the right key in the left one'''

        return self.keyLeft[self.keyRight.find(letter)]
    

    def corres_left_right(self, letter):
        '''Return the corresponding letter of the left key in the right one'''

        return self.keyRight[self.keyLeft.find(letter)]
    

    def key_rotation(self, key, letter, pos):
        '''Shift the specified key until the letter is at the given position'''

        if key == "left":

            while self.keyLeft[pos] != letter:
                self.keyLeft = self.keyLeft[-1] + self.keyLeft[:-1]

        elif key == "right":

            while self.keyRight[pos] != letter:
                self.keyRight = self.keyRight[-1] + self.keyRight[:-1]


    def shift_key(self, key):
        '''Allow to store a letter at a specific pos and shift other letter at his left till shift_pos'''
        
        if key == "left":

            # Transform into a list to allow item assignement
            self.keyLeft = list(self.keyLeft)

            tmp_letter = self.keyLeft[1]
            self.keyLeft[1] = " "
            index = 1

            while self.keyLeft.index(" ") != 13:
                self.keyLeft[index], self.keyLeft[index+1] = self.keyLeft[index+1], self.keyLeft[index]
                index += 1
            
            self.keyLeft = [tmp_letter if letter == " " else letter for letter in self.keyLeft]
            self.keyLeft = "".join(self.keyLeft)


        elif key == "right":

            # Transform into a list to allow item assignement
            self.keyRight = list(self.keyRight)

            tmp_letter = self.keyRight[2]
            self.keyRight[2] = " "
            index = 2

            while self.keyRight.index(" ") != 13:
                self.keyRight[index], self.keyRight[index+1] = self.keyRight[index+1], self.keyRight[index]
                index += 1
            
            self.keyRight = [tmp_letter if letter == " " else letter for letter in self.keyRight]
            self.keyRight = "".join(self.keyRight)


    def encode(self, msg):
        '''Encode a message using all previously made methods'''

        encode_msg = ""

        for letter in msg:
            # Get the correspondance
            encode_letter = self.corres_right_left(letter)
            encode_msg += encode_letter
            # Rotation for both keys and shift
            self.key_rotation("left", encode_letter, 0)
            self.shift_key("left")

            self.key_rotation("right", letter, 25)
            self.shift_key("right")

        # Once done, make sure the left and right keys are the same as initial
        self.keyLeft = self.InitialKeyLeft
        self.keyRight = self.InitialKeyRight

        return encode_msg
    

    def decode(self, msg):
        '''Decode the given message'''

        decode_msg = ""

        for letter in msg:
            # Get the correspondance
            decode_letter = self.corres_left_right(letter)
            decode_msg += decode_letter
            # Rotation for both keys and shift
            self.key_rotation("left", letter, 0)
            self.shift_key("left")

            self.key_rotation("right", decode_letter, 25)
            self.shift_key("right") 

        # Once done, make sure the left and right keys are the same as initial
        self.keyLeft = self.InitialKeyLeft
        self.keyRight = self.InitialKeyRight

        return decode_msg



if __name__ == "__main__":

    # Example with default keys and message

    keyLeft = "ALZBHGUWIEFJCDYNMQRVKPTOXS"
    keyRight = "TWXLPRDZMNUGSAQKJHEBCIFYVO"

    cypher = Chiffrement1(keyLeft, keyRight)

    lisible = cypher.decode("PJMNEAJFCDJPMXVMTAQUARKNPZDMWOSEOLMQBGBZTGPTHUHYSOVDLXEYAPUYYNLKAWETEBMLAWBFFPDGVKGKUBTRYDJIVEACLBYVLOLRJROQCHMQHSILAKWJCNDLQSXBOMNKFXSFKDGVDLCWQYDNLH")
    print("Decoded message : ", lisible)


    # Example with custom keys and message
    leftkey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rightkey = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    cypher2 = Chiffrement1(leftkey, rightkey)

    illisible = cypher.encode("JESUISZIGGSUNYORDLEFOUQUIADORELESHEXPLOSIFSETPARCOURSLESMONTAGNESENCHANTANTDESCHANTSDEGUERREAVECDESBOMBESPLEINLESPOCHESETUNGRANDSOURIRESURLEVISAGECARJEMEFOUDESDANGERSJEFAISSAUTERTOUTCEQUIBOUGEMESAMISDISENTQUEJESUISUNPEUFOUMAISJESUISJUSTEPASSIONNEPARLESDETONATIONSETLECHAOSCREATIFQUIENDECOULE")
    lisible = cypher.decode(illisible)

    print("Encoded message : ", illisible)
    print("Decoded message : ", lisible)


    # Reponses aux questions :  
    # 1. Il s'agit d'un chiffrement de type substitution polyalphabétique, car il permet d'encoder une même lettre de 2 manières différentes. Par ailleurs, il s'agit d'un chiffrement symétrique, car il utilise la même clé pour le chiffrement et le déchiffrement.
    # 2. Considérant que la clé est constitué de deux chaines de 26 caractères distincts, il y a 26! * 26! combinaisons possibles.
    # 3. La sécurité de ce chiffrement est plutôt forte car il y a beaucoup de combinaisons possibles. Il est difficile de casser ce chiffrement, ne serait-ce qu'a cause de la présence de 2 clés.
    # 4. Ce chiffrement est plus sécurisé qu'un simple chiffrement de César, car il utilise deux clés différentes et permet de chiffrer une même lettre de plusieurs manières différentes. Cependant, il reste vulnérable de par sa nature symétrique. 