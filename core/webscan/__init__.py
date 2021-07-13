from Wappalyzer import WebPage

def run_wappalizer(domain):
    try:
        web = WebPage.WebPage(domain)
        print(f"Teknologi yang digunakan Website : {domain}\n")
        for tech in web.apps:
            print(tech)
    except:
        print(f"Website {domain} dalam keadaan Down")

if __name__ == '__main__':
    domain = "http://amikom.ac.id"
    run_wappalizer(domain)
    