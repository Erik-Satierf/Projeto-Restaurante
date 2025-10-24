# Iniciar o git e mandar para o repositorio no Github

no terminal:
```bash
git init                        inicia o app git no projeto
git add .                       adiciona todos todos os arquivos no git para mandar para o github o . é importante
git commit -m ""                cria um ponto/commit, uma nova versao do original com suas alteraçoes "comentario"
git remote add origin http...   conecta o repositorio vs "repositorio local" ao site no github "repositorio online", precisa do http
git branch -m main              define a main
git push -u origin main         manda para o github e garante o salvamento lá
```
# Atualizar o github quando precisar "quando mudar algo"

no terminal:
```bash
git init            reinicia o app git
git add .
git commit -m ""    importante para dizer oq fez ex:"adicionei a classe exemplo"
git push            manda para o github e garante o salvamento lá