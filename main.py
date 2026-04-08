def explora(a):

    sitios_a_no_explorar = ["los baños", "el granero", "la madriguera"]
    printf"el alien {a} no va a explorar {random.choice(sitios_a_no_explorar)}")

def cosmos(a, p, g):
    for alien in a:
        print(
            f"El {alien} del planeta {random.choice(p)} de la galaxia {random.choice(g)}"
        )

explora(a)
