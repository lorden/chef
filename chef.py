from tts import TTS
from recipe_parser import RecipeParser


if __name__ == '__main__':
    tts = TTS()
    rp = RecipeParser('icecreamcone.json')
    text = raw_input('Say:')
    while text:
        if text == 'ingredients':
            ingredients = rp.get_ingredients()
            for ingredient in ingredients:
                tts.say(ingredient)
        elif text == 'instructions':
            instructions = rp.get_instruction()
            for instruction in instructions:
                tts.say(instruction[0:100])
        elif rp.find_ingredient(text):
            ingredient = rp.find_ingredient(text)[0]
            tts.say(ingredient['amount'] + ' ' + ingredient['ingredient'])

        text = raw_input('Say:')
