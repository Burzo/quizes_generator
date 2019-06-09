from django.contrib import admin
from django.template.response import TemplateResponse
from django import forms
from django.urls import path
from django.http import HttpResponse

from .models import Quiz

from . import views



# Najprej nared custom admin site
class QuizAdmin(admin.ModelAdmin):
    

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('addWords/', self.admin_site.admin_view(self.my_view), name='addWords')
        ]
        return my_urls + urls

    def my_view(self, request):
        
        if request.method == 'POST':
            print("DELA")


        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/change_form.html", context)

# ---- Custom site narjen



admin.site.register(Quiz, QuizAdmin)


# -- https://medium.com/@adriennedomingus/adding-custom-views-or-templates-to-django-admin-740640cc6d42 ---














# -----------------------Normal---------------------------------------------
# This is to show the big field with all the words below
# class WordsInline(admin.TabularInline):
#     model = models.Word

# Register your models here.
# admin.site.register(models.Word)

#------------------------- Different view yet the same basic view -------------------------------------------
# From https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
# Define the new admin class.

# class WordAdmin(admin.ModelAdmin):
#     #list_display = ("word1", "translatedWord1") - changes the table view 
#     # fields = [("word1", "translatedWord1"), ("sentenceStart1", "sentenceEnd1")]

#     # Just inlines to show the upper WordsInline
#     # inlines = [WordsInline]

#     # Can only be fields or fieldsets
#     fieldsets = (
#         ("Translated Words", {
#             "fields": (
#                 ("word1", "translatedWord1")
#             ),
#         }),
#         ("Sentence", {
#             "fields": (
#                 ("sentenceStart1", "sentenceEnd1")
#             )
#         })
#     )
    

# # Register it like before
# admin.site.register(models.Word, WordAdmin)