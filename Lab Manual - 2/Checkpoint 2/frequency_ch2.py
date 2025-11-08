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

# cipher1 = "af p xpkcagynpk pfg, af ipqe qpri, gauulkifc tpw, ceiri udvk tiki afgaxiffphni cd eao-wvmd popkwn, higpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd ifdt cepc au pfwceafm epxxiffg cd ringdf eaorinu hiudki cei opcelopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc-pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir–ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe"

# print("Cipher-1 Frequencies:")
# freq1 = frequency_analysis(cipher1)
# for char, percent in freq1:
#     print(f"{char}: {percent:.2f}%")
cipher2 = "aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zemdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vulkqvm. klu vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumi, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu leee ok aon umj toz sqee hs kqmmuez zkqssuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz vyhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zhhr klucv luojz omj kllhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok omghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmublogxkaeu tuoekl. ck teee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu teee dhwu hs ckl aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl lez whmug, whzk yuhyeu tuvu teeecmn kh shvncpu low lez hijckcuz omj lez nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuwvz tckl lez vueokcpuz (ubduyk, hs dhqvzu, klu zodrpeeuaonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhnm klu lhaackz hs yhhv omj qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lez ghqmnuv dhqzcmz aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz. tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lez lucv, omj avhqnik low kh ecpu ok aon umj; omj klu lhyuz hs klu zodrpeeau- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu, svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hay acvkljog-yovkcuz dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lez ktuumz, oz klu lhaackz doeeuj klu cvvuzyhmzeaeu ktumkcuz auktuum dicejlhhj omj dhwcnm hs onu ok klcwkg-klvuu"

print("Cipher-2 Frequencies:")
freq2 = frequency_analysis(cipher2)
for char, percent in freq2:
    print(f"{char}: {percent:.2f}%")