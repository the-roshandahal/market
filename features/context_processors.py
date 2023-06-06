from .models import Snippet
from themes.models import CompanySetup
def header_snippets(request):
    if Snippet.objects.exists():
        snippet = Snippet.objects.all()[0]
    else:
        snippet = None
    if CompanySetup.objects.exists():
        company = CompanySetup.objects.all()[0]
    else:
        company = None

    context = {
        'snippet': snippet,
        'company': company,
    }
    return context
