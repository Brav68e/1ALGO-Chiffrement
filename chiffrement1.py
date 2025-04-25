class Chiffrement1():

    keyLeft = "ALZBHGUWIEFJCDYNMQRVKPTOXS"
    keyRight = "TWXLPRDZMNUGSAQKJHEBCIFYVO"

    def __init__(self):
        
        self.keyLeft = Chiffrement1.keyLeft
        self.keyRight = Chiffrement1.keyRight



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
        self.keyLeft = Chiffrement1.keyLeft
        self.keyRight = Chiffrement1.keyRight

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
        self.keyLeft = Chiffrement1.keyLeft
        self.keyRight = Chiffrement1.keyRight

        return decode_msg



if __name__ == "__main__":

    cypher = Chiffrement1()

    print(cypher.decode("PJMNEAJFCDJPMXVMTAQUARKNPZDMWOSEOLMQBGBZTGPTHUHYSOVDLXEYAPUYYNLKAWETEBMLAWBFFPDGVKGKUBTRYDJIVEACLBYVLOLRJROQCHMQHSILAKWJCNDLQSXBOMNKFXSFKDGVDLCWQYDNLH"))