def explora(a):
    sitios_a_explorar = ['rio, lago, campo']
    print(f"el alien {a} explora {random.choice(sitios_a_explorar)}")

def cosmos(a, p, g):
    for alien in a:
        print(
            f"El {alien} del planeta {random.choice(p)} de la galaxia {random.choice(g)}"
        )

explora(a)
