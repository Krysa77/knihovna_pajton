import csv

class KnihovniSystem:
    def __init__(self, nazev_souboru):
        self.soubor = nazev_souboru
        self.knihy = self.nacti_knihy()

    def nacti_knihy(self):
        try:
            with open(self.soubor, 'r', encoding='UTF-8') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print('nenanlezen')
        except:
            print('chyba')
        finally:
            return []
    
    def uloz_knihy(self, json_soubor):
        with open(self.soubor, 'w', encoding='UTF-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.knihy[0].keys())
            writer.writeheader()
            writer.writerows(self.knihy)

system = KnihovniSystem('knih.csv')
print(system.knihy[0]['nazev_knihy'])