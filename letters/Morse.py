
Keys = 'abcdefghijklmnopqrstuvwxyz0123456789'
Values = ['.-','-...','-.-.','-..','.','..-.','--.','....',
          '..','.---','-.-','.-..','--','-.','---','.--.',
          '--.-','.-.','...','-', '..-','...-','.--','-..-',
          '-.--','--..','-----','.----','..---','...--',
          '....-','.....','-....','--...','---..','----.']
CODE = dict(zip(Keys.upper(), Values))

Decode_value = CODE.keys()
Decode_key = CODE.values()
Decode_dict = dict(zip(Decode_key,Decode_value))

class Morse():
    def Decode(self,input):
        msg = input
        msg1 = msg.split()
        temp = []
        for s in msg1:
            if s in Decode_dict.keys():
                temp.append(Decode_dict[s])
        ans = str(temp)
        return answer
    
    def Encode(self,input):
        msg = input
        temp = []
        for s in msg:
            if s == ' ':
                temp.append('')
            else:
                temp.append(CODE[s.upper()] + '   ')
        ans = str(temp)
        ans = ans.replace('\'','')
        ans = ans.replace(',',' ')
        return ans