class keyboard:
    def forward(self,letter):
        signal="ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self,signal):
        letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter
    
#k=keyboard()
#print(k.forward("A"))
#print(k.backward(0))