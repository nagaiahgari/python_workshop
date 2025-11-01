"""
  Author : Balaji Nagaiahgari
  install pyjokes external module before executing this program using the command "pip install pyjokes"
"""
import pyjokes


joke=pyjokes.get_joke();

print("printing some randome jokes using pyjokes external module.............")

print(joke)