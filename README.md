# Brief_24_IA_parle_moi


# Présentation de l'application 

Cette application permet d'avoir une discussion avec une IA, nommée Lily.
Vous obtiendrez une réponse écrite et vocale, noubliez pas d'allumer le son de votre ordinateur pour profiter pleinement de l'expérience.

Concernant la conception de cette application, le back-end est codé en python grâce au framework Flask, le front-end est codé en HTML/CSS.

Elle utilise une API de Openai pour le génération de réponse et un SDK de Azure (speech sdk) pour la reconnaissance et la synthèse vocale.

# Guide d'utilisation 

Pour tester cette application, il vous suffit de suivre ces quelques étapes :

1) Téléchergez le repository sur git hub gâce à ce lien : https://github.com/lilifull/brief-24-ia-parle-moi.git

2) Créez un environnement virtuel et installez les bibliothèques nécaissaires à partir du fichier requirements.txt présent dans ce repository et activez-le.

4) Obtenez les clés nécaissaires pour l'utilisation de l'API openai et du SDK azure speech :
- https://platform.openai.com/docs/quickstart/build-your-application, vous permet d'obtenir la clé openai.
- https://portal.azure.com/#home, créez une ressource azure pour récuperer une clé et une région.

3) Utilisez le fichier .env.exemple pour entrer vos clés :
- OPENAI_API_KEY, pour l'API de openai 
- SPEECH_KEY, pour votre ressource azure
- SPEECH_REGION, pour la région azure de votre ressource
Rennomez ce fichier .env

4) Executez le script app.py

Voilà, vous êtes prêt pour discuter avec une IA !

## Note :

Si la reconnaissance vocale ne reconnait pas pour certains mots, vous pouvez les ajoutées dans la liste 'word_list' du fichier python utils, ces mots auront alors plus de chance d'être recunnu. 
Cette liste contient déjà certains mots non reconnu au départ : 'Sophana', 'C#', 'Scikit-learn', 'scipy', 'R', 'serverless', 'pytorch', 'seaborn', 'simplonien', 'simplonienne','Sirine','Lakhbir','Simplonline'.
Vous pouvez les tester.
