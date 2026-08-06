class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        number = ""
        i=0
        while i < len(s):
            if s[i]=='#':
                decoded_strs.append(s[i+1:i+1+int(number)])
                i += int(number)+1
                number = ""
            else: 
                number+= s[i]
                i+=1
        return decoded_strs
