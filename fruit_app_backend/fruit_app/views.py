from django.shortcuts import render
from django.http import JsonResponse

def send_fruits(request):
    fruits = [
        {
            "name": "Apfel", 
            "gewicht": 150,
            "farbe": "Rot"
        },
        {
            "name": "Banane", 
            "gewicht": 120,
            "farbe": "Gelb"
        },
        {
            "name": "Blaubeere", 
            "gewicht": 2,
            "farbe": "Blau"
        },
        {
            "name": "Mango", 
            "gewicht": 300,
            "farbe": "Orange"
        },
        {
            "name": "Kiwi", 
            "gewicht": 70,
            "farbe": "Grün"
        }
    ]
    return JsonResponse(fruits, safe=False)
