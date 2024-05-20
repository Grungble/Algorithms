import heapq

message = 'marko is a big dum dum'

letter_dict = {}

def letter_counter(uncoded_text:str,letter_dict:dict):
    for letter in uncoded_text:
        current_num = uncoded_text.count(letter)
        if letter in letter_dict:
            pass
            #print(f'{letter} is in the dictionary already')
        else:
            letter_dict.update({f'{letter}':current_num})
            #print(letter_dict)
    return letter_dict
if __name__ == '__main__':
    print(letter_counter(message,letter_dict))
    