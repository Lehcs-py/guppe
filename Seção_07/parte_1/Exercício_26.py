print("""
26. Faça um programa que calcule o desvio padrão de um matriz v contendo n = 10 números, onde m é A media do matriz.
    Desvio Padrão = d= √[(v1-m)²+...(v10-m)²]/(10-1)
""")

v = [36, 70, 7, 73, 45, 19, 22, 25, 90, 92]

m = sum(v)/len(v)  # media
mq = 0  # media dos quadrados da diferença

for num in v:
    mq += (m - num)**2

d = (mq/len(v))**0.5

print(d)
