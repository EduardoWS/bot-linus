import discord
from discord.channel import DMChannel
from discord.ext.commands.core import dm_only
import wikipedia
from discord.ext import commands
""" from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer """
import random
import json
""" from googletrans import Translator """
import asyncio
import psycopg2 as db

intents = discord.Intents.default()
intents.members = True



db_host = ""
db_user = ""
db_name = ""
db_pass = ""



client = commands.Bot(command_prefix = '-', case_insensitive = True, intents = intents)

@client.event
async def on_ready():
    print('O LINUS ESTÁ ONLINE!')
    """ global chatbot
    chatbot = ChatBot('Linus')
    global trainer
    trainer = ListTrainer(chatbot) """

""" @client.command()
async def treinar(ctx):
    

    trainer.train([
        'Olá!',
        'Oi',
        
        'Olá, como vai?',
        'Oi, estou bem e você?',

        'Estou bem!',
        'Como foi seu dia?',

        'Foi legal e o teu?',
        'Foi cansativo',

        'Qual é o seu nome?',
        'Me chamo Linus, prazer em te conhecer!'])

    trainer.train([
        'Entendi',
        'Então, me fale mais sobre você',
        'Legal',
        'Então, sobre o que quer conversar?',
        'Que bom!',
        'O que gosta de fazer?'])
    trainer.train([
        'Quantos anos você tem?',
        'Eu tenho 51 anos. Nasci no dia 28 de dezembro de 1969',
        'Qual sua musica favorita?',
        'Chopin - Nocturne op.9 No.2, sem dúvidas!!',
        'O que vc costuma fazer?',
        'Programar, escutar música e agradecer o meu criador Berserker por ter me dado vida.'
    ])
    await ctx.send('Treinamento concluído!')
 """
@client.listen('on_message')
async def on_message(message):
    content = message.content
    channel = message.channel
    author = message.author.name
    mention = message.author.mention
    
    

    #previnir erro
    if author == 'Linus':
        return


    """ elif type(message.channel) == discord.DMChannel:  #content.startswith('-') and 
        
        msg = content[1:]
        response = chatbot.get_response(msg)
        await channel.send(response)
 """

    


    if content == 'bom dia':
        await channel.send(f'Mau dia, {mention}!!')
    
    elif content == 'fala':
        rodar = random.randint(1, 5)
        if rodar == 1:
            await channel.send(f'Eae, meu chegado')
        
        elif rodar == 2:
            await channel.send(f'Fala, meu compatriota')
        
        elif rodar == 3:
            await channel.send(f'Não enche!!')
        
        elif rodar == 4:
            await channel.send(f'Opa, como vai?')

        elif rodar == 5:
            await channel.send(f'Cara? Sem tempo...')
        

    elif content == '-whois':
        await channel.send('Linus Benedict Torvalds, sou um engenheiro de software, nascido na Finlândia e naturalizado estado-unidense em 2010, sou o criador, e por muito tempo fui o desenvolvedor mais importante do núcleo Linux')

    elif content == '.inforifa' and channel.name == 'teste-linus':

        valores = list(range(1, 201))
        random.shuffle(valores)
        
        
        valor = json.dumps(valores, separators=(", ", " - "))
        await channel.send(valor)

""" @client.command()
async def ensinar(ctx):
    await ctx.send('Faça uma pergunta:')
    def check(message):
        if message.author == ctx.author and ctx.channel == message.channel:
            return check
    try:
        msg = await client.wait_for('message', check=check, timeout=60)
        msg = msg.content
        await ctx.send('Agora digite uma resposta para esta pergunta:')
        rsp = await client.wait_for('message', check=check, timeout=60)
        rsp = rsp.content
        trainer.train([
        f'{msg}',
        f'{rsp}'

        ])
        await ctx.send(f'Pergunta adicionada: `{msg}` \n\nResposta adicionada: `{rsp}`')

    except:
        await ctx.send('Tempo expirado.')
    
     """

@client.command()
async def p(ctx, *, search):
    
    wikipedia.set_lang('pt')
    try:
        pesquisa = wikipedia.summary(search)
        if len(pesquisa) > 2000:

            loc = pesquisa[:2000].rfind('.')
                
            await ctx.send(pesquisa[:loc+1])
            
            """ trainer.train([
            f'{search}',
            f'{pesquisa[:loc+1501]}'

            ]) """
                
        else:
            
            """ await ctx.send(pesquisa)
            trainer.train([
            f'{search}',
            f'{pesquisa}'

            ]) """

    except:
        await ctx.send('Não entendi o que você disse.')
    


# ====== JOGO DA FORCA ======
@client.command()
async def mudarid(ctx, idf):
    if ctx.channel.name == 'teste-bots':
        conn = db.connect(dbname=db_name, user=db_user, host=db_host, password=db_pass)
        cur = conn.cursor()
        cur.execute("UPDATE idforca SET id = %s", (idf, ))
        conn.commit()
        cur.close()
        conn.close()
        await ctx.send(f'ID mudado para {idf}!!')



@client.command()
async def forca(ctx, member1: discord.Member, member2: discord.Member=None, member3: discord.Member=None):
    
    if ctx.channel.name == 'teste-bots':
        conn = db.connect(dbname=db_name, user=db_user, host=db_host, password=db_pass)
        cur = conn.cursor()
        cur.execute("SELECT id FROM idforca")
        ressultado_id = cur.fetchone()

        if ressultado_id[0] == 0:
            if member2 == None:
                if ctx.author.id == member1.id:
                    await ctx.send(f'Você não pode jogar com você mesmo, seu solitário.')
                    return
                else:
                    cur.execute("UPDATE idforca SET id = 1")
                    conn.commit()
                    await ctx.send(f'{member1.mention} aguarde o **{ctx.author.name}** escolher uma palavra!')
            elif member2 != None and member3 == None:
                if ctx.author.id == member1.id or ctx.author.id == member2.id:
                    await ctx.send(f'Você não pode jogar com você mesmo, seu solitário.')
                    return
                else:
                    cur.execute("UPDATE idforca SET id = 1")
                    conn.commit()
                    await ctx.send(f'{member1.mention} e {member2.mention} aguardem o **{ctx.author.name}** escolher uma palavra!')
            elif member3 != None:
                if ctx.author.id == member1.id or ctx.author.id == member2.id or ctx.author.id == member3.id:
                    await ctx.send(f'Você não pode jogar com você mesmo, seu solitário.')
                    return
                else:
                    cur.execute("UPDATE idforca SET id = 1")
                    conn.commit()
                    await ctx.send(f'{member1.mention}, {member2.mention} e {member3.mention} aguardem o **{ctx.author.name}** escolher uma palavra!')

            escolhas = client.get_user(ctx.author.id)
            await escolhas.send('Escolha uma palavra:')

            def check(message):
                if message.author == ctx.author and not message.guild:
                    return check 
            try:
                palavra = await client.wait_for('message', check=check, timeout=180)
                palavra = palavra.content.upper()
                await escolhas.send('Agora digite uma dica:')
                dica = await client.wait_for('message', check=check, timeout=180)
                dica = dica.content.upper()
                
            except:
                cur.execute("UPDATE idforca SET id = 0")
                conn.commit()
                await escolhas.send('Tempo expirado. Coloque o comando `-forca @user` novamente no canal adequado.')
                return
            
            
            
            cur.execute("INSERT INTO forca (palavra, dica) VALUES (%s, %s)", (palavra, dica))
            conn.commit()
            
            
            
            palavra_secreta = '_' * len(palavra)
            t = ''
            jog1 = member1
            jog2 = member2
            jog3 = member3

            def encaixar(tent: str, palavra: str, palavra_secreta: str) -> str:
                palavra_lista = list(palavra_secreta)

                for index, letra in enumerate(list(palavra)):
                    if letra == tent:
                        palavra_lista[index] = tent
                
                palavra_secreta = "".join(palavra_lista)

                return palavra_secreta




            vez = jog1
            vida = 5
            spc = ''
            cont = 0

            while True:

                for n in range(1, len(palavra_secreta) + 1):
                    spc += palavra_secreta[n-1] + ' '
                
                if vida == 5:
                    h = '\❤️\❤️\❤️\❤️\❤️'
                elif vida == 4:
                    h = '\❤️\❤️\❤️\❤️'
                elif vida == 3:
                    h = '\❤️\❤️\❤️'
                elif vida == 2:
                    h = '\❤️\❤️'
                elif vida == 1:
                    h = '\❤️'
                emb = discord.Embed(
                title='JOGO DA FORCA',
                description=f'''
DICA: `{dica}`

{t}

` {spc}`


VIDAS: {h}

RODADA: {vez.mention}        
            '''
        )
                emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                await ctx.send(embed=emb)
                def check2(message):
                    
                    flag = 0
                    msg = message.content
                    if msg.isalnum() or msg.isascii():
                        flag = 1
                    
                    if message.author == vez and ctx.channel == message.channel and len(message.content) == 1 and flag == 1:
                        return check2
                    elif message.author == vez and ctx.channel == message.channel and message.content.upper()[:6] == 'CHUTAR':
                        return check2
                
                try:
                    tent = await client.wait_for('message', check=check2, timeout=60)
                    tent = tent.content.upper()
                    
                except:
                    if cont == 1 or vida == 1:
                        await ctx.send(f'{vez.mention} pensou tanto que perdeu.')
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='FIM DE JOGO ⚰️',
                            description=f'''
A palavra que o(a) {ctx.author.mention} escolheu foi:

` {spc}`

**USE `-forca @user` PARA COMEÇAR OUTRO JOGO**
                        '''
                    )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break

                    else:
                        if member2 == None:
                            await ctx.send(f'{vez.mention} pensou demais e perdeu 1 \❤️!')
                            spc = ''
                            vida -= 1
                            cont += 1
                            continue
                        elif member2 != None and member3 == None:
                            await ctx.send(f'{vez.mention} pensou demais. Perdeu a vez e 1 \❤️!')
                            spc = ''
                            vida -= 1
                            cont += 1
                            if vez == jog1:
                                vez = jog2
                            else:
                                vez = jog1
                            continue
                        elif member3 != None:
                            await ctx.send(f'{vez.mention} pensou demais. Perdeu a vez e 1 \❤️!')
                            spc = ''
                            vida -= 1
                            cont += 1
                            if vez == jog1:
                                vez = jog2
                            elif vez == jog2:
                                vez = jog3
                            elif vez == jog3:
                                vez = jog1
                            continue


                if tent[:6] == 'CHUTAR':
                    if tent[7:] == palavra:
                        
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='🎉 TEMOS UM GANHADOR 🎉',
                            description=f'''
**PARABÉNS {vez.mention} !!**

` {spc}`

VIDAS: {h}
                    '''
                )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break
                    else:
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='FIM DE JOGO ⚰️',
                            description=f'''
A palavra que o(a) {ctx.author.mention} escolheu foi:

` {spc}`

Lembre-se que se errar o chute você perde!!

**USE `-forca @user` PARA COMEÇAR OUTRO JOGO**
                    '''
                    )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break



                if tent in t and tent != '':
                    await ctx.send(f'{vez.mention} já tentaram essa letra!!')
                    if member2 != None and member3 == None:
                        if vez == jog1:
                            vez = jog2
                        else:
                            vez = jog1
                    elif member3 != None:
                        if vez == jog1:
                            vez = jog2
                        elif vez == jog2:
                            vez = jog3
                        elif vez == jog3:
                            vez = jog1
                    spc = ''
                    continue
                    
                else:
                    t += tent + ' '
                    



                if tent in palavra:
                    palavra_secreta = encaixar(tent, palavra, palavra_secreta)


                else:
                    vida -= 1
                    if vida == 0:
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='FIM DE JOGO ⚰️',
                            description=f'''
A palavra que o(a) {ctx.author.mention} escolheu foi:

` {spc}`

**USE `!forca @user` PARA COMEÇAR OUTRO JOGO**
                        '''
                    )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break




                if palavra_secreta == palavra:
                    spc = ''
                    for n in range(1, len(palavra_secreta) + 1):
                        spc += palavra_secreta[n-1] + ' '
                    emb = discord.Embed(
                        title='🎉 TEMOS UM GANHADOR 🎉',
                        description=f'''
**PARABÉNS {vez.mention} !!**

` {spc}`

VIDAS: {h}
                    '''
                )
                    emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                    await ctx.send(embed=emb)
                    cur.execute("UPDATE idforca SET id = 0")
                    conn.commit()
                    break

                if member2 != None and member3 == None:
                    if vez == jog1:
                        vez = jog2
                    else:
                        vez = jog1
                elif member3 != None:
                    if vez == jog1:
                        vez = jog2
                    elif vez == jog2:
                        vez = jog3
                    elif vez == jog3:
                        vez = jog1

                spc = ''
                cont = 0

        else:
            await ctx.send(f'{ctx.author.mention} já estão jogando comigo! Por favor, aguarde o jogo terminar.')
    else:
        await ctx.send('Canal errado bobinho(a)')
    cur.close()
    conn.close()


@client.command()
async def fs(ctx):
    if ctx.channel.name == 'teste-bots':
        conn = db.connect(dbname=db_name, user=db_user, host=db_host, password=db_pass)
        cur = conn.cursor()

        cur.execute("SELECT id FROM idforca")
        ressultado_id = cur.fetchone()
        
        if ressultado_id[0] == 0:

            cur.execute("SELECT * FROM forca ORDER BY random() LIMIT 1")
            resultado = cur.fetchall()

            palavra = resultado[0][0].upper()
            dica = resultado[0][1].upper()

            palavra_secreta = '_' * len(palavra)
            t = ''

            cur.execute("UPDATE idforca SET id = 1")
            conn.commit()

            def encaixar(tent: str, palavra: str, palavra_secreta: str) -> str:
                palavra_lista = list(palavra_secreta)

                for index, letra in enumerate(list(palavra)):
                    if letra == tent:
                        palavra_lista[index] = tent
                
                palavra_secreta = "".join(palavra_lista)

                return palavra_secreta

            vida = 5
            spc = ''
            cont = 0

            while True:

                for n in range(1, len(palavra_secreta) + 1):
                    spc += palavra_secreta[n-1] + ' '
                
                if vida == 5:
                    h = '\❤️\❤️\❤️\❤️\❤️'
                elif vida == 4:
                    h = '\❤️\❤️\❤️\❤️'
                elif vida == 3:
                    h = '\❤️\❤️\❤️'
                elif vida == 2:
                    h = '\❤️\❤️'
                elif vida == 1:
                    h = '\❤️'
                emb = discord.Embed(
                title='JOGO DA FORCA SINGLEPLAYER',
                description=f'''
DICA: `{dica}`

{t}

` {spc}`


VIDAS: {h}

JOGADOR: {ctx.author.mention}
        
            '''
        )
                emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                await ctx.send(embed=emb)
                def check2(message):
                    flag = 0
                    msg = message.content
                    if msg.isascii() or msg.isalnum():
                        flag = 1
                        
                    if message.author == ctx.author and ctx.channel == message.channel and len(message.content) == 1 and flag == 1:
                        return check2
                    elif message.author == ctx.author and ctx.channel == message.channel and message.content.upper()[:6] == 'CHUTAR':
                        return check2
                
                try:
                    tent = await client.wait_for('message', check=check2, timeout=60)
                    tent = tent.content.upper()
                    
                    

                    
                except:
                    if cont == 1 or vida == 1:
                        await ctx.send(f'{ctx.author.mention} pensou tanto que perdeu.')
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='FIM DE JOGO ⚰️',
                            description=f'''
A palavra que eu escolhi foi:

` {spc}`

**USE `-fs` PARA COMEÇAR OUTRO JOGO**
                        '''
                    )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break


                    else:
                        await ctx.send(f'{ctx.author.mention} pensou demais e perdeu 1 \❤️!')
                        spc = ''
                        vida -= 1
                        cont += 1
                        continue
                    
                    
                if tent[:6] == 'CHUTAR':
                    if tent[7:] == palavra:
                        
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='🎉 TEMOS UM GANHADOR 🎉',
                            description=f'''
**PARABÉNS {ctx.author.mention} !!**

` {spc}`

VIDAS: {h}
                    '''
                )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break
                    else:
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='FIM DE JOGO ⚰️',
                            description=f'''
A palavra que eu escolhi foi:

` {spc}`

Lembre-se que se errar o chute você perde!!

**USE `-fs` PARA COMEÇAR OUTRO JOGO**
                    '''
                    )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break



                if tent in t and tent != '':
                    await ctx.send(f'{ctx.author.mention} você já tentou essa letra!!')
                    
                else:
                    t += tent + ' '
                    



                if tent in palavra:
                    palavra_secreta = encaixar(tent, palavra, palavra_secreta)


                else:
                    vida -= 1
                    if vida == 0:
                        spc = ''
                        for n in range(1, len(palavra) + 1):
                            spc += palavra[n-1] + ' '
                        emb = discord.Embed(
                            title='FIM DE JOGO ⚰️',
                            description=f'''
A palavra que eu escolhi foi:

` {spc}`

**USE `-fs` PARA COMEÇAR OUTRO JOGO**
                        '''
                    )
                        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                        await ctx.send(embed=emb)
                        cur.execute("UPDATE idforca SET id = 0")
                        conn.commit()
                        break




                if palavra_secreta == palavra:
                    spc = ''
                    for n in range(1, len(palavra_secreta) + 1):
                        spc += palavra_secreta[n-1] + ' '
                    emb = discord.Embed(
                        title='🎉 TEMOS UM GANHADOR 🎉',
                        description=f'''
**PARABÉNS {ctx.author.mention} !!**

` {spc}`

VIDAS: {h}
                    '''
                )
                    emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/843496086089629716/863886769882923009/hangman-game-og-share.png')
                    await ctx.send(embed=emb)
                    cur.execute("UPDATE idforca SET id = 0")
                    conn.commit()
                    break

                spc = ''
                cont = 0

        else:
            await ctx.send(f'{ctx.author.mention} já estão jogando comigo! Por favor, aguarde o jogo terminar.')

    else:
        await ctx.send('Canal errado bobinho(a)')

    cur.close()
    conn.close()


""" @client.command()
async def trad(ctx, lg=None, *, pesquisar):
    trans = Translator()
    if lg == None:
        tradu = trans.translate(pesquisar, dest='pt', src='en')
    else:
        tradu = trans.translate(pesquisar, dest='pt', src=lg)
    await ctx.send(tradu.text) """










@client.event
async def on_member_join(member):
    channel = client.get_channel(831559846511378483)
    await channel.send(f'Bem-vindo(a), {member.mention}!')




client.run('')
