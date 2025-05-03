1.3) PJMNEAJFCDJPMXVMTAQUARKNPZDMWOSEOLMQBGBZTGPTHUHYSOVDLXEYAPUYYNLKAWETEBMLAWBFFPDGVKGKUBTRYDJIVEACLBYVLOLRJROQCHMQHSILAKWJCNDLQSXBOMNKFXSFKDGVDLCWQYDNLH

Le message une fois déchiffré est : ISEEAREDDOORANDIWANTITPAINTEDBLACKNOCOLORSANYMOREIWANTTHEMTOTURNBLACKISEETHEGIRLSWALKBYDRESSEDINTHEIRSUMMERCLOTHESIHAVETOTURNMYHEADUNTILMYDARKNESSGOES

1.4) Texte non-chiffré : JESUISZIGGSUNYORDLEFOUQUIADORELESHEXPLOSIFSETPARCOURSLESMONTAGNESENCHANTANTDESCHANTSDEGUERREAVECDESBOMBESPLEINLESPOCHESETUNGRANDSOURIRESURLEVISAGECARJEMEFOUDESDANGERSJEFAISSAUTERTOUTCEQUIBOUGEMESAMISDISENTQUEJESUISUNPEUFOUMAISJESUISJUSTEPASSIONNEPARLESDETONATIONSETLECHAOSCREATIFQUIENDECOULE

Texte chiffré avec  leftkey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    rightkey = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

MRFWMWRDHRRDAREHUWCTBKVMUEVCTXCRCCZTBLXGPWSNPJANAGNDUCSEBIBXUZFGUJETYWZTDUMSGFPYMCOWIBQTIRVTJTCSDADDFRKFOPWWGYKKRATPUILCHUOBIBMEDCHLLMAPTXLTZKLTKZDSTJJJOLKWOEUXEUIHYPXXHXJBJQXSMNHADBMGBFWSXNNVTTIRDTRBDWRGSKDQFTYRASOGSNYFCCECNKOKYVJBLCSZWJXVOPUSPZPMXHRWXNROBFQNEIPWLZCMPGMNNGSPGMBKCBUQFVSZTFJ

1.5)  
1. Il s'agit d'un chiffrement de type substitution polyalphabétique, car il permet d'encoder une même lettre de 2 manières différentes. Par ailleurs, il s'agit d'un chiffrement symétrique, car il utilise la même clé pour le chiffrement et le déchiffrement.
2. Considérant que la clé est constitué de deux chaines de 26 caractères distincts, il y a 26! * 26! combinaisons possibles.
3. La sécurité de ce chiffrement est plutôt forte car il y a beaucoup de combinaisons possibles. Il est difficile de casser ce chiffrement, ne serait-ce qu'a cause de la présence de 2 clés.
4. Ce chiffrement est plus sécurisé qu'un simple chiffrement de César, car il utilise deux clés différentes et permet de chiffrer une même lettre de plusieurs manières différentes. Cependant, il reste vulnérable de par sa nature symétrique. 


2.3) HANHARYMTPTLAYNCIPSITTITNOWRIOEFHOAEALOWIDIIGTNOSATTNSDOATNSSOEGSHLEFTTAMTODAGGITHSGTIDYTGEETSSSTETMOILJINNWGSNIEEISNAISTKNUELIYSYENNAUAAEILGYLTMUGNMUOASOGRNBTENMGNSWFIRBAJIJMEIGHIOTR

Le message une fois déchiffré est : WATCHINGGIRLSGOPASSINGBYITAINTTHELATESTTHINGIMJUSTSTANDINGINADOORWAYIMJUSTTRYINGTOMAKESOMESENSEOUTOFTHESEGIRLSGOPASSINGBYTHETALESTHEYTELLOFMENIMNOTWAITINGONALADYIMJUSTWAITINGONAFRIEND

2.4) Texte non-chiffré : ZIGGSESTUNYORDLEEXPLOSIFPASSIONNÉPARLESBOMBESORIGINAIREDEPILTOVERILSÈMELECHAOSAVECSESINVENTIONSDÉTONANTESTRANSFORMANTCHAQUECOMBATENUNFEUDARTIFICE

Texte chiffré avec 5 lignes et offset 3: EDSOEOROMSINNSCMFFSSRLOIINLSSRIETVÈEOASNOSATNFTHOBNEIIGTOELFSNRBEIADLESLAVEVIDNEAONACAUUTCZGUYEPPSÉAOBGNEIRLEHESETÉOSRRAQETNDREINXAPMIPICCNTTMUEA

2.5)
1. Quel est le type de chiffrement de cet algorithme ?
C’est un chiffrement par transposition, car il ne modifie pas les lettres du message mais change leur position selon un motif en vague.

2. Quel nombre de clés peut-on constituer ?
La clé est composée de deux entiers : n (≥ 2) et offset (entre 0 et 2n−3).
Pour chaque n, il y a 2n−3 valeurs possibles d'offset. Donc, si on limite n à une valeur maximale N, on aurait :
Nombre total de clés = somme de 2n−3 pour n de 2 à N.

3. Que pensez-vous de la sécurité de cet algorithme ?
Elle est faible pour des usages modernes : un attaquant peut facilement essayer toutes les petites combinaisons possibles de n et offset, surtout si le texte chiffré est court. Ce chiffrement ne résiste pas à une attaque par force brute ou à une analyse fréquentielle.

4. Quels sont ses principales qualités et défauts ?

Qualités :

Simple à comprendre et à implémenter.

Réversible sans perte de données.

Défauts :

Peu sécurisé.

Facilement cassable avec des outils modernes.

Dépend fortement de la longueur du message pour ne pas révéler la structure.