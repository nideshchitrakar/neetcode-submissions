class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for s in strs:
            curr_len = len(s)
            encoded_str += f'{str(curr_len)}#{s}'

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        curr_index = 0

        while curr_index < len(s):
            j = curr_index
            while s[j] != '#':
                j += 1
            word_len = int(s[curr_index:j])
            decoded_list.append(s[j+1:j+1+word_len])
            curr_index = word_len + j + 1

        return decoded_list
