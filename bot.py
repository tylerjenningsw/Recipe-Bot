import nextcord
import nextcord.ext.commands
import os
from datetime import date
import pyrebase
from dotenv import load_dotenv
from database import firebaseConfig

client = nextcord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# TODO: Setup inital command with modal prompting users of recipe name/ingredients


@client.slash_command(name="Recipe", description="Recipe bot commands!", guild_ids=[977909622230900766])
@nextcord.ext.commands.cooldown(1, 60, type=nextcord.ext.commands.BucketType.default)
async def recipe(interaction: nextcord.Interaction):
    pass


@recipe.subcommand(name="Add recipe", description="Add a recipe to the recipe list")
async def add(interaction: nextcord.Interaction):
    await interaction.response.send_message("Added recipe!")

# TODO: Get specific recipe from database

# TODO: Get random recipe from database

# TODO: Setup databse (FireBase)


def new_recipe(recipe_name: str, ingredient_list: list[str], instructions: str, date: date, user: str):
    try:
        for ingredients in range(len(ingredient_list)):
            ingredient = ingredient_list[ingredients]
            ingredient = ingredient.lower()
            for letters in range(len(ingredient) - 1):
                currentletter = ingredient_list[ingredients][letters]
                nextletter = ingredient_list[ingredients][letters + 1]
                if currentletter is ' ' and nextletter.isalpha():
                    nextletter = nextletter.upper()

        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()
        data = {
            "Recipe": recipe_name,
            "Ingredients": ingredient_list,
            "Instructoons": instructions,
            "Date created": date,
            "Author": user
        }
        db.child(f"{recipe_name} by {user}").set(data)
    except Exception as e:
        print(f"Error - Data Entry Add Failed: {e}")

# TODO: Take input of users and pass it to database


try:
    load_dotenv()
    token = os.getenv("TOKEN")
    client.run(token)
except Exception as e:
    print(f"Error - Login Failed: {e}")
