class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        delimiter = "#"
        for s in strs:
            encoded_string += str(len(s)) + delimiter + s
        print(encoded_string)
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        answer_list = []
        i = 0
        while i < len(s):
            current_length = int(s[i:].split('#')[0])
            current_length_digits = len(str(current_length))
            current_string = s[(i + current_length_digits + 1):(i + current_length_digits + 1 + current_length)]
            answer_list.append(current_string)
            i += current_length + current_length_digits + 1
        return answer_list

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))