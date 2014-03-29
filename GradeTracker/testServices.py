import gdata.docs.service

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, activityEdit, subactivityAdd, MyRegistrationForm
from django.contrib.auth.decorators import login_required


def googleTest( request ):
	# Create a client class which will make HTTP requests with Google Docs server.
	client = gdata.docs.service.DocsService()
	# Authenticate using your Google Docs email address and password.
	client.ClientLogin('alexdmail15@gmail.com', 'vpmqesd43')

	# Query the server for an Atom feed containing a list of your documents.
	documents_feed = client.GetDocumentListFeed()
	# Loop through the feed and extract each document entry.
	docs = []
	for document_entry in documents_feed.entry:
	 	# Display the title of the document on the command line.
	 	docs.append( document_entry.title.text )

	return render(request, 'GradeTracker/index.html', {'docs':docs } )  