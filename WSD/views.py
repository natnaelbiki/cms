from .models import Branch, Manager
from django.views.generic import TemplateView, ListView
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'

class ManagerSearchResultsView(ListView):
    model = Manager
    template_name = 'manager_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("qm")
        print(query)
        return Manager.objects.filter(
            Q(name__icontains=query) | Q(position__icontains=query))

class BranchSearchResultsView(ListView):
    model = Branch
    template_name = 'branch_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("qb")
        print(query)
        return Branch.objects.filter(
            Q(name__icontains=query))

class ManagerView(ListView):
    model = Manager 
    template_name = 'manager.html'

class BranchView(ListView):
    model = Branch 
    template_name = 'branch.html'