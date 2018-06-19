from django import forms
from django.conf import settings
import requests

class TriviaForm(forms.Form):
    def question(self):
        result = {}
        response = requests.get('https://opentdb.com/api.php?amount=1&type=boolean')
        if response.status_code == 200:  # SUCCESS
            result = response.json()[1]
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found'
            else:
                result['message'] = 'Trivia is not available at the moment. Please try again later.'
        return result









class ChuckForm(forms.Form):

    def reply(self):
        result ={}
        endpoint = 'https://api.chucknorris.io/jokes/random'
        reply= requests.get('https://api.chucknorris.io/jokes/random')
        if reply.status_code == 200:
            result = reply.json()
            result['success']
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'Even Chuck Norris takes a vacation. Please try again later.'
            else:
                result['message'] = 'Even Chuck Norris takes a vacation. Please try again later.'
        return result


class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=25)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        return result



class SynonymsForm(forms.Form):
    word = forms.CharField(max_length=25)

    def search(self):
         result = {}
         word = self.cleaned_data['word']
         endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}/synonyms;antonyms'
         url = endpoint.format(source_lang='en', word_id=word)
         headers= { 'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
         response = requests.get(url, headers=headers)
         if response.status_code == 200:  # SUCCESS
             result = response.json()
             result['success'] = True
         else:
             result['success'] = False
             if response.status_code == 404:  # NOT FOUND
                 result['message'] = 'No entry found for "%s"' % word
             else:
                 result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
         return result


class AntonymsForm(forms.Form):
    word = forms.CharField(max_length=25)

    def search(self):
         result = {}
         word = self.cleaned_data['word']
         endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}/synonyms;antonyms'
         url = endpoint.format(source_lang='en', word_id=word)
         headers= { 'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
         response = requests.get(url, headers=headers)
         if response.status_code == 200:  # SUCCESS
             result = response.json()
             result['success'] = True
         else:
             result['success'] = False
             if response.status_code == 404:  # NOT FOUND
                 result['message'] = 'No entry found for "%s"' % word
             else:
                 result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
         return result
