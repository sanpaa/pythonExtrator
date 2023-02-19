# PyExtract (Unimed Salto-Itu)
<h4>Ultima atualização: 19/02/2023 </h4>
<h2>
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
<h4>
    Sendo assim, pós conexão, sendo obrigatorio fazer um cursor para commit e push no banco de dados.
    <br>Abaixo mais alguns Exemplos:</br>
<h4>
    
    # Primeiro a direção do banco:
    cursor = connection.cursor()
    
    # Depois comando para a inserção *execute(SQL,PARAMETRIZAÇÕES)*
    cursor.execute(sql,dados)
    
    # E por fim, o commit que envia para o banco de dados:
    connection.commit()

