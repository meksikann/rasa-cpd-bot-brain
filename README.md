# Starter Pack for Rasa Stack

This starter pack helps you build a bot faster with [Rasa Stack](http://rasa.com/products/rasa-stack/). Apart from a basic file and folder structure, it gives you some initial training data. Clone this repo and start building your bot.

For more information on the Rasa Stack, please visit the docs here:
- [Rasa Core](https://core.rasa.com/)
- [Rasa NLU](https://nlu.rasa.com/)

## Setup
```
pip install rasa_core
```


RASA-NLU with spyCy ***************************************
```
pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

   == for tensorflow *****************************************
```
pip install rasa_nlu[tensorflow]
```
To install the necessary requirements, run:

```
pip install -r requirements.txt
```
install all dependencies ever needed
```
pip install -r alt_requirements/requirements_full.txt
```
*****************************************************************

Install duckling local if you use ner_duckling_http in pipelene (duckling used to recognize mostly etc. dates https://duckling.wit.ai/)
http://rasa.com/docs/nlu/master/components/#id2

```
docker run -p 8000:8000 rasa/duckling
```


## Usage

To train the NLU model, run ``make train-nlu``

To train the Core model, run ``make train-core``

To run the bot on the command line run ``make cmdline``
To run the core-server on the command line run ``make core-server``

## What now?

To continue developing your bot, you can start by adding some NLU data for intents/entities relevant to your use case. These then need to be added to your domain file. From there you can add more utterances for the bot, or custom actions you've written in `actions.py` and then write stories using these. 


## test nlp url:
http://localhost:5005/conversations/default/parse?query=hello
