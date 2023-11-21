text = input()
unique_symbols = ''
repetitions = ''
current_symbol = '' #collection
for index in range(len(text)):
    if not text[index].isdigit(): #we have non-numeric character
        current_symbol += text[index].upper()
    else: #we have digit here --> number for repetition
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ''
        repetitions = ''
print(f'Unique symbols used: {len(set(unique_symbols))}')
print(unique_symbols) # rage message