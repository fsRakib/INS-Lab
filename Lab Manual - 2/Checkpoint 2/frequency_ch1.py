def frequency_analysis(text):
    # Remove spaces and punctuation for analysis
    clean_text = ''.join(c for c in text.lower() if c.isalpha())
    total_chars = len(clean_text)
    
    freq = {}
    for char in clean_text:
        freq[char] = freq.get(char, 0) + 1
    
    # Convert to percentages
    for char in freq:
        freq[char] = (freq[char] / total_chars) * 100
    
    # Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

cipher1 = "af p xpkcagynpk pfg, af ipqe qpri, gauulkifc tpw, ceiri udvk tiki afgaxiffphni cd eao-wvmd popkwn, higpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd ifdt cepc au pfwceafm epxxiffg cd ringdf eaorinu hiudki cei opcelopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc-pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir–ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe"

print("Cipher-1 Frequencies:")
freq1 = frequency_analysis(cipher1)
for char, percent in freq1:
    print(f"{char}: {percent:.2f}%")