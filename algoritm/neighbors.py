def getGraph():
    graph={
        #'CiudadOrigen':{'Vecino1': distancia,'vecino2':d},
        'Acacías':{'San Martin': 33,'Tauramena':142},
        'Aguadas':{'Marmato': 22,'Villeta':128},
        'Aipe':{'Vistahermosa': 172,'Campoalegre':65},
        'Bogotá':{'Ibague': 133,'La Calera':12,'Salamina':175},
        'Campoalegre':{'Aipe':65,'Rivera':13,'Gigante':51},
        'Chía':{'La Calera':19,'Villeta':49,'Sopo':14},
        'Chocontá':{'Ubaté':26,'Villeta':49,'Sopo':38},        
        'Garzón':{'Pitalito':60,'Puerto Rico':61,'Gigante':14},
        'Gigante':{'Garzón':14,'Campoalegre':51},
        'Hato Corozal':{'Ubaté':246,'Paz de Ariporo':34},
        'Ibague':{'Bogotá': 133,'Palermo':174},
        'La Calera':{'Bogotá': 12,'Chía':19},
        'La Dorada':{'Neira':100,'Villeta':55},
        'Manizales':{'Neira':12,'Palermo':241},
        'Marmato':{'Aguadas':22,'Salamina':15},
        'Neira':{'La Dorada':100,'Manizales':12},
        'Palermo':{'Ibague':174,'Manizales':241,'Rivera':23},
        'Paz de Ariporo':{'Hato Corozal':34,'Pore':20},
        'Pitalito':{'Puerto Rico': 99,'Garzón':60},
        'Pore':{'Paz de Ariporo':20,'Yopal':62},
        'Puerto Rico':{'Pitalito':99,'Garzón':61},        
        'Rivera':{'Campoalegre':13,'Palermo':23},
        'Salamina':{'Marmato':15,'Bogotá':175},
        'San Martin':{'Acacías':33,'Vistahermosa':63},
        'Sopo':{'Chía':14,'Chocontá':38},
        'Tauramena':{'Acacías':142,'Yopal':84},
        'Ubaté':{'Chocontá': 26,'Hato Corozal':246},
        'Villeta':{'Aguadas':128,'Chía':49,'La Dorada':55},
        'Vistahermosa':{'San Martin':63,'Aipe': 172},
        'Yopal':{'Pore':62,'Tauramena':84}
    }
    return graph

def getPosition():    
    position={
        'Bogotá':0,
        'Acacías':270,
        'Aguadas':100,
        'Aipe':170,
        'Campoalegre':130,
        'Chía':40,
        'Chocontá':110,        
        'Garzón':200,
        'Gigante':160,
        'Hato Corozal':180,
        'Ibague':20,
        'La Calera':10,
        'La Dorada':120,
        'Manizales':190,
        'Marmato':60,
        'Neira':150,
        'Palermo':50,
        'Paz de Ariporo':220,
        'Pitalito':230,
        'Pore':260,
        'Puerto Rico': 240,  
        'Rivera':90,
        'Salamina':30,
        'San Martin':250,
        'Sopo':70,
        'Tauramena':290,
        'Ubaté':140,
        'Villeta':80,
        'Vistahermosa':210,
        'Yopal':280
    }
    return position

    
    