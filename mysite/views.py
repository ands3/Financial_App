from django.shortcuts import render
import pandas as pd
from .utils import scrape_to_df
from .models import GDP, GNP

# Create your views here.
def homepage(request):
    
    GDP_df = scrape_to_df('GDP', '168300fd58f9d160f1ad9aecf9855f1b')
    for _, row in GDP_df.iterrows():
        GDP.objects.create(GDP_realtime_start=row['realtime_start'], GDP_date=row['date'], GDP_value=row['value'])           
    GDP_query_results = GDP.objects.all()
    
    GNP_df = scrape_to_df('GNP', '168300fd58f9d160f1ad9aecf9855f1b')
    for _, row in GNP_df.iterrows():
        GNP.objects.create(GNP_realtime_start=row['realtime_start'], GNP_date=row['date'], GNP_value=row['value'])           
    GNP_query_results = GNP.objects.all()
    
    context = {'GDP_symbol': 'GDP', 'GDP_query_results': GDP_query_results, 
               'GNP_symbol': 'GNP', 'GNP_query_results': GNP_query_results}
    
    return render(request, "pages/base.html", context)