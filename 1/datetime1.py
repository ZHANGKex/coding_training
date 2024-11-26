from datetime import timedelta
def next_week(d):
    return d + timedelta(days=7)


if __name__ == "__main__":
    from datetime import date

    # Test simple
    print(next_week(date(2024, 1, 1)))  # Résultat attendu : 2024-01-08

    # Test avec changement de mois
    print(next_week(date(2024, 2, 27)))  # Résultat attendu : 2024-03-05 (année bissextile)

    # Test avec un jour en milieu de mois
    print(next_week(date(2024, 3, 15)))  # Résultat attendu : 2024-03-22

    # Test avec la fin d'année
    print(next_week(date(2023, 12, 29)))  # Résultat attendu : 2024-01-05
