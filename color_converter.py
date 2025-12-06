# color_converter.py
# Auteur: [МУТЧИНГА Рози]
# Variante 6: Convertisseur RGB vers HEX
# Ce fichier fait partie du projet 'hello-engineer'

def main():
    print("=== CONVERTISSEUR RGB → HEX ===")
    print("Conversion des couleurs RGB en code hexadécimal")
    
    try:
        # Demander les valeurs RGB
        print("\nEntrez les valeurs RGB (0 à 255):")
        r = int(input("Rouge (R) : "))
        g = int(input("Vert  (G) : "))
        b = int(input("Bleu  (B) : "))
        
        # Vérifier que les valeurs sont valides
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("\n Erreur : Les valeurs doivent être entre 0 et 255 !")
            return
        
        # Convertir en hexadécimal
        hex_code = f"#{r:02X}{g:02X}{b:02X}"
        
        # Afficher le résultat
        print(f"\n Conversion réussie !")
        print(f"   RGB({r}, {g}, {b}) = {hex_code}")
        
        # Spécial variante 6
        if r == 255 and g == 128 and b == 0:
            print(f"\n✨ C'est la couleur de la variante 6 !")
            print("   #FF8000 = Orange vif")
        
    except ValueError:
        print("\n Erreur : Veuillez entrer des nombres entiers valides !")
    except Exception as e:
        print(f"\n Erreur inattendue : {e}")

# Point d'entrée principal
if __name__ == "__main__":
    main()
    print("\n" + "=" * 40)
    print("Programme terminé. Merci !")