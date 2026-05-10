import math

def get_dist(pA, pB):
    return math.hypot(pA[0] - pB[0], pA[1] - pB[1])

def dito_su(p_polso, p_nocca, p_punta):
    return get_dist(p_punta, p_polso) > get_dist(p_nocca, p_polso)

def pugno(p, scala):
    return not dito_su(p[0], p[5], p[8]) and \
           not dito_su(p[0], p[9], p[12]) and \
           not dito_su(p[0], p[13], p[16]) and \
           not dito_su(p[0], p[17], p[20])

def ok(p, scala):
    cerchio = get_dist(p[4], p[8]) < (scala * 0.25)
    altre_dita = dito_su(p[0], p[9], p[12]) and \
                 dito_su(p[0], p[13], p[16]) and \
                 dito_su(p[0], p[17], p[20])
    return cerchio and altre_dita

def vittoria(p, scala):
    return dito_su(p[0], p[5], p[8]) and \
           dito_su(p[0], p[9], p[12]) and \
           not dito_su(p[0], p[13], p[16]) and \
           not dito_su(p[0], p[17], p[20])

def polliceinsu(p, scala):
    pollice_lontano = get_dist(p[4], p[5]) > (scala * 0.6)
    altre_chiuse = pugno(p, scala)
    return pollice_lontano and altre_chiuse