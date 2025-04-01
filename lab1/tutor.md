# Moj tutorijal

## Autor: Ana Novković

`git clone REPO` - Klonira repozitorij s predanog URL-a

`git status` - Prikazuje trenutno stanje brancha

`git add FILE` - Dodaje file u staging, tj. priprema izmjene na fileu za commit

`git log` - Prikazuje povijest (commitove) trenutnog brancha

`git diff` - Prikazuje izmjene između trenutnog stanja u radnom
direktoriju i trenutnog staginga

`git commit -m "PORUKA"` - Kreira novi commit sa predanom porukom

`git push REMOTE BRANCH` - Šalje izmjene na repozitorij REMOTE na
branch BRANCH

## Commitanje i pushanje nove izmjene

```bash
git status # Provjerimo putanju filea
git add FILE # Dodajemo file u staging
git status # Provjerimo da je ispravno dodano
git commit -m "PORUKA" # Kreiramo novi commit
git log # Provjerite je li kreiran
git push REMOTE BRANCH # Pushamo kreirani commit 
```

## Povlačenje izmjena s udaljenog repozitorija 

```bash
git pull origin master # Ako radi git push bez remotea i brancha, radit će i pull
```