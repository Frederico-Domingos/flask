def orderListe(list):
    lis1, lis2, lis3, lis4 = [], [], [], []
    for value in list:
        lis1.append(value[1])
        lis2.append(value[2])
        lis3.append(value[3])
        lis4.append(value[4])

    return lis1, lis2, lis3, lis4

def teste_disc(list,qualidade,Perguntas):
    area_da_gestão, area_da_medicina, area_da_informatica, area_da_contabilidade = Perguntas
    influente, dominante, estavel, analitico = qualidade
    i, d, e, a = 0, 0, 0, 0
    ag, am, ai, ac = 0, 0, 0, 0
    for value in list:
        if influente.__contains__(value):
            i += 3.33
        if dominante.__contains__(value):
            d += 3.33
        if estavel.__contains__(value):
            e += 3.33
        if analitico.__contains__(value):
            a += 3.33
        if area_da_gestão.__contains__(value):
            ag += 7
        if area_da_informatica.__contains__(value):
            ai += 7
        if area_da_medicina.__contains__(value):
            am += 7
        if area_da_contabilidade.__contains__(value):
            ac += 7

    result = {
        "influente": i,
        "dominante": d,
        "estavel": e,
        "analitico": a,
        "area_da_gestao": ag+d,
        "area_da_medicina": am+e,
        "area_da_informatica": ai+i,
        "area_da_contabilidade": ac+a
    }

    return result
