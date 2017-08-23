import email, getpass, imaplib, os, re

from django.core.management.base import BaseCommand, CommandError
from scrape.models import Link
from django.utils import timezone


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('from_email')
        parser.add_argument('my_email')
        parser.add_argument('my_pwd')

    def handle(self, *args, **options):
        usr = options["my_email"]
        pwd = options["my_pwd"]

        m = imaplib.IMAP4_SSL("imap.gmail.com")
        m.login(usr, pwd)

        m.select()

        resp, items = m.search(None, '(FROM "' + options["from_email"] + '")')
        items = items[0].split()[::-1]

        regional_links = [""] * 7

        # Regions to Index Matching:
        # 0 : Central
        # 1 : Western
        # 2 : SW
        # 3 : Midwest
        # 4 : SE
        # 5 : NE
        # 6 : Florida

        ii = 0

        for i in items:
            ii += 1
            if not "" in regional_links:
                break

            r, d = m.fetch(i, "(UID BODY[TEXT])")

            whole_email_str = d[0][1].decode("utf-8")
            #print(r)
            #print(d[0][1].decode("utf-8"))
            # f = open("helloworld" + str(ii) + ".html",'w')
            # f.write(d[0][1].decode("utf-8"))
            # f.close()

            regionals = [False] * 7
            if (re.search("CENTRAL UNITED STATES", whole_email_str) != None):
                regionals[0] = True
            elif (re.search("SOUTHWESTERN UNITED STATES", whole_email_str) != None):
                regionals[2] = True
            elif (re.search("MIDWESTERN UNITED STATES", whole_email_str) != None):
                regionals[3] = True
            elif (re.search("WESTERN UNITED STATES", whole_email_str) != None):
                regionals[1] = True
            elif (re.search("SOUTHEASTERN UNITED STATES", whole_email_str) != None):
                regionals[4] = True
            elif (re.search("NORTHEASTERN UNITED STATES", whole_email_str) != None):
                regionals[5] = True
            elif (re.search("FLORIDA UNITED STATES", whole_email_str) != None):
                regionals[6] = True

            
            if ((regionals[0] and regional_links[0] != "") or (regionals[1] and regional_links[1] != "") or (regionals[2] and regional_links[2] != "") or (regionals[3] and regional_links[3] != "") or (regionals[4] and regional_links[4] != "") or (regionals[5] and regional_links[5] != "") or (regionals[6] and regional_links[6] != "")):
                continue


            click_url_uncoded = re.search("(http).*(\n.*)?", whole_email_str).group(0)
            click_url_partial = click_url_uncoded.replace("=3D", "=")
            click_url = click_url_partial.replace(">*", "")
            click_url = click_url.replace("=\r\n", "")
            click_url = click_url.replace("\r", "")
            regional_links[regionals.index(True)] = click_url

        try:
            l = Link.objects.filter(region_name="central")[0]
            l.region_link = regional_links[0]
        except:
            l = Link(region_name="central", region_link=regional_links[0])
        l.save()

        try:
            l = Link.objects.filter(region_name="western")[0]
            l.region_link = regional_links[1]
        except:
            l = Link(region_name="western", region_link=regional_links[1])
        l.save()

        try:
            l = Link.objects.filter(region_name="southwestern")[0]
            l.region_link = regional_links[2]
        except:
            l = Link(region_name="southwestern", region_link=regional_links[2])
        l.save()

        try:
            l = Link.objects.filter(region_name="midwestern")[0]
            l.region_link = regional_links[3]
        except:
            l = Link(region_name="midwestern", region_link=regional_links[3])
        l.save()

        try:
            l = Link.objects.filter(region_name="southeastern")[0]
            l.region_link = regional_links[4]
        except:
            l = Link(region_name="southeastern", region_link=regional_links[4])
        l.save()

        try:
            l = Link.objects.filter(region_name="northeastern")[0]
            l.region_link = regional_links[5]
        except:
            l = Link(region_name="northeastern", region_link=regional_links[5])
        l.save()

        try:
            l = Link.objects.filter(region_name="florida")[0]
            l.region_link = regional_links[6]
        except:
            l = Link(region_name="florida", region_link=regional_links[6])
        l.save()




        
            

