class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "###EMPTY###"
        encoded_string = ""
        for i in strs:
            encoded_string += i
            encoded_string += "1!1!1!"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "###EMPTY###":
            return []
        decoded_strs = s.split("1!1!1!")
        if decoded_strs != [""]:
            decoded_strs.pop()
        return decoded_strs