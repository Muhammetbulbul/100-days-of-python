#random modülü eklenir.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#index alabilmek için her bir görseli tek bir atamaya koyuyoruz.
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
#randint kullanmamızın sebebi 0-2 arasındaki tam sayıları rastgele bize vermesi.
computer_choice = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer_choice])

#sistemin ilk denetlemesi gereken şey hata var mı yok mu ? Bu sebepten ötürü hata mesajını inceliyoruz.
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
#Bu kısımda sadece iki istisna durum var 2/0 ve tam tersi. Geri kalan her bir ölçek eşit olmadığı sürece birbirlerini eliyorlar.
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")