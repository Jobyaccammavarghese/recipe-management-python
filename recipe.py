def add_recipe(recipe_name, recipe_ingredients, recipe_instructions):
    with open("recipes.txt", "a") as recipes_file:
        recipes_file.write(f"{recipe_name}\n")
        recipes_file.write(f"Ingredients:\n{recipe_ingredients}\n")
        recipes_file.write(f"Instructions:\n{recipe_instructions}\n\n")

def view_recipes():
    with open("recipes.txt", "r") as recipes_file:
        recipes = recipes_file.read().split("\n\n")
        for recipe in recipes:
            print(recipe)
            print()

def search_recipe(recipe_name):
    with open("recipes.txt", "r") as recipes_file:
        recipes = recipes_file.read().split("\n\n")
        for recipe in recipes:
            if recipe_name in recipe:
                print(recipe)
                return
        print(f"No recipe with the name '{recipe_name}' was found.")

while True:
        print("Welcome to the Recipe Book!")
        print("Select an option:")
        print("1. Add a recipe")
        print("2. View all recipes")
        print("3. Search for a recipe")
        print("4. Quit")

        option = int(input())
        if option == 1:
            recipe_name = input("Enter the name of the recipe: ")
            recipe_ingredients = input("Enter the ingredients of the recipe: ")
            recipe_instructions = input("Enter the instructions for the recipe: ")
            add_recipe(recipe_name, recipe_ingredients, recipe_instructions)
            print("Recipe added!")
        elif option == 2:
            view_recipes()
        elif option == 3:
            recipe_name = input("Enter the name of the recipe to search for: ")
            search_recipe(recipe_name)
        elif option == 4:
            break
        else:
            print("Invalid option, please try again.")

