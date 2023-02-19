<h1 id="title">PyExtract </h1>

<h4>Ultima atualização: 19/02/2023 </h4>
<h2 id='anotacoes'>
Algumas anotações que merecem atenção abaixo:
</h2>
  
<h4>Existem tipos de conexões com o banco de dados da Oracle, como por exemplo abaixo: </h4>

    # Para o Python, precisamos de um client para poder fazer as conexões, por isso ultilizamos o InstantClient
    # Link abaixo:
    # https://www.oracle.com/br/database/technologies/instant-client/downloads.html


    # Pós Download só precisamos referenciar o PATH da pasta no codigo, como no exemplo abaixo:
    cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\usuario\Desktop\instantclient_21_9")
   
    # Metodo de Conexão 1: 
    connection = cx_Oracle.connect("usuario/senha@endereço:porta/nomedoendereço")
    
    # Metodo de conexão 2:
    dsn = cx_Oracle.makedsn(host='endereço', port=porta)
    connection = cx_Oracle.connect(user="usuario", password='senha',
                                   dsn=dsn,
                                   encoding="UTF-8")
<br>
<h4>
    Sendo assim, pós conexão, sendo obrigatorio fazer um cursor para commit e push no banco de dados. 
</h4>
    
    # Primeiro a direção do banco:
    cursor = connection.cursor()
    
    # Depois comando para a inserção *execute(SQL,PARAMETRIZAÇÕES)*
    cursor.execute(sql,dados)
    
    # E por fim, o commit que envia para o banco de dados:
    connection.commit()
<br>
<h4> E o mais importante de todos os comandos, o close da conexão: </h4>
    
    # Não podemos deixar a conexão aberta, mas a IDE do Python provavelmente irá alertar caso não feche.
    cursor.close()

<br>
<h2 id='extras'> Extras: </h2>
<h4> Como usar select pelo Python</h4>

    # sqlTxt = """select * from custom_tasy.AUX_copart_lojas_cem_fesp"""
    # row = cursor.fetchone()
    # b = row
    # b = str(b)
    # print(b)

<br>
<h4> Contar linhas de uma inserção ou select: </h4>
    
    # ContadorLinha = cursor.rowcount
    # print("Numero de linhas inseridas = ", ContadorLinha)

<h7 style = bold> Lembrando que o contador só funciona depois de usar o cursor.execute ! </h7>
<br>
<h4> Manipulação de arquivos existentes e/ou não:  </h4>
    
    #try:
    #   f = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste2.txt", "r")
    #   a = f.readlines()
    #   for linha in a:
    #       print(linha, "\n")
    #       print(len(a))
    #   f.close()
    #except FileNotFoundError:
    #    f = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste2.txt", 'w+')
    #    a = f.writelines("Vazio")
    #    f.close()
    #    print("Arquivo não encontrado, porém, criado.")

