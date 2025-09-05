q50 = 0
m_alt = 0.0
q10_20 = 0
lt  = 0.0
q_p_40 = 0.0
for i in range(1,6,1):
    ida  = int(input("idade?"))
    alt  = float(input("altura?"))
    pes  = float(input("peso?"))
    
    if (ida >= 50):
        q50 = q50 + 1
        
    if (ida >= 10 and ida <=20):
        m_alt = m_alt + alt
        q10_20 = q10_20 + 1
        
    if (pes < 40):
        q_p_40 = q_p_40 + 1
        
print("+50id=",q50," media alt 10-20=",m_alt/q10_20,"-40k=",(100*q_p_40)/5)
    
